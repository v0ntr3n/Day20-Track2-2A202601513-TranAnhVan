# CÃ¡c challenge bonus â chá»n má»t má»¥c vÃ  phÃ¢n tÃ­ch sÃ¢u

CÃ¡c sweep lÃ  pháº§n khá»i Äá»ng. Nhá»¯ng challenge dÆ°á»i ÄÃ¢y cÃ³ tÃ­nh má». **HÃ£y chá»n má»t.**
Má»t bÃ i C5 ÄÆ°á»£c giáº£i thÃ­ch sÃ¢u tá»t hÆ¡n viá»c lÃ m C1, C2 vÃ  C3 á» má»©c sÆ¡ sÃ i.

C1âC7 vÃ  C10 ÄÃ¡p á»©ng tiÃªu chÃ­ bonus **B4**. C6, C8 vÃ  C9 cÅ©ng cÃ³ thá» dÃ¹ng riÃªng Äá» ÄÃ¡p á»©ng
**B5**. Xem [`README.md`](README.md). TrÆ°á»c tiÃªn, hÃ£y kiá»m tra má»i flag trÃªn binary cá»§a
báº¡n báº±ng `llama-server --help | grep <flag>`. llama.cpp thay Äá»i nhanh vÃ  tÃ i liá»u nÃ y
ÄÆ°á»£c cá» Äá»nh theo build `b10488`.

---

## C1. Speculative decoding báº±ng MTP head cá»§a Gemma 4

> **YÃªu cáº§u `LAB_MODEL=gemma4-e2b`.** Qwen3.5 0.8B khÃ´ng phÃ¡t hÃ nh MTP head, nÃªn
> challenge nÃ y chá» dÃ¹ng ÄÆ°á»£c vá»i Gemma. Náº¿u dÃ¹ng model nhá», hÃ£y chá»n C2, C5, C7, C8
> hoáº·c C9.

Gemma 4 E2B phÃ¡t hÃ nh riÃªng má»t **MTP (multi-token prediction) head** dÆ°á»i dáº¡ng GGUF.
Báº¡n khÃ´ng cáº§n tÃ¬m má»t draft model tÆ°Æ¡ng thÃ­ch tokenizer vÃ¬ draft khá»p vá»i target ÄÃ£
ÄÆ°á»£c phÃ¡t hÃ nh cÃ¹ng model.

```bash
.venv/bin/python labs/00-setup/download-model.py --with-mtp     # ~98 MB
llama-server --help | grep -iE "draft|mtp|spec"       # find the current flag names
```

Trong build `b10488`, cÃ¡c draft flag lÃ  `-md/--model-draft` vÃ  `--draft-max`, **khÃ´ng
pháº£i** `--draft-model`. TÃªn sau lÃ  cÃ¡ch viáº¿t cá»§a vLLM. MTP head ÄÆ°á»£c gáº¯n qua `-md` hay
má»t flag chuyÃªn biá»t lÃ  Äiá»u báº¡n pháº£i xÃ¡c nháº­n báº±ng `--help` trÆ°á»c khi
cháº¡y.

Äo token/giÃ¢y khi báº­t vÃ  táº¯t speculative decoding á» 2â3 má»©c temperature. Deck nÃªu
EAGLE-3 Äáº¡t 3â6.5Ã, nhÆ°ng káº¿t quáº£ cá»§a báº¡n cÃ³ thá» tháº¥p hÆ¡n nhiá»u. HÃ£y giáº£i thÃ­ch khoáº£ng
cÃ¡ch dá»±a trÃªn acceptance rate, tá»· lá» kÃ­ch thÆ°á»c draft/target vÃ  áº£nh hÆ°á»ng cá»§a greedy
so vá»i sampled decoding.

Speculative decoding lÃ  má»t tá»i Æ°u latency. Khi concurrency cao, chi phÃ­ verification
cÃ³ thá» lÃ m káº¿t quáº£ cháº­m hÆ¡n. VÃ¬ váº­y, production engine thÆ°á»ng táº¯t cÆ¡ cháº¿ nÃ y khi batch
size vÆ°á»£t má»t threshold. Cháº¡y `make load-50` khi báº­t vÃ  táº¯t nÃ³ Äá» kiá»m tra hiá»n tÆ°á»£ng
trÃªn mÃ¡y cá»§a báº¡n.

## C2. Quantization cho KV cache

```bash
.venv/bin/python labs/02-serve/serve.py -- --cache-type-k q8_0 --cache-type-v q8_0
```

ÄÃ¢y lÃ  cÃ¡ch kiá»m tra Ã½ tÆ°á»ng âFP8 KV cacheâ trong deck trÃªn CPU, Metal hoáº·c Vulkan.
Äo ba yáº¿u tá»: lÆ°á»£ng RAM giáº£m, thay Äá»i latency vÃ  thay Äá»i cháº¥t lÆ°á»£ng. Theo dÃµi RSS cá»§a
process khi `--ctx-size` tÄng. Vá»i cháº¥t lÆ°á»£ng, hÃ£y táº¡o má»t eval gá»m 10 prompt cÃ³ thá»
cháº¥m tá»± Äá»ng, cháº³ng háº¡n trÃ­ch xuáº¥t JSON hoáº·c phÃ©p tÃ­nh sá» há»c. Tiáº¿t kiá»m bá» nhá» nhÆ°ng
lÃ m giáº£m accuracy khÃ´ng pháº£i lÃ  má»t káº¿t quáº£ tá»t.

## C3. Phá»¥c vá»¥ nhiá»u LoRA

`--lora` cháº¥p nháº­n nhiá»u adapter. TÃ¬m hoáº·c train hai LoRA nhá». Hugging Face cÃ³ nhiá»u
lá»±a chá»n, cháº³ng háº¡n má»t LoRA cho SQL vÃ  má»t LoRA cho tool calling. Phá»¥c vá»¥ cáº£ hai trÃªn
cÃ¹ng base weights, rá»i Äo chi phÃ­ chuyá»n adapter theo tá»«ng request. ÄÃ¢y lÃ  khung phá»¥c
vá»¥ Multi-LoRA trong deck, gá»m Punica vÃ  S-LoRA, á» quy mÃ´ laptop.

## C4. Láº¥y máº«u Best-of-N vá»i reranker

Gá»­i cÃ¹ng má»t prompt N láº§n song song vá»i cÃ¡c seed khÃ¡c nhau, sau ÄÃ³ dÃ¹ng má»t reranker
nháº¹ Äá» chá»n cÃ¢u tráº£ lá»i tá»t nháº¥t. CÃ³ thá» báº¯t Äáº§u báº±ng heuristic vá» Äá» dÃ i hoáº·c má»©c láº·p.
Äo end-to-end latency vÃ  cháº¥t lÆ°á»£ng so vá»i single-shot.

Má»¥c ÄÃ­ch lÃ  kiá»m tra cÃ¡ch dÃ¹ng throughput Äá» tÄng cháº¥t lÆ°á»£ng cho má»t ngÆ°á»i dÃ¹ng thay vÃ¬
phá»¥c vá»¥ thÃªm ngÆ°á»i dÃ¹ng. CÃ¡c slot cá»§a `--parallel` khÃ´ng phÃ¢n biá»t hai cÃ¡ch sá»­ dá»¥ng nÃ y.

## C5. Challenge âmodel nhá» nháº¥t váº«n há»¯u Ã­châ

Náº¿u laptop cá»§a báº¡n cháº­m, hÃ£y Äi dáº§n xuá»ng dáº£i Unsloth Dynamic:
`UD-Q8_K_XL` â `UD-Q4_K_XL` â `UD-Q2_K_XL` â `UD-IQ2_M`. TÃ¬m má»©c model ngá»«ng há»¯u Ã­ch,
khÃ´ng chá» má»©c model ngá»«ng nhanh. Tá»± cháº¥m 5 prompt á» má»i má»©c.

Sáº£n pháº©m cáº§n ná»p lÃ  láº­p luáº­n vá» quantization báº¡n thá»±c sá»± sáº½ triá»n khai trong giá»i háº¡n
RAM cá»§a mÃ¬nh, kÃ¨m má»t failure quan sÃ¡t ÄÆ°á»£c á» má»©c tháº¥p hÆ¡n káº¿ tiáº¿p.

## C6. Vulkan so vá»i CUDA trÃªn cÃ¹ng GPU *(cÅ©ng ÄÃ¡p á»©ng B5)*

Náº¿u cÃ³ NVIDIA GPU, báº¡n ÄÃ£ cÃ³ má»t ná»­a thÃ­ nghiá»m. TrÃªn Linux, prebuilt runtime cá»§a lab
lÃ  báº£n Vulkan vÃ¬ llama.cpp **khÃ´ng phÃ¡t hÃ nh prebuilt CUDA binary cho Linux**. HÃ£y build
phÃ­a CUDA:

```bash
LLAMA_CMAKE_FLAGS=-DGGML_CUDA=ON make build-llama
make compare-builds
```

Viá»c build vá»i `-DGGML_CUDA=ON` vÃ  so sÃ¡nh báº±ng `make compare-builds` Äá»ng thá»i hoÃ n
thÃ nh challenge C6. Äá»nh lÆ°á»£ng khoáº£ng cÃ¡ch, rá»i tráº£ lá»i cÃ¢u há»i chÃ­nh: vÃ¬ sao vLLM vÃ 
SGLang dÃ¹ng kernel riÃªng theo nhÃ  cung cáº¥p nhÆ° FA3, FA4, FlashMLA vÃ  TRTLLM-MHA thay vÃ¬
chá» cung cáº¥p má»t ÄÆ°á»ng Vulkan dÃ¹ng chung. Sá» Äo cá»§a báº¡n lÃ  báº±ng chá»©ng cho láº­p luáº­n.

## C7. Kháº£o sÃ¡t instruction set cá»§a CPU

Build hai láº§n vá»i `-DGGML_NATIVE=ON` vÃ  `-DGGML_NATIVE=OFF`. Váº¿ thá»© hai táº¡o má»t báº£n CPU
baseline chung. Sau ÄÃ³ so sÃ¡nh hai báº£n. Kiá»m tra CPU tháº­t sá»± há» trá»£ gÃ¬ báº±ng
`/proc/cpuinfo` trÃªn Linux hoáº·c `sysctl -a | grep machdep.cpu` trÃªn macOS, rá»i thá»­ báº­t
tÆ°á»ng minh cÃ¡c extension.

Láº­p báº£ng build flag so vá»i token/giÃ¢y. ÄÃ¢y lÃ  cÃ¹ng loáº¡i quyáº¿t Äá»nh mÃ  há» thá»ng cloud
ÄÆ°a ra khi chá»n FA3 cho Hopper hoáº·c FA4 cho Blackwell: kernel pháº£i khá»p vá»i silicon.

KhÃ´ng bao giá» so sÃ¡nh má»t báº£n Debug vá»i má»t báº£n Release rá»i gá»i chÃªnh lá»ch ÄÃ³ lÃ 
speedup.

## C8. Semantic cache â cache phÃ­a trÃªn KV cache *(cÅ©ng ÄÃ¡p á»©ng B5)*

Deck mÃ´ táº£ serving stack cÃ³ **ba táº§ng cache**:

```
request -> [1] semantic cache (meaning) -> [2] prefix/KV cache -> [3] full inference
```

Khi táº§ng 1 hit, há» thá»ng tráº£ láº¡i cÃ¢u tráº£ lá»i ÄÃ£ lÆ°u cho má»t prompt ÄÆ°á»£c paraphrase mÃ 
khÃ´ng tá»n compute, prefill hay decode. Táº§ng 2 chá» cÃ³ Ã­ch khi prefix giá»ng nhau tá»«ng byte.

```bash
make serve &            # chat       :8080
make serve-embed &      # embeddings :8081
make semantic-cache
# no servers? logic demo + threshold sweep:
.venv/bin/python bonus/serving-regimes/semantic-cache-demo.py --offline --sweep
```

**Lab khÃ´ng cÃ³ embedding model chuyÃªn dá»¥ng, nÃªn `make serve-embed` cháº¡y chat model á»
pooling mode.** Mean-pooled decoder state lÃ  má»t sentence encoder yáº¿u. Paraphrase tháº­t
cÃ³ thá» cÃ³ Äiá»m tháº¥p hÆ¡n prompt khÃ´ng liÃªn quan. KhÃ´ng bÃ¡o raw hit rate nhÆ° má»t káº¿t quáº£
cháº¥t lÆ°á»£ng. Sáº£n pháº©m cáº§n ná»p lÃ  pháº§n cháº©n ÄoÃ¡n:

- NÃªu má»t **false hit**, tá»©c prompt khÃ´ng liÃªn quan nhÆ°ng váº«n match, kÃ¨m similarity score.
- NÃªu má»t **false miss**, tá»©c paraphrase tháº­t nhÆ°ng khÃ´ng match, kÃ¨m similarity score.
- Chá»©ng minh khÃ´ng cÃ³ má»t threshold duy nháº¥t sá»­a ÄÆ°á»£c cáº£ hai trÆ°á»ng há»£p.
- Giáº£i thÃ­ch vÃ¬ sao decoder ÄÆ°á»£c train Äá» dá»± ÄoÃ¡n token káº¿ tiáº¿p khÃ´ng pháº£i sentence
  encoder tá»t, vÃ  embedding model chuyÃªn dá»¥ng nhÆ° Qwen3-Embedding, BGE-M3 hoáº·c
  EmbeddingGemma khÃ¡c á» ÄÃ¢u.

Náº¿u muá»n cÃ³ má»t ÄÆ°á»ng cong rÃµ hÆ¡n, hÃ£y Äáº·t `--embed-url` tá»i server Äang cháº¡y má»t GGUF
embedding model thá»±c vÃ  so sÃ¡nh hai phÃ¢n phá»i similarity. So sÃ¡nh weak embedder vá»i
proper embedder trÃªn cÃ¹ng prompt stream lÃ  báº±ng chá»©ng máº¡nh hÆ¡n báº£ng hit rate riÃªng láº».

Trong bÃ¡o cÃ¡o, hÃ£y nÃªu thÃªm rá»§i ro báº£o máº­t: semantic cache vÃ  prefix cache dÃ¹ng chung cÃ³
thá» lÃ m lá» thÃ´ng tin giá»¯a ngÆ°á»i dÃ¹ng qua timing side channel. Há» thá»ng production
thÆ°á»ng thÃªm salt theo tá»«ng tenant.

## C9. Phá»¥c vá»¥ embedding vÃ  reranker â pháº§n retrieval *(cÅ©ng ÄÃ¡p á»©ng B5)*

Embedding serving lÃ  má»t **regime khÃ¡c**: má»i vÄn báº£n chá» cáº§n má»t forward pass, khÃ´ng cÃ³
KV cache vÃ  khÃ´ng cÃ³ vÃ²ng decode. Throughput Äáº¿n tá»« static batch lá»n, khÃ´ng pháº£i
continuous batching.

```bash
make serve-embed &
make embed-demo
```

Äo cÃ¡ch latency thay Äá»i theo batch size trong trÆ°á»ng há»£p chá» cÃ³ prefill, rá»i so sÃ¡nh
ÄÆ°á»ng cong ÄÃ³ vá»i sá» liá»u bá» giá»i háº¡n bá»i decode á» track 02. Giáº£i thÃ­ch vÃ¬ sao chat
endpoint vÃ  embedding endpoint cáº§n chiáº¿n lÆ°á»£c batching trÃ¡i ngÆ°á»£c nhau, cÃ¹ng há» quáº£ khi
phá»¥c vá»¥ cáº£ hai sau má»t autoscaler.

Demo dÃ¹ng láº¡i chat GGUF Äá» trÃ¡nh táº£i thÃªm. Retrieval thá»±c táº¿ cáº§n embedding model chuyÃªn
dá»¥ng. HÃ£y ghi rÃµ giá»i háº¡n nÃ y trong bÃ¡o cÃ¡o.

## C10. Phá»¥c vá»¥ VLM, dáº¡ng má»

Gemma 4 E2B lÃ  model Äa phÆ°Æ¡ng thá»©c. Repo cung cáº¥p `mmproj-F16.gguf`, khoáº£ng 986 MB, lÃ m
vision projector. Deck Â§5 xáº¿p VLM serving vÃ o nhÃ³m bÃ i toÃ¡n kiá»u datacenter, nhÆ°ng báº¡n
váº«n cÃ³ thá» cháº¡y trÃªn mÃ¡y cá»§a mÃ¬nh:

```bash
# fetch mmproj-F16.gguf from the same repo, then:
.venv/bin/python labs/02-serve/serve.py -- --mmproj models/mmproj-F16.gguf
```

HÃ£y tá»± thiáº¿t káº¿ thÃ­ nghiá»m. CÃ¢u há»i chÃ­nh lÃ : má»t hÃ¬nh áº£nh trong prompt thay Äá»i TTFT vÃ 
dung lÆ°á»£ng KV cache nhÆ° tháº¿ nÃ o so vá»i cÃ¹ng sá» lÆ°á»£ng text token. Repo khÃ´ng cung cáº¥p
script cho challenge nÃ y.

---

## CÃ¡ch viáº¿t bÃ¡o cÃ¡o

Vá»i challenge ÄÃ£ chá»n, hÃ£y viáº¿t má»t section trong `submission/REFLECTION.md` hoáº·c táº¡o
`bonus/<challenge>.md`:

- **Thiáº¿t láº­p** â pháº§n cá»©ng vÃ  thay Äá»i chÃ­nh xÃ¡c báº¡n ÄÃ£ thá»±c hiá»n.
- **Sá» liá»u** â báº£ng before/after.
- **Má»t Äoáº¡n phÃ¢n tÃ­ch** â Äiá»u báº¡n rÃºt ra ngoÃ i ná»i dung ÄÃ£ cÃ³ trong deck.

HÃ£y ghi ÄÃºng káº¿t quáº£ ká» cáº£ khi nÃ³ trÃ¡i ká»³ vá»ng. Má»t finding báº¥t ngá» ÄÆ°á»£c giáº£i thÃ­ch rÃµ
thÆ°á»ng cÃ³ giÃ¡ trá» hÆ¡n káº¿t quáº£ khá»p ká»³ vá»ng nhÆ°ng khÃ´ng ÄÆ°á»£c phÃ¢n tÃ­ch.
