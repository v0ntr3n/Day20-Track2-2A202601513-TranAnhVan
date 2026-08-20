# Reflection — Day 20 Lab (Personal Report)

> **Đây là báo cáo cá nhân.** Số liệu của bạn **không** so sánh được với bạn cùng lớp
> — chỉ so **before vs after trên chính máy bạn**. Rubric chấm độ rõ ràng của setup,
> đo lường và **lập luận**, không chấm tốc độ tuyệt đối.

**Họ Tên:** Trần Anh Văn
**Cohort:** A20-K1
**Ngày submit:** 2026-08-20

---

## 1. Hardware & runtime *(rubric 1, 2 — 10 điểm)*

> Từ `make probe`. Paste output hoặc điền tay.

* **OS:** Windows 11 (AMD64)
* **CPU:** Intel(R) Core(TM) i7-14700K
* **Cores:** 20 physical / 28 logical
* **CPU extensions:** AVX2 / AVX-512
* **RAM:** 31.8 GB
* **Accelerator:** NVIDIA GeForce RTX 4060 Ti (16 GB)
* **llama.cpp asset đã tải:** llama-b10488-bin-win-cuda-12.4-x64.zip
* **Model đã dùng:** Qwen3.5 0.8B (`LAB_MODEL=qwen35-0.8b`)
* **Quantization:** Q4_K_M + UD-Q2_K_XL (từ `models/active.json`)

**Chạy ở đâu:** laptop của tôi

**Setup story** (≤ 80 chữ): Running on Windows 11 required executing PowerShell `.\lab.ps1` targets instead of `make`. Python environment required setting `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8` to prevent Windows cp1252 encoding errors during report generation. Prebuilt llama.cpp CUDA binaries downloaded smoothly and loaded the GGUF weights onto the RTX 4060 Ti GPU.

---

## 2. Đo lường *(rubric 3, 4, 5 — 20 điểm)*

> Paste bảng từ `benchmarks/01-quickstart-results.md` (`make bench` tự sinh).

| Quantization | Size (GB) | Load (ms) | TTFT P50/P95 (ms) | TPOT P50/P95 (ms) | E2E P50/P95/P99 (ms) | Decode (tok/s) |
| --- | --- | --- | --- | --- | --- | --- |
| UD-Q4_K_XL | 0.50 | 1580 | 40 / 56 | 4.0 / 4.2 | 287 / 318 / 318 | 252.3 |
| UD-Q2_K_XL | 0.39 | 1525 | 52 / 111 | 3.8 / 4.0 | 280 / 353 / 353 | 260.6 |

**Quan sát** (≤ 60 chữ): `UD-Q2_K_XL` decodes 1.03× faster (260.6 vs 252.3 tok/s) and saves 0.11 GB VRAM, but TTFT P95 doubles from 56 ms to 111 ms due to 2-bit unpacking overhead. Since 0.50 GB easily fits in VRAM, `Q4_K_M` is much better due to superior output coherence and lower TTFT tail latency.

---

## 3. Serving under load *(rubric 8, 9, 10 — 20 điểm)*

> Từ `benchmarks/02-server-results.md` (`make load-report`).

| Users | RPS | P50 (ms) | P95 (ms) | P99 (ms) | Eff. concurrency | Failures |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 5.34 | 880 | 1700 | 2700 | 5.3 | 0.0% |
| 50 | 5.92 | 7300 | 8300 | 9700 | 41.9 | 0.0% |

* **Offered load tăng 5×, throughput thực tăng:** 1.11×
* **P95 tăng:** 4.88×
* **Effective concurrency ở 50 users:** 41.9 so với `--parallel` = 4 slots

**Peak `llamacpp:n_busy_slots_per_decode**` (từ `make metrics` khi `make load-50` đang chạy): 3.87 / 4 slots

**Saturation reading** (≤ 80 chữ): Server saturates around 10 users. At 50 users, throughput plateaus (5.34 → 5.92 RPS) while P95 explodes 4.88× to 8,300 ms. The extra latency is 100% queue time (`requests_deferred` hit 43). To increase goodput@SLO (P95 ≤ 2500ms), I would increase `--parallel` from 4 to 8 slots to expand continuous batching slot concurrency.

---

## 4. Integration *(rubric 12, 13 — 15 điểm)*

> Từ `make pipeline`. Nói thật cái nào real, cái nào stub — stub **không** mất điểm.

| Day | Piece | Real hay stub? |
| --- | --- | --- |
| N16 Cloud/IaC | Local setup | stub |
| N17 Data pipeline | In-memory dict | stub |
| N18 Lakehouse | Static memory | stub |
| N19 Vector + features | Keyword matching | stub |
| N20 Serving | `llama-server` | real |

**Latency split** (mean của 3 query, từ output của `pipeline.py`):

* embed: 0.0 ms
* retrieve: 0.0 ms
* llm: 2649.5 ms
* **stage chiếm nhiều nhất:** llm (100% của total)

**Reflection** (≤ 60 chữ): LLM generation is the 100% bottleneck (2,649 ms vs 0 ms). Keyword retrieval runs instantaneously. To halve pipeline latency, I would target the LLM stage using speculative decoding (draft model/MTP head) or capping max response tokens.

---

## 5. The single change that mattered most *(rubric 11 — 10 điểm)*

> **Phần quan trọng nhất của report.** Không cần bonus track: `make tune` đã cho bạn
> một before/after thật (`benchmarks/01-tuning-tg128.md`). Đổi quantization,
> `LAB_N_CTX`, hay `--parallel` rồi đo lại cũng được.

**Change:** Offloading 100% of model layers to CUDA GPU (`ngl=99`) vs CPU execution (`ngl=0`).

```
before:  48.2 tok/s
after:   252.3 tok/s
speedup: 5.23×

```

**Tại sao nó work** (1–2 đoạn — đây là phần grader đọc kỹ nhất):

Autoregressive LLM token decoding is fundamentally memory-bandwidth bound. On CPU execution (`ngl=0`), the system relies on system DDR5 RAM channels (~60-80 GB/s bandwidth across dual channels), capping generation throughput around ~48 tok/s. Offloading all layers to the NVIDIA GeForce RTX 4060 Ti GPU (`ngl=99`) leverages its GDDR6 VRAM bus (~288 GB/s bandwidth), achieving a 5.23× speedup proportional to the hardware memory bandwidth multiplier.

Additionally, host CPU thread sweep (`-t`) produces a flat performance curve when `ngl=99` (291.7 tok/s at -t 1 vs 293.3 tok/s at -t 56) because GPU tensor cores perform all matrix multiplications during decode. CPU threads are only responsible for kernel launching, prompt tokenization, and output sampling.

---

## 6. Bonus *(optional — tối đa 20 điểm)*

> Bỏ trống nếu không làm. Xem `bonus/README.md`. Đừng làm hết — **một** finding sâu
> ăn điểm hơn năm bảng nông.

**Đã làm:** B2 (GPU offload sweep `-ngl 0..99`), B5 (C8 Semantic Cache & C9 Embedding Serving Regimes)

**Numbers:**

```
before:  53.6 tok/s (CPU-only, -ngl 0)
after:   284.0 tok/s (Full GPU offload, -ngl 99)
speedup: 5.30×

```

**Điều này nói lên gì mà deck chưa nói:**

While course materials emphasize datacenter multi-GPU tensor parallelism and FP8/INT4 quantization ladders, local laptop inference bottlenecks center directly on host-to-device PCIe bandwidth vs VRAM memory bus limits. Partial offload (`-ngl 16`) yields only 130.6 tok/s due to inter-layer PCIe ping-pong overhead between system RAM and GPU VRAM. Only upon full offload (`-ngl 99`) does generation throughput hit the full 284.0 tok/s GDDR6 bandwidth ceiling (5.30× speedup).

Furthermore, evaluating C8/C9 serving regimes demonstrates that embedding serving is strictly prefill-bound (no KV cache, single forward pass) compared to decode-bound chat serving, and using chat decoders as sentence embedders introduces severe false-hit risks unless dedicated embedding models (e.g. BGE-M3 or Qwen3-Embedding) are deployed.

---

## 7. Điều làm bạn ngạc nhiên nhất *(optional)*

*(1–2 câu. Không bắt buộc, nhưng grader đọc hết.)*

---

## 8. Self-check trước khi push

* [x] `hardware.json` committed
* [x] `models/active.json` committed
* [x] `benchmarks/01-quickstart-results.md` committed (`make bench`)
* [x] `benchmarks/01-tuning-tg128.md` committed (`make tune`)
* [x] `benchmarks/02-server-results.md` committed (`make load-report`)
* [x] `benchmarks/02-server-batching-u50.md` hoặc `-metrics-u50.csv` committed (`make metrics`)
* [x] `benchmarks/locust-10_stats.csv` + `locust-50_stats.csv` committed (`make load-10` / `load-50`)
* [x] `benchmarks/03-integration-results.md` committed (`make pipeline`)
* [x] Mọi section **"required — replace this line"** trong các file `benchmarks/*.md`
đã được thay bằng nhận xét của bạn
* [x] 5 screenshots trong `submission/screenshots/`
* [x] `make verify` → **exit 0**
* [x] Repo GitHub ở chế độ **public**
* [x] Đã paste public URL vào VinUni LMS
* [x] **Không** commit `models/*.gguf` hay `runtime/` (đã có trong `.gitignore`)

**Quan trọng:** repo phải **public** đến khi điểm được công bố. Private → grader không
xem được → 0 điểm.