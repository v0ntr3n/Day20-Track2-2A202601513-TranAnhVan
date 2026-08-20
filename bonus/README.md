# Pháº§n bonus (+20 Äiá»m, khÃ´ng báº¯t buá»c)

> Chá» báº¯t Äáº§u khi báº¡n ÄÃ£ hoÃ n táº¥t base track vÃ  `make verify` exit 0. Xem
> **[GUIDE.md â PHASE 2](../GUIDE.md)**.

á» pháº§n lab chÃ­nh, báº¡n ÄÆ°á»£c cung cáº¥p má»t prebuilt binary vÃ  má»t server hoáº¡t Äá»ng sáºµn.
Trong track nÃ y, báº¡n Äi xuá»ng má»t lá»p tháº¥p hÆ¡n: tá»± compile llama.cpp cho CPU cá»§a mÃ¬nh,
cháº¡y sweep cÃ¡c knob quan trá»ng trÃªn pháº§n cá»©ng cá»§a mÃ¬nh vÃ  giáº£i thÃ­ch káº¿t quáº£.

> **Laptop yáº¿u hoáº·c chá» cÃ³ CPU thÆ°á»ng hÆ°á»ng lá»£i nhiá»u nháº¥t á» B1.** Prebuilt binary dÃ¹ng
> trong lab pháº£i cháº¡y ÄÆ°á»£c trÃªn nhiá»u mÃ¡y nÃªn chá» nháº¯m tá»i má»t CPU baseline chung. Báº£n
> build dÃ nh cho CPU tháº­t cá»§a báº¡n cÃ³ thá» dÃ¹ng ÄÃºng cÃ¡c vector extension mÃ  CPU há» trá»£.
> VÃ¬ váº­y, khoáº£ng cÃ¡ch thÆ°á»ng rÃµ nháº¥t trÃªn pháº§n cá»©ng khiÃªm tá»n. ÄÃ¢y thÆ°á»ng lÃ  speedup lá»n
> nháº¥t cÃ³ thá» Äáº¡t ÄÆ°á»£c trong lab nÃ y.

**Thá»i gian dá»± kiáº¿n:** 60â120 phÃºt. RiÃªng bÆ°á»c build máº¥t 5â15 phÃºt. Má»i sweep máº¥t
5â15 phÃºt. **KhÃ´ng cáº§n cháº¡y táº¥t cáº£.** HÃ£y chá»n má»t hoáº·c hai má»¥c phÃ¹ há»£p vá»i pháº§n cá»©ng
vÃ  cÃ¢u há»i báº¡n muá»n tráº£ lá»i.

---

## NÄm tiÃªu chÃ­ bonus, má»i tiÃªu chÃ­ 4 Äiá»m

| # | ÄÆ°á»£c Äiá»m khi | Lá»nh | Äiá»m |
|--:|---|---|--:|
| B1 | Compile llama.cpp cho CPU cá»§a báº¡n vÃ  **so vá»i prebuilt binary** | `make build-llama && make compare-builds` | 4 |
| B2 | Cháº¡y Ã­t nháº¥t 1 sweep | `make sweep-quant` / `sweep-ctx` / `sweep-batch` / `sweep-gpu` | 4 |
| B3 | Speedup **cá»§a bonus track** cÃ³ before/after rÃµ rÃ ng | REFLECTION Â§6 (tá»« B1 hoáº·c B2, **khÃ´ng** pháº£i káº¿t quáº£ `make tune` cá»§a base) | 4 |
| B4 | LÃ m Ã­t nháº¥t 1 challenge C1âC7 hoáº·c C10 | [`bonus/CHALLENGES.md`](CHALLENGES.md) | 4 |
| B5 | Má»t so sÃ¡nh runtime/regime â **chá»n 1**: MLX (Mac) Â· C8 semantic cache Â· C9 embedding serving Â· C6 Vulkan vs CUDA | `make mlx-compare` Â· `make semantic-cache` Â· `make embed-demo` | 4 |

**Tá»ng bonus: 20 Äiá»m.**

Chi tiáº¿t tá»«ng challenge cÃ³ trong [`CHALLENGES.md`](CHALLENGES.md).

B1 yÃªu cáº§u cáº£ hai pháº§n: build tá»« mÃ£ nguá»n **vÃ ** so sÃ¡nh vá»i prebuilt binary báº±ng
`make compare-builds`. Chá» build thÃ nh cÃ´ng chÆ°a Äá»§ Äá» Äáº¡t B1.

B5 cÃ³ bá»n lá»±a chá»n Äá» má»i ná»n táº£ng Äá»u cÃ³ thá» Äáº¡t 20/20:

| MÃ¡y cá»§a báº¡n | Lá»±a chá»n B5 |
|---|---|
| Apple Silicon | `make mlx-compare` â MLX so vá»i llama.cpp Metal trÃªn cÃ¹ng model; cáº§n `pip install 'mlx-lm>=0.31.3' mlx` |
| NVIDIA GPU | **C6** Vulkan so vá»i CUDA; báº¡n ÄÃ£ cÃ³ phÃ­a Vulkan/prebuilt |
| Má»i ná»n táº£ng | **C8** `make semantic-cache` â cache náº±m phÃ­a trÃªn KV cache |
| Má»i ná»n táº£ng | **C9** `make serve-embed && make embed-demo` â regime bá» giá»i háº¡n bá»i prefill |

C8 vÃ  C9 cÅ©ng cháº¡y ÄÆ°á»£c vá»i `--offline`. Khi ÄÃ³, script dÃ¹ng embedding tá»ng há»£p vÃ 
khÃ´ng cáº§n server. Báº¡n cÃ³ thá» Äá»c, cháº¡y vÃ  phÃ¢n tÃ­ch logic trong lÃºc chá» táº£i model.

TrÆ°á»c khi chá»n, báº¡n cáº§n biáº¿t hai Äiá»m sau:

- **Model chá» áº£nh hÆ°á»ng tá»i má»t challenge.** C1 vá» speculative decoding cáº§n MTP head
  cá»§a Gemma 4 E2B. Qwen3.5 0.8B khÃ´ng phÃ¡t hÃ nh MTP head. B1, B2, B3, B5 vÃ  C2âC10
  Äá»u dÃ¹ng ÄÆ°á»£c vá»i cáº£ hai model. Vá»i model nhá», hÃ£y chá»n C2, C5, C7, C8 hoáº·c C9 thay
  cho C1. CÃ¡c sweep Äá»c dáº£i quantization tá»« model registry, nÃªn `make sweep-quant`
  tá»± thÃ­ch á»©ng vá»i model báº¡n ÄÃ£ chá»n.

- **MLX:** khi strict load, `mlx-lm` tá»« chá»i khoáº£ng 140 parameter trong bá» Gemma 4
  MLX weights cá»§a Unsloth. Gemma 4 E2B dÃ¹ng chung KV á» 20 trong sá» 35 layer, cÃ²n quÃ¡
  trÃ¬nh chuyá»n Äá»i váº«n giá»¯ láº¡i táº¥t cáº£ parameter. Script
  `compare-mlx-vs-llama-cpp.py` phÃ¡t hiá»n trÆ°á»ng há»£p nÃ y, thá»­ láº¡i báº±ng non-strict load
  vÃ  in má»t sample generation. Báº¡n pháº£i kiá»m tra sample ÄÃ³ cÃ³ máº¡ch láº¡c trÆ°á»c khi
  tin vÃ o sá» Äo. BÃ i nÃ y cáº§n `mlx-lm >= 0.31.3`.

- **C8 semantic cache:** lab khÃ´ng cÃ³ embedding model chuyÃªn dá»¥ng. VÃ¬ váº­y,
  `make serve-embed` cháº¡y chat model á» pooling mode. ÄÃ¢y lÃ  má»t sentence encoder yáº¿u;
  paraphrase tháº­t cÃ³ thá» nháº­n Äiá»m tháº¥p hÆ¡n prompt khÃ´ng liÃªn quan. BÃ i lÃ m khÃ´ng yÃªu
  cáº§u bÃ¡o hit rate. Báº¡n pháº£i cháº©n ÄoÃ¡n váº¥n Äá»: nÃªu má»t false hit vÃ  má»t false miss kÃ¨m
  Äiá»m sá», rá»i chá»©ng minh khÃ´ng cÃ³ má»t threshold duy nháº¥t sá»­a ÄÆ°á»£c cáº£ hai. HÃ£y Äá»c C8
  trÆ°á»c khi báº¯t Äáº§u.

---

## NÃªn cháº¡y sweep nÃ o

| TrÆ°á»ng há»£p | NÃªn cháº¡y | LÃ½ do |
|---|---|---|
| Chá» cÃ³ CPU | **B1** `compare-builds`, rá»i kháº£o sÃ¡t thread ká»¹ hÆ¡n | Compile flag vÃ  sá» thread lÃ  hai knob chÃ­nh cá»§a báº¡n |
| RAM háº¡n cháº¿ | `make sweep-quant` | Äo trá»±c tiáº¿p ÄÃ¡nh Äá»i giá»¯a kÃ­ch thÆ°á»c, tá»c Äá» vÃ  cháº¥t lÆ°á»£ng |
| CÃ³ GPU | `make sweep-gpu` | TÃ¬m Äiá»m partial offload khÃ´ng cÃ²n cáº£i thiá»n |
| LÃ m RAG vá»i context dÃ i | `make sweep-ctx` | Quan sÃ¡t chi phÃ­ prefill tÄng phi tuyáº¿n vÃ  tÃ¡c Äá»ng lÃªn TTFT |
| Phá»¥c vá»¥ nhiá»u ngÆ°á»i dÃ¹ng | `make sweep-batch` | Äo cÃ¡ch chunked prefill Äá»i throughput láº¥y TTFT |

Cáº¥u trÃºc thÆ° má»¥c:

```
bonus/
âââ 01-build-from-source.md   â per-OS, per-backend build guide
âââ compare-builds.py         â B1: prebuilt vs your build, same model, same workload
âââ CHALLENGES.md             â C1-C10, pick one and go deep
âââ sweeps/
â   âââ quant-sweep.py        â Unsloth Dynamic ladder, UD-IQ2_M -> UD-Q8_K_XL
â   âââ ctx-len-sweep.py      â prefill cost vs prompt length
â   âââ batch-size-sweep.py   â -b / -ub, chunked prefill
â   âââ gpu-offload-sweep.py  â -ngl 0..99
âââ serving-regimes/
â   âââ embedding-serving.py  â C9, prefill-bound regime
â   âââ semantic-cache-demo.py â C8, meaning-based cache
âââ mlx/
    âââ compare-mlx-vs-llama-cpp.py   â B5 on Apple Silicon
```

CÃ¡c report ÄÆ°á»£c ghi vÃ o `benchmarks/bonus-*.md` á» thÆ° má»¥c gá»c cá»§a repo. HÃ£y commit
nhá»¯ng tá»p nÃ y.

---

## LiÃªn há» vá»i ná»i dung trong deck

Deck trÃ¬nh bÃ y FlashAttention, PagedAttention, cÃ¡ch chá»n kernel FA3 so vá»i FA4 vÃ  MLA.
ÄÃ³ lÃ  cÃ¡c quyáº¿t Äá»nh trÃªn GPU datacenter. Báº¡n khÃ´ng cháº¡y ÄÆ°á»£c FA3 trÃªn laptop, nhÆ°ng
váº«n cÃ³ thá» Äo cÃ¹ng má»t loáº¡i ÄÃ¡nh Äá»i á» quy mÃ´ nhá»:

| Knob trÃªn laptop | TrÆ°á»ng há»£p tÆ°Æ¡ng á»©ng á» datacenter |
|---|---|
| Sá» thread `-t` | Äá» rá»ng parallelism / kÃ­ch thÆ°á»c TP |
| `-b` / `-ub` | Láº­p lá»ch chunked prefill |
| Lá»±a chá»n quantization | Ma tráº­n quyáº¿t Äá»nh FP8 / INT4 / NVFP4 |
| Layer offload `-ngl` | Pháº§n cháº¡y trÃªn accelerator so vá»i host |
| `-DGGML_NATIVE=ON` | Chá»n FA3 cho Hopper so vá»i FA4 cho Blackwell |

Sau khi tá»± Äo, báº¡n cÃ³ thá» xem `--gpu-memory-utilization` cá»§a vLLM nhÆ° má»t ÄÃ¡nh Äá»i cáº§n
kiá»m chá»©ng, khÃ´ng pháº£i má»t con sá» máº·c Äá»nh Ã¡p dá»¥ng cho má»i mÃ¡y.

---

## CÃ¡ch viáº¿t bÃ¡o cÃ¡o

Trong `submission/REFLECTION.md`, dÃ¹ng **Â§6**. Â§5 dÃ nh cho thay Äá»i cá»§a base track;
B3 pháº£i dÃ¹ng káº¿t quáº£ cá»§a bonus track.

```
Change:  <e.g. rebuilt llama.cpp with -DGGML_NATIVE=ON on a CPU with AVX-512>
Before:  <number + units>
After:   <number + units>
Speedup: <X.Y>x
Why it worked (1-2 paragraphs): <a mechanism, not vibes -- memory bandwidth?
                                 vector width? cache residency? scheduling?>
```

Má»i report ÄÆ°á»£c sinh dÆ°á»i `benchmarks/` Äá»u káº¿t thÃºc báº±ng má»t section cÃ³ ÄÃ¡nh dáº¥u
**"required -- replace this line"**. Báº¡n pháº£i thay dÃ²ng ÄÃ³ báº±ng nháº­n xÃ©t cá»§a mÃ¬nh.
Náº¿u cÃ²n sÃ³t, `make verify` sáº½ fail. Sá» liá»u chá» lÃ  Äáº§u vÃ o; pháº§n giáº£i thÃ­ch má»i lÃ  ná»i
dung ÄÆ°á»£c cháº¥m.

HÃ£y trung thá»±c khi káº¿t quáº£ trÃ¡i vá»i ká»³ vá»ng. Má»t finding ÄÆ°á»£c giáº£i thÃ­ch ká»¹ cÃ³ giÃ¡ trá»
hÆ¡n nÄm báº£ng sá» liá»u nÃ´ng. Káº¿t quáº£ Äi ngÆ°á»£c deck nhÆ°ng ÄÆ°á»£c phÃ¢n tÃ­ch rÃµ thÆ°á»ng ÄÆ°á»£c
cháº¥m cao hÆ¡n káº¿t quáº£ ÄÃºng ká»³ vá»ng mÃ  khÃ´ng cÃ³ giáº£i thÃ­ch.

## KhÃ´ng so sÃ¡nh giá»¯a cÃ¡c laptop

Sá» liá»u cá»§a báº¡n khÃ´ng so sÃ¡nh ÄÆ°á»£c vá»i sá» liá»u cá»§a báº¡n cÃ¹ng lá»p. So sÃ¡nh há»£p lá» lÃ 
before vÃ  after trÃªn cÃ¹ng mÃ¡y cá»§a báº¡n.
