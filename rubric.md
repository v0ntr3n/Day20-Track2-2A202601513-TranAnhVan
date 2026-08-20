# Rubric â Day 20 Lab (100 Äiá»m base + 20 bonus)

Track-2 Daily Lab, trá»ng sá» **30%**.

> **ÄÃ¢y lÃ  bÃ¡o cÃ¡o cÃ¡ nhÃ¢n.** Má»i báº¡n cháº¡y trÃªn mÃ¡y mÃ¬nh. Sá» liá»u cá»§a báº¡n **khÃ´ng** so
> sÃ¡nh ÄÆ°á»£c vá»i báº¡n cÃ¹ng lá»p â chá» so **before vs after trÃªn chÃ­nh mÃ¡y báº¡n**. Rubric cháº¥m
> **Äá» rÃµ rÃ ng cá»§a setup + Äo lÆ°á»ng + láº­p luáº­n**, khÃ´ng cháº¥m tá»c Äá» tuyá»t Äá»i.
> Air M1 8 GB vÃ  RTX 5090 Äá»u cÃ³ thá» Äáº¡t 100/100.
>
> **ToÃ n bá» 100 Äiá»m base khÃ´ng cáº§n GPU, khÃ´ng cáº§n compiler, khÃ´ng cáº§n Docker.**

Grader cháº¥m **file tháº­t trong repo cá»§a báº¡n**, khÃ´ng cháº¥m nhá»¯ng gÃ¬ báº¡n nÃ³i báº¡n ÄÃ£ lÃ m.

CÃ¡ch lÃ m tá»«ng bÆ°á»c: **[GUIDE.md](GUIDE.md)**

---

## Base track â 100 Äiá»m

### Pháº§n A Â· Setup (10 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | Lá»nh sinh ra báº±ng chá»©ng | Äiá»m |
|--:|---|---|--:|
| 1 | `hardware.json` cÃ³ trong repo. Náº¿u báº¡n cháº¡y trÃªn Colab/Kaggle thÃ¬ khai bÃ¡o á» REFLECTION Â§1 | `make probe` | 5 |
| 2 | `models/active.json` cÃ³ trong repo vÃ  há»£p lá» | `make setup` | 5 |

### Pháº§n B Â· Äo lÆ°á»ng (20 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | Lá»nh | Äiá»m |
|--:|---|---|--:|
| 3 | CÃ³ báº£ng latency cho **cáº£ hai** quantization, Äá»§ percentile | `make bench` | 10 |
| 4 | **TTFT vÃ  TPOT bÃ¡o riÃªng**, khÃ´ng gá»p thÃ nh end-to-end | `make bench` | 5 |
| 5 | CÃ³ nháº­n xÃ©t cá»§a báº¡n vá» 2-bit vs 4-bit â nhanh hÆ¡n bao nhiÃªu, **vÃ  cÃ³ ÄÃ¡ng khÃ´ng** | báº¡n viáº¿t vÃ o `benchmarks/01-quickstart-results.md` | 5 |

### Pháº§n C Â· Serving (25 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | Lá»nh | Äiá»m |
|--:|---|---|--:|
| 6 | `llama-server` phá»¥c vá»¥ ÄÆ°á»£c `/v1/chat/completions` | `make serve` + `make smoke` | 10 |
| 7 | `/metrics` cÃ³ `llamacpp:tokens_predicted_total` **khÃ¡c 0** sau request | `make smoke` (in ra sáºµn) | 5 |
| 8 | Load test á» **cáº£** 10 vÃ  50 users, 60s má»i láº§n | `make load-10` Â· `make load-50` | 5 |
| 9 | **Continuous batching quan sÃ¡t ÄÆ°á»£c** â peak `n_busy_slots_per_decode` dÆ°á»i load | `make metrics` **khi** `make load-50` Äang cháº¡y | 5 |

### Pháº§n D Â· PhÃ¢n tÃ­ch (20 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | á» ÄÃ¢u | Äiá»m |
|--:|---|---|--:|
| 10 | **Saturation reading** â server bÃ£o hoÃ  á» ÄÃ¢u, báº±ng chá»©ng nÃ o. RPS cÃ³ plateau? P95 phá»ng lÃªn bao nhiÃªu? Effective concurrency so vá»i sá» slot? | `make load-report` â báº¡n viáº¿t vÃ o `benchmarks/02-server-results.md` | 10 |
| 11 | **"Thay Äá»i quan trá»ng nháº¥t"** â before/after tháº­t + giáº£i thÃ­ch **cÆ¡ cháº¿** | REFLECTION Â§5 | 10 |

### Pháº§n E Â· Integration (15 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | á» ÄÃ¢u | Äiá»m |
|--:|---|---|--:|
| 12 | `pipeline.py` cháº¡y háº¿t 3 query vÃ  in ra context ÄÃ£ retrieve | `make pipeline` | 10 |
| 13 | Khai bÃ¡o **cÃ¡i nÃ o real / cÃ¡i nÃ o stub** trong N16âN19, **vÃ ** latency chia theo stage (embed / retrieve / llm) | REFLECTION Â§4 | 5 |

### Pháº§n F Â· Submission (10 Äiá»m)

| # | ÄÆ°á»£c Äiá»m khi | á» ÄÃ¢u | Äiá»m |
|--:|---|---|--:|
| 14 | REFLECTION.md Äiá»n Äáº§y Äá»§ Â· `make verify` **exit 0** Â· 5 screenshots | `make verify` | 10 |

**Tá»ng base: 100 Äiá»m**

---

## Äiá»m 11 â pháº§n náº·ng nháº¥t, vÃ  cÃ¡ch láº¥y nÃ³ mÃ  **khÃ´ng** cáº§n bonus

`make tune` sweep thread count báº±ng `llama-bench` â **khÃ´ng compiler, khÃ´ng GPU** â rá»i
ghi ra `benchmarks/01-tuning-tg128.md` kÃ¨m before/after vÃ  tá» lá» speedup. File ÄÃ³ lÃ  Äá»§
cho Äiá»m 11.

Äá»i quantization, `LAB_N_CTX`, hoáº·c `--parallel` rá»i Äo láº¡i cÅ©ng ÄÆ°á»£c.

**CÃ¡i ÄÆ°á»£c cháº¥m lÃ  pháº§n giáº£i thÃ­ch, khÃ´ng pháº£i Äá» lá»n con sá».** Má»t speedup 1.06Ã ÄÆ°á»£c
giáº£i thÃ­ch ÄÃºng cÆ¡ cháº¿ Än Äiá»m cao hÆ¡n 3Ã nhÆ°ng chá» ghi "nÃ³ nhanh hÆ¡n".

BÃ¡m vÃ o cÆ¡ cháº¿ cá»¥ thá»: memory bandwidth? vector width? cache residency? queueing?
**Náº¿u káº¿t quáº£ khÃ¡c ká»³ vá»ng tá»« deck â nÃ³i rÃµ vÃ  giáº£i thÃ­ch.** ÄÃ³ lÃ  chá» Än Äiá»m, khÃ´ng
pháº£i chá» máº¥t Äiá»m.

---

## Bonus track â 20 Äiá»m (optional)

Má»i tiÃªu chÃ­ Äá»u Äáº¡t ÄÆ°á»£c trÃªn **báº¥t ká»³** ná»n táº£ng. B5 cÃ³ 4 lá»±a chá»n nÃªn Apple Silicon
lÃ  *má»t* option, khÃ´ng pháº£i Äiá»u kiá»n.

| # | ÄÆ°á»£c Äiá»m khi | Lá»nh | Äiá»m |
|--:|---|---|--:|
| B1 | Compile llama.cpp cho CPU cá»§a báº¡n vÃ  **so vá»i prebuilt binary** | `make build-llama && make compare-builds` | 4 |
| B2 | Cháº¡y Ã­t nháº¥t 1 sweep | `make sweep-quant` / `sweep-ctx` / `sweep-batch` / `sweep-gpu` | 4 |
| B3 | Speedup **cá»§a bonus track** cÃ³ before/after rÃµ rÃ ng | REFLECTION Â§6 (tá»« B1 hoáº·c B2, **khÃ´ng** pháº£i káº¿t quáº£ `make tune` cá»§a base) | 4 |
| B4 | LÃ m Ã­t nháº¥t 1 challenge C1âC7 hoáº·c C10 | `bonus/CHALLENGES.md` | 4 |
| B5 | Má»t so sÃ¡nh runtime/regime â **chá»n 1**: MLX (Mac) Â· C8 semantic cache Â· C9 embedding serving Â· C6 Vulkan vs CUDA | `make mlx-compare` Â· `make semantic-cache` Â· `make embed-demo` | 4 |

**Tá»ng bonus: 20 Äiá»m**

Bonus **khÃ´ng** lÃ m giáº£m Äiá»m base. Bá» háº³n bonus váº«n á»n. Submission bonus **tá»t** ÄÆ°á»£c
instructor viáº¿t review riÃªng, táº­p trung vÃ o cháº¥t lÆ°á»£ng láº­p luáº­n.

**Äá»«ng lÃ m háº¿t.** *Má»t* finding giáº£i thÃ­ch sÃ¢u > nÄm báº£ng sá» nÃ´ng.

---

## 5 screenshots báº¯t buá»c

Táº¥t cáº£ Äá»u tá»« base track â **khÃ´ng cÃ¡i nÃ o cáº§n bonus, GPU, hay compiler.**
Chi tiáº¿t + tips: [`submission/screenshots/README.md`](submission/screenshots/README.md)

> TÃªn file dÆ°á»i ÄÃ¢y lÃ  **gá»£i Ã½** (giá»¯ sá» thá»© tá»± Äá» sáº¯p ÄÃºng thá»© tá»± cháº¡y); grader map
> chÃºng qua REFLECTION cá»§a báº¡n. `make verify` Äáº¿m Äá»§ 5 áº£nh **ÄÃ£ commit**, khÃ´ng Ã©p tÃªn.

| # | File | Tá»« lá»nh |
|--:|---|---|
| 1 | `01-hardware-probe.png` | `make probe` |
| 2 | `02-bench.png` | `make bench` (báº£ng káº¿t quáº£) |
| 3 | `03-serve-and-smoke.png` | `make serve` + `make smoke` (Äiá»m 6 **vÃ ** 7 trong 1 áº£nh) |
| 4 | `04-locust-10.png` | `make load-10` |
| 5 | `05-locust-50.png` | `make load-50` |

---

## Nhá»¯ng cÃ¡ch máº¥t Äiá»m hay gáº·p

| Máº¥t Äiá»m vÃ¬ | TrÃ¡nh báº±ng cÃ¡ch |
|---|---|
| Repo Äá» **private** â grader khÃ´ng xem ÄÆ°á»£c | Set **public** cho tá»i khi cÃ³ Äiá»m. Private = **0 Äiá»m** |
| `make metrics` cháº¡y khi server ráº£nh â `busy_slots â 1`, khÃ´ng cÃ³ báº±ng chá»©ng batching | Cháº¡y `make metrics` **chá»ng thá»i gian** vá»i `make load-50` (Äiá»m 9) |
| CÃ²n sÃ³t section **"required â replace this line"** trong `benchmarks/*.md` | `make verify` sáº½ fail. Äá»c vÃ  Äiá»n háº¿t |
| REFLECTION cÃ²n placeholder `<Há» TÃªn>`, `_Answer here._` | `make verify` sáº½ fail |
| Â§5 chá» ghi sá», khÃ´ng giáº£i thÃ­ch | NÃ³i rÃµ cÆ¡ cháº¿. ÄÃ¢y lÃ  10 Äiá»m |
| Sá» trong REFLECTION khÃ´ng khá»p `benchmarks/*.md` | Äá»c láº¡i `benchmarks/*.md` rá»i copy ÄÃºng sá» trÆ°á»c khi push |
| Commit `models/*.gguf` (5 GB) | ÄÃ£ cÃ³ trong `.gitignore` â Äá»«ng `git add -f` |
| KhÃ´ng khai bÃ¡o ÄÃ£ dÃ¹ng Colab/Kaggle | Ghi 1 dÃ²ng á» REFLECTION Â§1. Khai bÃ¡o thÃ¬ **khÃ´ng máº¥t Äiá»m**; khÃ´ng khai bÃ¡o thÃ¬ máº¥t |
| NÃ³i pipeline lÃ  "real" khi Äang stub | Stub **khÃ´ng máº¥t Äiá»m**. NÃ³i dá»i má»i máº¥t (Äiá»m 13) |

---

## CÃ¡ch submit

**KHÃNG cáº§n PR â chá» submit GitHub URL cÃ´ng khai vÃ o VinUni LMS.**

1. Fork/copy repo nÃ y lÃªn GitHub account cá»§a báº¡n, set **public**
2. HoÃ n thÃ nh base track (`make verify` exit 0)
3. (Optional) lÃ m bonus
4. Add 5 screenshots vÃ o `submission/screenshots/`
5. Äiá»n `submission/REFLECTION.md`
6. `make verify` â **exit 0**
7. Push, paste public URL vÃ o Ã´ submission Day 20 trÃªn LMS

---

## Grader cháº¡y repo cá»§a báº¡n nhÆ° tháº¿ nÃ o

```bash
git clone https://github.com/<you>/<your-repo>
cd <your-repo>
cat hardware.json models/active.json          # Äiá»m 1, 2
cat benchmarks/01-quickstart-results.md       # Äiá»m 3, 4, 5
cat benchmarks/02-server-results.md           # Äiá»m 10
cat benchmarks/02-server-batching*.md         # Äiá»m 9
ls submission/screenshots/                    # Äiá»m 6, 7, 8
cat submission/REFLECTION.md                  # Äiá»m 11, 12, 13
make verify                                   # Äiá»m 14 â exit 0?
ls benchmarks/bonus-*.md                      # bonus
```

`make verify` chá» kiá»m tra **file ÄÃ£ commit**. Model weights vÃ  runtime binary náº±m trong
`.gitignore` cÃ³ chá»§ ÄÃ­ch, nÃªn viá»c grader khÃ´ng cÃ³ chÃºng **khÃ´ng bao giá»** lÃ  lá»i.

---

## Late policy / regrade

Theo policy chuáº©n cá»§a Track-2 â xem `INDEX-Track2.md` trong repo course material.
