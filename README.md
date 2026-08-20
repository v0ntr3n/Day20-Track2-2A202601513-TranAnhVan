# Day 20 â Model Serving & Inference Optimization (Track 2)

Lab cho **AICB-P2T2 Â· NgÃ y 20**.

Báº¡n dá»±ng má»t inference stack tháº­t trÃªn laptop cá»§a mÃ¬nh, Äo **TTFT / TPOT / P50 / P95 /
P99**, Äáº©y nÃ³ tá»i Äiá»m bÃ£o hoÃ  báº±ng load test, rá»i tune má»t knob vÃ  viáº¿t report vá» thay
Äá»i táº¡o ra speedup lá»n nháº¥t **trÃªn chÃ­nh mÃ¡y báº¡n**.

> ### ð Báº¯t Äáº§u á» ÄÃ¢y: **[GUIDE.md](GUIDE.md)**
> HÆ°á»ng dáº«n tá»«ng bÆ°á»c, cÃ³ lá»nh cá»¥ thá» vÃ  checkpoint. Äá»c [`rubric.md`](rubric.md) trÆ°á»c
> Äá» biáº¿t grader cháº¥m gÃ¬.

---

## Lab nÃ y cháº¡y trÃªn mÃ¡y nÃ o cÅ©ng ÄÆ°á»£c

| | |
|---|---|
| **Model** | Chá»n **má»t** trong hai (cáº£ hai Apache-2.0, khÃ´ng gated): |
| | **Gemma 4 E2B** â [unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) Â· ~5.2 GB Â· cáº§n 8 GB RAM Â· *máº·c Äá»nh* |
| | **Qwen3.5 0.8B** â [unsloth/Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) Â· ~0.9 GB Â· cáº§n 4 GB RAM Â· nhanh hÆ¡n, nháº¹ hÆ¡n |
| **Runtime** | **llama.cpp prebuilt binary** â táº£i 11â33 MB (báº£n Windows CUDA 140â240 MB), **khÃ´ng compile** |
| **Cáº§n** | Python â¥ 3.10 Â· **8 GB RAM** (hoáº·c **4 GB** vá»i Qwen3.5 0.8B) Â· 3â10 GB ÄÄ©a |
| **KhÃ´ng cáº§n** | GPU Â· compiler Â· Docker Â· API key Â· tÃ i khoáº£n tráº£ phÃ­ |
| **OS** | Windows Â· macOS (Intel + Apple Silicon) Â· Linux |
| **Windows** | KhÃ´ng cÃ³ `make` â dÃ¹ng **`.\lab.ps1 <target>`** (tÃªn target giá»ng há»t) |
| **RAM < 8 GB?** | `LAB_MODEL=qwen35-0.8b make setup` â cháº¡y local vá»i model nhá» |
| **RAM < 4 GB?** | DÃ¹ng [`cloud/`](cloud/README.md) â Colab/Kaggle, **Äiá»m khÃ´ng Äá»i** |

> **Sá» liá»u cá»§a báº¡n khÃ´ng so sÃ¡nh ÄÆ°á»£c vá»i báº¡n cÃ¹ng lá»p.** Chá» so **before vs after trÃªn
> chÃ­nh mÃ¡y báº¡n**. Rubric cháº¥m Äá» rÃµ rÃ ng cá»§a setup + Äo lÆ°á»ng + **láº­p luáº­n**, khÃ´ng cháº¥m
> tá»c Äá» tuyá»t Äá»i. Má»t báº¡n dÃ¹ng Air M1 8 GB vÃ  má»t báº¡n dÃ¹ng RTX 5090 Äá»u cÃ³ thá» Äáº¡t
> 100/100. ToÃ n bá» 100 Äiá»m base **khÃ´ng cáº§n GPU, khÃ´ng cáº§n compiler**.

---

## Luá»ng lÃ m lab

LÃ m **theo ÄÃºng thá»© tá»± nÃ y**. Äá»«ng nháº£y vÃ o bonus trÆ°á»c khi base xong.

```
ââ 1 â BASE TRACK ââââââââââââââââââ 100 Äiá»m Â· báº¯t buá»c Â· ~2 giá» ââ
â                                                                  â
â   make probe                 hardware.json                       â
â   make setup                 runtime + Gemma 4 E2B               â
â   make bench                 TTFT / TPOT / percentiles, 2 quant  â
â   make tune                  thread sweep â before/after cá»§a báº¡n â
â   make serve   + make smoke  OpenAI-compat API + /metrics        â
â   make load-10 / load-50     load test                           â
â   make metrics               continuous batching (cháº¡y CÃNG load)â
â   make load-report           server bÃ£o hoÃ  á» ÄÃ¢u                â
â   make pipeline              RAG â llama-server                  â
â   viáº¿t submission/REFLECTION.md                                  â
â   make verify                pháº£i exit 0                         â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
                                 â
                    base xong, verify exit 0
                                 â¼
ââ 2 â BONUS TRACK ââââââââââââ +20 Äiá»m Â· optional Â· ~1-2 giá» âââââ
â                                                                  â
â   B1  make build-llama && make compare-builds                    â
â       compile cho CPU cá»§a báº¡n â so vá»i prebuilt binary           â
â       (mÃ¡y yáº¿u tháº¯ng Äáº­m nháº¥t á» ÄÃ¢y)                             â
â   B2  make sweep-quant / sweep-ctx / sweep-batch / sweep-gpu     â
â   B3  ghi before/after vÃ o REFLECTION Â§6                         â
â   B4  1 challenge trong bonus/CHALLENGES.md (C1âC7)              â
â   B5  make mlx-compare  Â·  make semantic-cache  Â·  make embed-demoâ
â       (4 lá»±a chá»n â má»i ná»n táº£ng Äá»u Äáº¡t ÄÆ°á»£c)                   â
â                                                                  â
â   Chá»n 1-2 cÃ¡i. Má»T insight giáº£i thÃ­ch rÃµ > nÄm báº£ng sá» nÃ´ng.     â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
                                 â
                                 â¼
ââ 3 â SUBMIT ââââââââââââââââââââââââââââââââââââââââ ~5 phÃºt âââââ
â   make verify â exit 0  Â·  repo PUBLIC  Â·  paste URL vÃ o LMS      â
ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
```

Cháº¡y `make` Äá» xem toÃ n bá» target.

---

## VÃ¬ sao lab khÃ´ng dÃ¹ng vLLM / SGLang

Nhá»¯ng engine ÄÃ³ cáº§n CUDA GPU + 16 GB VRAM trá» lÃªn. Äáº¹p trÃªn slide, khÃ´ng cháº¡y ÄÆ°á»£c trÃªn
má»t lá»p 30 laptop há»n há»£p. llama.cpp cho báº¡n **cÃ¹ng teaching surface** â GGUF
quantization, paged KV cache, continuous batching, OpenAI-compat API, Prometheus
`/metrics` â trÃªn báº¥t cá»© pháº§n cá»©ng nÃ o báº¡n Äang cÃ³.

**VÃ  vÃ¬ sao prebuilt binary, khÃ´ng pháº£i `llama-cpp-python`:** Gemma 4 dÃ¹ng architecture
`gemma4` (4/2026). Wheel `llama-cpp-python` trÃªn PyPI vendor má»t báº£n llama.cpp cÅ© hÆ¡n vÃ 
sáº½ bÃ¡o `unknown model architecture: 'gemma4'`. Prebuilt release binary khÃ´ng cÃ³ váº¥n Äá»
ÄÃ³, táº£i nhanh hÆ¡n, **vÃ ** cho báº¡n `/metrics` + `--parallel` + `--cont-batching` ngay tá»«
Äáº§u â nhá»¯ng thá»© báº£n Python khÃ´ng cÃ³.
