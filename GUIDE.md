# GUIDE â LÃ m lab Day 20 tá»« Äáº§u Äáº¿n cuá»i

LÃ m láº§n lÆ°á»£t theo hÆ°á»ng dáº«n nÃ y. Má»i bÆ°á»c cho biáº¿t **lá»nh cáº§n cháº¡y**, **káº¿t quáº£ báº¡n sáº½
tháº¥y** vÃ  **file ÄÆ°á»£c sinh ra**. CÃ¡c file ÄÃ³ lÃ  báº±ng chá»©ng Äá» cháº¥m Äiá»m.

**Tá»ng thá»i gian:** ~2.5 giá» cho base track Â· +1â2 giá» náº¿u lÃ m bonus.

> ### ðª Windows: Äá»c pháº§n nÃ y trÆ°á»c
> Windows khÃ´ng cÃ³ `make`. Khi hÆ°á»ng dáº«n ghi `make <target>`, hÃ£y dÃ¹ng
> **`.\lab.ps1 <target>`** vá»i cÃ¹ng tÃªn target.
>
> ```powershell
> powershell -ExecutionPolicy Bypass -File labs/00-setup/bootstrap.ps1   # chá» cháº¡y 1 láº§n
> .\lab.ps1                 # xem toÃ n bá» target
> .\lab.ps1 bench           # tÆ°Æ¡ng ÄÆ°Æ¡ng make bench
> ```

> ### ð Vá» cÃ¡c lá»nh `python` trong tÃ i liá»u
> Lab **khÃ´ng** dÃ¹ng `python` toÃ n cá»¥c â má»i thá»© cháº¡y trong virtualenv mÃ  `make setup`
> táº¡o ra. VÃ¬ váº­y tÃ i liá»u luÃ´n ghi ÄÆ°á»ng dáº«n Äáº§y Äá»§:
>
> | OS | DÃ¹ng |
> |---|---|
> | macOS / Linux | `.venv/bin/python labs/...` |
> | Windows | `.venv\Scripts\python labs\...` |
>
> TrÃªn macOS/Linux, gÃµ `python` tráº§n thÆ°á»ng bÃ¡o `command not found` (chá» cÃ³ `python3`),
> vÃ  ká» cáº£ `python3` cÅ©ng thiáº¿u package cá»§a lab. LuÃ´n dÃ¹ng `.venv/bin/python`.

```
PHASE 0  Setup                 ~20 phÃºt
PHASE 1  Base track (100 Äiá»m)  ~2 giá»      â báº¯t buá»c
PHASE 2  Bonus track (20 Äiá»m)  ~1-2 giá»    â optional, chá» lÃ m SAU khi xong base
PHASE 3  Submit                 ~5 phÃºt
```

> **Quy táº¯c quan trá»ng:** má»i file `benchmarks/*.md` do lab sinh ra Äá»u cÃ³ section
> **"required -- replace this line"**. Báº¡n **pháº£i** thay section ÄÃ³ báº±ng nháº­n xÃ©t cá»§a
> mÃ¬nh. Náº¿u cÃ²n sÃ³t, `make verify` sáº½ fail. Sá» liá»u chá» lÃ  Äáº§u vÃ o; pháº§n nháº­n xÃ©t má»i lÃ 
> ná»i dung ÄÆ°á»£c cháº¥m.

---

# PHASE 0 â Setup

## BÆ°á»c 0.1 â Kiá»m tra mÃ¡y

```bash
make probe
```

Báº¡n sáº½ tháº¥y thÃ´ng tin vá» CPU, sá» core, RAM, accelerator vÃ  model dÃ¹ng trong lab.

**Chá»n cÃ¡ch cháº¡y ngay á» bÆ°á»c nÃ y:**

| RAM | CÃ¡ch lÃ m |
|---|---|
| **â¥ 8 GB** | Tiáº¿p tá»¥c bÆ°á»c 0.2 vÃ  0.3 trÃªn laptop |
| **4â8 GB** | Váº«n cháº¡y local, chá» Äá»i model: `LAB_MODEL=qwen35-0.8b make setup` (xem bÆ°á»c 0.2). **KhÃ´ng máº¥t Äiá»m.** |
| **< 4 GB** | Má» [`cloud/README.md`](cloud/README.md) vÃ  lÃ m trÃªn Colab/Kaggle. **KhÃ´ng máº¥t Äiá»m.** |

â Sinh ra: **`hardware.json`** *(rubric 1)*

â **Chá»¥p screenshot ngay:** `submission/screenshots/01-hardware-probe.png`

## BÆ°á»c 0.2 â Chá»n model

Lab cÃ³ **hai** option. Cáº£ hai Apache-2.0, **khÃ´ng gated** (khÃ´ng token, khÃ´ng accept license).
Chá»n má»t, lÃ m háº¿t lab vá»i nÃ³.

| | **Gemma 4 E2B** *(máº·c Äá»nh)* | **Qwen3.5 0.8B** *(nhá», nhanh)* |
|---|---|---|
| Repo | [unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) | [unsloth/Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) |
| Táº£i vá» | ~5.2 GB | **~0.9 GB** |
| RAM tá»i thiá»u | 8 GB | **4 GB** |
| Model load | ~6 s | **~3 s** |
| Decode (M1, Metal) | ~27 tok/s | **~42 tok/s** |
| Cháº¥t lÆ°á»£ng cÃ¢u tráº£ lá»i | tá»t hÆ¡n | tháº¥p hÆ¡n (0.8B lÃ  0.8B) |
| Bonus C1 (MTP spec-decode) | cÃ³ MTP head | khÃ´ng cÃ³ |

**Chá»n tháº¿ nÃ o:**

- **RAM â¥ 8 GB, muá»n cÃ¢u tráº£ lá»i tá»­ táº¿** â Gemma 4 E2B. KhÃ´ng cáº§n lÃ m gÃ¬, ÄÃ¢y lÃ  máº·c Äá»nh.
- **RAM 4â8 GB, hoáº·c muá»n cháº¡y nhanh gáº¥p 5 láº§n** â Qwen3.5 0.8B:

  ```bash
  export LAB_MODEL=qwen35-0.8b      # macOS / Linux
  $env:LAB_MODEL = 'qwen35-0.8b'    # Windows PowerShell
  ```

  Set **trÆ°á»c** khi cháº¡y `make setup`. Sau ÄÃ³ `models/active.json` ghi láº¡i lá»±a chá»n, nÃªn
  cÃ¡c bÆ°á»c sau tá»± dÃ¹ng ÄÃºng model â báº¡n khÃ´ng cáº§n export láº¡i má»i láº§n.

**Rubric khÃ´ng quan tÃ¢m báº¡n chá»n model nÃ o.** Cáº£ hai Äá»u cho Äá»§ TTFT/TPOT/percentile,
load test, batching vÃ  tuning story. Model nhá» tháº­m chÃ­ lÃ m pháº§n load test dá» Äá»c hÆ¡n vÃ¬
má»i request xong nhanh hÆ¡n nÃªn báº¡n thu ÄÆ°á»£c nhiá»u máº«u hÆ¡n trong 60 s.

### File sáº½ ÄÆ°á»£c táº£i

| Vai trÃ² | Gemma 4 E2B | Qwen3.5 0.8B |
|---|---|---|
| primary | `gemma-4-E2B-it-UD-Q4_K_XL.gguf` (2.97 GB) [táº£i](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q4_K_XL.gguf) | `Qwen3.5-0.8B-Q4_K_M.gguf` (0.50 GB) [táº£i](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_K_M.gguf) |
| compare | `gemma-4-E2B-it-UD-Q2_K_XL.gguf` (2.24 GB) [táº£i](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q2_K_XL.gguf) | `Qwen3.5-0.8B-UD-Q2_K_XL.gguf` (0.39 GB) [táº£i](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-UD-Q2_K_XL.gguf) |
| bonus C1 | `mtp-gemma-4-E2B-it.gguf` (0.09 GB) [táº£i](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/mtp-gemma-4-E2B-it.gguf) | â |

**BÆ°á»c 0.3 (`make setup`) tá»± táº£i hai file Äáº§u.** Báº£ng trÃªn Äá» báº¡n biáº¿t mÃ¬nh Äang táº£i gÃ¬, vÃ 
Äá» dÃ¹ng khi máº¡ng trÆ°á»ng cháº·n Hugging Face. Náº¿u táº£i tá»± Äá»ng fail, script in ra ÄÃºng lá»nh
`curl` cáº§n cháº¡y â chi tiáº¿t trong
[`labs/00-setup/MANUAL-DOWNLOAD.md`](labs/00-setup/MANUAL-DOWNLOAD.md).

---

## BÆ°á»c 0.3 â CÃ i Äáº·t

```bash
make setup
```

BÆ°á»c nÃ y máº¥t khoáº£ng 5â15 phÃºt vÃ  thá»±c hiá»n ba viá»c:

- Táº¡o `.venv` vÃ  cÃ i 4 package Python.
- Táº£i **llama.cpp prebuilt binary** (10â35 MB, **khÃ´ng compile**).
- Táº£i **Gemma 4 E2B** vá»i 2 quantization (~5.2 GB).

TrÃªn Windows, báº¡n cÃ³ thá» cháº¡y target tÆ°Æ¡ng á»©ng:

```powershell
.\lab.ps1 setup
```

Hoáº·c cháº¡y bootstrap trá»±c tiáº¿p:

```powershell
pwsh -ExecutionPolicy Bypass -File labs/00-setup/bootstrap.ps1
```

â Sinh ra: **`models/active.json`** *(rubric 2)*, `runtime/`, `models/*.gguf`

Náº¿u táº£i model fail do máº¡ng trÆ°á»ng cháº·n Hugging Face, xem
[`labs/00-setup/MANUAL-DOWNLOAD.md`](labs/00-setup/MANUAL-DOWNLOAD.md).

---

# PHASE 1 â Base track (100 Äiá»m)

## BÆ°á»c 1.1 â Äo baseline: TTFT / TPOT / percentiles

> ð Äá»c [`labs/01-measure/README.md`](labs/01-measure/README.md) trÆ°á»c: vÃ¬ sao TPOT bá»
> cháº·n bá»i **memory bandwidth** chá»© khÃ´ng pháº£i FLOPs, vÃ  vÃ¬ sao cháº¡y benchmark cáº¡nh 40
> tab Chrome lÃ  Äang Äo Chrome. REFLECTION Â§2 vÃ  Â§5 cháº¥m ÄÃºng pháº§n láº­p luáº­n nÃ y.

```bash
make bench
```

Script tá»± báº­t `llama-server`, gá»­i 10 prompt qua HTTP streaming, táº¯t server, rá»i láº·p láº¡i
vá»i quantization thá»© hai. BÆ°á»c nÃ y máº¥t vÃ i phÃºt.

Báº¡n sáº½ tháº¥y báº£ng tÆ°Æ¡ng tá»± (vÃ­ dá»¥: Gemma 4 E2B trÃªn M1):

```
| Quantization | Size (GB) | TTFT P50/P95 | TPOT P50/P95 | Decode (tok/s) |
| UD-Q4_K_XL   | 2.97      | 194 / 203    | 37.0 / 40.7  | 27.0           |
| UD-Q2_K_XL   | 2.24      | 202 / 479    | 33.9 / 34.9  | 29.5           |
```

Vá»i Qwen3.5 0.8B trÃªn cÃ¹ng mÃ¡y, con sá» nhanh hÆ¡n rÃµ rá»t (~42 vÃ  ~50 tok/s). **Äá»«ng so sá»
cá»§a báº¡n vá»i hai báº£ng nÃ y** â chÃºng chá» Äá» báº¡n biáº¿t output trÃ´ng ra sao.

â Sinh ra: **`benchmarks/01-quickstart-results.md`** *(rubric 3, 4, 5)*

â **Chá»¥p screenshot:** `02-bench.png`

**Báº¡n cáº§n lÃ m:** má» file trÃªn vÃ  thay section *"Your observation"*. NÃªu rÃµ 2-bit nhanh
hÆ¡n bao nhiÃªu, nhá» hÆ¡n bao nhiÃªu vÃ  **cÃ³ ÄÃ¡ng dÃ¹ng khÃ´ng**.

Äá» ÄÃ¡nh giÃ¡ pháº§n "cÃ³ ÄÃ¡ng dÃ¹ng khÃ´ng", hÃ£y thá»­ cháº¥t lÆ°á»£ng cá»§a cáº£ hai quantization:

```bash
make serve                                      # terminal 1: báº£n 4-bit
.venv/bin/python labs/02-serve/serve.py --compare         # hoáº·c báº£n 2-bit
```

Äáº·t cÃ¹ng má»t cÃ¢u há»i cho cáº£ hai, Äá»c káº¿t quáº£ rá»i ÄÆ°a ra káº¿t luáº­n.

> â ï¸ Cáº£ hai server máº·c Äá»nh dÃ¹ng port **8080**. Báº¡n **pháº£i táº¯t** server thá»© nháº¥t báº±ng
> Ctrl-C trÆ°á»c khi báº­t báº£n `--compare`. CÃ¡ch khÃ¡c lÃ  dÃ¹ng port riÃªng:
> `.venv/bin/python labs/02-serve/serve.py --compare --port 8090`.

## BÆ°á»c 1.2 â Tune thread count cho mÃ¡y cá»§a báº¡n

```bash
make tune
```

Káº¿t quáº£ nÃ y lÃ  nguá»n cho **REFLECTION Â§5**: má»t before/after tháº­t, khÃ´ng cáº§n compiler
hay GPU. BÆ°á»c nÃ y máº¥t vÃ i phÃºt.

```
| threads (-t) | tg128 (tok/s) | vs best |
| 1            | 27.7          | 96%     |
| 4            | 28.9          | 100%    |   â best
| 8            | 27.4          | 95%     |
| 16           | 24.2          | 84%     |   â oversubscribe, cháº­m hÆ¡n
```

â Sinh ra: **`benchmarks/01-tuning-tg128.md`** *(nguá»n cho rubric 11)*

â Screenshot optional: `06-tune.png`

**Báº¡n cáº§n lÃ m:** xÃ¡c Äá»nh **knee** vÃ  giáº£i thÃ­ch nguyÃªn nhÃ¢n. Náº¿u curve khÃ´ng peak á»
physical core count nhÆ° ká»³ vá»ng, hÃ£y nÃ³i rÃµ. ÄÃ¢y lÃ  dá»¯ liá»u ÄÃ¡ng phÃ¢n tÃ­ch, khÃ´ng pháº£i
lá»i cáº§n che Äi.

## BÆ°á»c 1.3 â Dá»±ng server vÃ  chá»©ng minh server hoáº¡t Äá»ng

> ð Äá»c [`labs/02-serve/README.md`](labs/02-serve/README.md) trÆ°á»c: continuous batching,
> cÃ¡ch Äá»c queue time vs compute time báº±ng Little's Law, vÃ  thÃ­ nghiá»m ÄÃ¡ng giÃ¡ nháº¥t cá»§a
> lab (`--parallel 1` so vá»i `--parallel 4`). REFLECTION Â§3 cháº¥m pháº§n nÃ y.

Báº¡n cáº§n **2 terminal**.

**Terminal 1** â giá»¯ server cháº¡y:

```bash
make serve
```

**Terminal 2:**

```bash
make smoke
```

`make smoke` chá»©ng minh hai viá»c trong má»t láº§n cháº¡y: server tráº£ vá» má»t completion tháº­t,
vÃ  `/metrics` cÃ³ `llamacpp:tokens_predicted_total` khÃ¡c 0.

â *(rubric 6, 7)*

â **Chá»¥p screenshot:** `03-serve-and-smoke.png`. áº¢nh pháº£i cÃ³ **cáº£** server Äang listen
vÃ  output cá»§a `make smoke`. Báº¡n cÃ³ thá» chia ÄÃ´i terminal hoáº·c chá»¥p hai file `03a-` /
`03b-`.

## BÆ°á»c 1.4 â Load test

Giá»¯ server cháº¡y á» terminal 1. Táº¡i terminal 2:

```bash
make load-10       # 10 users, 60s
```

â **Chá»¥p screenshot:** `04-locust-10.png`. áº¢nh pháº£i tháº¥y dÃ²ng cÃ³
`# reqs Â· Median Â· 95%ile Â· 99%ile`.

Tiáº¿p theo lÃ  50 users. BÆ°á»c nÃ y cáº§n **3 terminal**:

```bash
# terminal 2:
make load-50

# terminal 3, CHáº Y NGAY KHI load-50 Äang cháº¡y:
make metrics
```

> â ï¸ **Lá»i phá» biáº¿n nháº¥t cá»§a lab:** cháº¡y `make metrics` khi server Äang ráº£nh. Khi ÄÃ³,
> `n_busy_slots_per_decode` sáº½ â 1 vÃ  khÃ´ng chá»©ng minh ÄÆ°á»£c continuous batching.
> `make metrics` **pháº£i cháº¡y chá»ng thá»i gian vá»i `make load-50`**.

â **Chá»¥p screenshot:** `05-locust-50.png`

â Sinh ra: **`benchmarks/02-server-batching-u50.md`** + `.csv` *(rubric 9)*

Báº¡n sáº½ tháº¥y má»t dÃ²ng tÆ°Æ¡ng tá»±:
`Peak n_busy_slots_per_decode = 3.79 of 4 slots`. ÄÃ¢y lÃ  báº±ng chá»©ng continuous batching
Äang hoáº¡t Äá»ng.

## BÆ°á»c 1.5 â XÃ¡c Äá»nh Äiá»m saturation cá»§a server

```bash
make load-report
```

Script Äá»c hai load test phÃ­a trÃªn. NÃ³ dÃ¹ng Little's Law
(`RPS Ã average latency`) Äá» tÃ­nh **effective concurrency**, rá»i so vá»i sá» slot cá»§a
`--parallel`.

â Sinh ra: **`benchmarks/02-server-results.md`** *(rubric 10)*

**Báº¡n cáº§n lÃ m:** tráº£ lá»i server saturation á» ÄÃ¢u vÃ  báº±ng chá»©ng lÃ  gÃ¬. Náº¿u throughput
tÄng Ã­t nhÆ°ng P95 tÄng máº¡nh, pháº§n latency tÄng thÃªm lÃ  **queue time**, khÃ´ng pháº£i
compute. ÄÃ¢y lÃ  láº­p luáº­n goodput@SLO trong deck Â§8.

## BÆ°á»c 1.6 â Cháº¡y RAG pipeline

> ð Äá»c [`labs/03-integrate/README.md`](labs/03-integrate/README.md) trÆ°á»c: vÃ¬ sao
> prefill lÃ  pháº§n RAG thá»i phá»ng, vÃ  prompt caching thay Äá»i sá» Äo tháº¿ nÃ o.

Giá»¯ server cháº¡y. Táº¡i terminal 2:

```bash
make pipeline
```

Báº¡n sáº½ tháº¥y 3 query, context ÄÆ°á»£c retrieve vÃ  latency theo tá»«ng stage:

```
timings : {'embed': 0.0, 'retrieve': 0.3, 'llm': 1875.2, 'total': 1875.5}
Dominant stage: llm (100% of total)
```

â Sinh ra: **`benchmarks/03-integration-results.md`** *(rubric 12, 13)* â file nÃ y cÃ³ má»t
section **"required -- replace this line"** báº¡n pháº£i thay. Screenshot optional: `08-pipeline.png`

**Báº¡n cáº§n lÃ m:** trong REFLECTION Â§4, khai bÃ¡o rÃµ stage nÃ o **real**, stage nÃ o **stub**.
DÃ¹ng stub khÃ´ng máº¥t Äiá»m; khai bÃ¡o sai má»i máº¥t Äiá»m. Náº¿u cÃ³ code N19, thay hai chá»
`STUB` trong `labs/03-integrate/pipeline.py`.

## BÆ°á»c 1.7 â Viáº¿t REFLECTION.md

Má» [`submission/REFLECTION.md`](submission/REFLECTION.md) vÃ  Äiá»n Äá»§ má»i section. ÄÃ¢y
lÃ  file grader Äá»c ká»¹ nháº¥t.

Pháº§n quan trá»ng nháº¥t lÃ  **Â§5 "The single change that mattered most"** (10 Äiá»m). DÃ¹ng
káº¿t quáº£ `make tune` á» bÆ°á»c 1.2 vÃ  giáº£i thÃ­ch **cÆ¡ cháº¿**: memory bandwidth, cache hay
scheduling. KhÃ´ng chá» nÃªu cáº£m nháº­n hoáº·c chÃ©p láº¡i con sá».

## BÆ°á»c 1.8 â Kiá»m tra base track

```bash
make verify
```

Lá»nh nÃ y pháº£i **exit 0**. Náº¿u fail, output sáº½ liá»t kÃª file cÃ²n thiáº¿u vÃ  lá»nh cáº§n cháº¡y.

**Base track hoÃ n táº¥t táº¡i ÄÃ¢y. Báº¡n ÄÃ£ cÃ³ Äá»§ báº±ng chá»©ng cho 100 Äiá»m base.**

---

# PHASE 2 â Bonus track (20 Äiá»m, optional)

> **Chá» báº¯t Äáº§u khi PHASE 1 ÄÃ£ hoÃ n táº¥t vÃ  `make verify` ÄÃ£ exit 0.** Bonus khÃ´ng bÃ¹
> ÄÆ°á»£c pháº§n base cÃ²n thiáº¿u.

Chi tiáº¿t: [`bonus/README.md`](bonus/README.md) Â·
[`bonus/CHALLENGES.md`](bonus/CHALLENGES.md)

Chá»n **1â2 má»¥c**, khÃ´ng cáº§n lÃ m háº¿t. CÃ³ 5 tiÃªu chÃ­, má»i tiÃªu chÃ­ 4 Äiá»m:

| | Lá»nh | Ghi chÃº |
|---|---|---|
| **B1** | `make build-llama && make compare-builds` | Compile cho CPU cá»§a báº¡n rá»i so vá»i prebuilt binary. **MÃ¡y yáº¿u thÆ°á»ng cÃ³ má»©c cáº£i thiá»n rÃµ nháº¥t á» ÄÃ¢y.** Cáº§n `cmake`. |
| **B2** | `make sweep-quant` / `sweep-ctx` / `sweep-batch` / `sweep-gpu` | Chá»n 1 sweep phÃ¹ há»£p vá»i bottleneck cá»§a báº¡n |
| **B3** | â | Ghi before/after cá»§a B1 hoáº·c B2 vÃ o REFLECTION Â§6 |
| **B4** | â | Chá»n 1 challenge C1âC7 trong `bonus/CHALLENGES.md` |
| **B5** | `make mlx-compare` (Mac) **hoáº·c** `make semantic-cache` (C8) **hoáº·c** `make serve-embed && make embed-demo` (C9) **hoáº·c** C6 | 4 lá»±a chá»n; ná»n táº£ng nÃ o cÅ©ng cÃ³ lá»±a chá»n phÃ¹ há»£p |

Gá»£i Ã½ theo mÃ¡y vÃ  má»¥c tiÃªu:

- **CPU-only** â B1 (`compare-builds`). ÄÃ¢y thÆ°á»ng lÃ  speedup lá»n nháº¥t trong lab.
- **RAM háº¡n cháº¿** â `make sweep-quant`.
- **CÃ³ GPU** â `make sweep-gpu`.
- **Quan tÃ¢m RAG long-context** â `make sweep-ctx`.
- **KhÃ´ng muá»n táº£i thÃªm** â C8 hoáº·c C9, cÃ³ thá» cháº¡y vá»i `--offline`.

Má»i bonus script cÅ©ng sinh file `benchmarks/bonus-*.md` cÃ³ section
*"required -- replace this line"*. Báº¡n váº«n pháº£i Äiá»n section nÃ y.

---

# PHASE 3 â Submit

1. Cháº¡y `make verify` láº§n cuá»i. Káº¿t quáº£ pháº£i **exit 0**.
2. Fork/copy repo lÃªn GitHub account cá»§a báº¡n vÃ  set **public**.
3. Commit vÃ  push:

   ```bash
   git add -A && git commit -m "Day 20 lab submission" && git push
   ```

4. Paste public URL vÃ o Ã´ submission Day 20 trÃªn VinUni LMS.

**Repo pháº£i public cho Äáº¿n khi Äiá»m ÄÆ°á»£c cÃ´ng bá».** Náº¿u repo private, grader khÃ´ng thá»
Äá»c bÃ i vÃ  báº¡n nháº­n **0 Äiá»m**.

KhÃ´ng commit `models/*.gguf` hoáº·c `runtime/`. Hai path nÃ y ÄÃ£ cÃ³ trong `.gitignore`, vÃ 
`make verify` khÃ´ng yÃªu cáº§u chÃºng.

---

# Troubleshooting

| Triá»u chá»©ng | CÃ¡ch xá»­ lÃ½ |
|---|---|
| `unknown model architecture: 'gemma4'` | llama.cpp quÃ¡ cÅ©. Cháº¡y `make runtime` Äá» táº£i láº¡i báº£n ÄÃ£ pin. |
| `make probe` bÃ¡o `GPU offload : OFF` dÃ¹ mÃ¡y cÃ³ GPU | BÃ¬nh thÆ°á»ng, vÃ  **khÃ´ng máº¥t Äiá»m** â toÃ n bá» 100 Äiá»m base cháº¡y trÃªn CPU. Upstream llama.cpp **khÃ´ng** phÃ¡t hÃ nh báº£n CUDA cho Linux, nÃªn mÃ¡y Linux + NVIDIA nháº­n báº£n Vulkan; thiáº¿u Vulkan ICD thÃ¬ runtime khÃ´ng tháº¥y device nÃ o. Lab tá»± set `ngl=0` Äá» report khÃ´ng ghi sai. Muá»n dÃ¹ng GPU: `LLAMA_CMAKE_FLAGS=-DGGML_CUDA=ON make build-llama` (bonus B1). |
| `make serve` bÃ¡o khÃ´ng tÃ¬m tháº¥y venv | Báº¡n chÆ°a cháº¡y `make setup`. |
| `couldn't bind HTTP server socket â¦ port: 8080` | CÃ³ process khÃ¡c Äang giá»¯ port 8080. Äá»i port: `LAB_SERVER_PORT=8090 make serve` (vÃ  dÃ¹ng cÃ¹ng biáº¿n ÄÃ³ cho `make smoke`, `make load-10/50`, `make metrics`, `make pipeline`). TrÃªn Colab notebook ÄÃ£ set sáºµn. |
| `make bench` fail, cÃ¢u tráº£ lá»i rá»ng | Gemma 4 lÃ  reasoning model; lab ÄÃ£ set `--reasoning off`. Náº¿u báº¡n tá»± báº­t `LAB_REASONING=on`, `content` sáº½ rá»ng cho Äáº¿n khi model "nghÄ©" xong. |
| `make metrics` bÃ¡o scrape failed | Server chÆ°a cháº¡y. Cháº¡y `make serve` trÆ°á»c. |
| `busy_slots â 1` dÃ¹ ÄÃ£ cháº¡y metrics | Báº¡n cháº¡y `make metrics` khi khÃ´ng cÃ³ load. Pháº£i cháº¡y chá»ng vá»i `make load-50`. |
| locust chá» hoÃ n thÃ nh vÃ i request | BÃ¬nh thÆ°á»ng trÃªn mÃ¡y yáº¿u. Muá»n thÃªm máº«u, dÃ¹ng `-t 3m` hoáº·c giáº£m `LAB_LOAD_SHORT_TOKENS`. |
| Hugging Face bá» cháº·n | Xem [`labs/00-setup/MANUAL-DOWNLOAD.md`](labs/00-setup/MANUAL-DOWNLOAD.md). |
| MÃ¡y < 8 GB RAM | DÃ¹ng [`cloud/README.md`](cloud/README.md). |
| `make verify` fail mÃ  chÆ°a rÃµ lÃ½ do | Output ghi ÄÃºng file cÃ²n thiáº¿u vÃ  lá»nh cáº§n cháº¡y. Äá»c tá»«ng dÃ²ng lá»i. |
| Sau checklist cÃ³ dÃ²ng `make: *** [verify] Error 1` | BÃ¬nh thÆ°á»ng. ÄÃ³ chá» lÃ  cÃ¡ch `make` bÃ¡o ráº±ng `verify` tÃ¬m tháº¥y má»¥c cÃ²n thiáº¿u â khÃ´ng pháº£i `make` bá» lá»i. Äá»c checklist á» trÃªn nÃ³. |

## CÃ¡c knob cÃ³ thá» Äá»i

KhÃ´ng cáº§n táº¡o file `.env`. Set inline:

```bash
LAB_N_THREADS=4 make bench       # dÃ¹ng thread count tá»t nháº¥t tá»« make tune
LAB_N_CTX=4096 make serve        # context lá»n hÆ¡n (tá»n RAM hÆ¡n)
LAB_PARALLEL=8 make serve        # nhiá»u slot hÆ¡n
LAB_REASONING=on make bench      # báº­t thinking Äá» Äo chi phÃ­
```

Danh sÃ¡ch Äáº§y Äá»§: [`.env.example`](.env.example)
