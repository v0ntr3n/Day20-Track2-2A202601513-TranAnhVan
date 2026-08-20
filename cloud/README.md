# Cloud fallback â Colab / Kaggle

> CÃ¡c bÆ°á»c cá»§a lab khÃ´ng Äá»i: **[GUIDE.md](../GUIDE.md)**

ÄÃ¢y lÃ  **phÆ°Æ¡ng Ã¡n fallback**, khÃ´ng pháº£i cÃ¡ch cháº¡y máº·c Äá»nh. HÃ£y dÃ¹ng
[`Day20-lab.ipynb`](Day20-lab.ipynb) khi laptop cÃ³ dÆ°á»i **4 GB RAM**, hoáº·c khi setup local
gáº·p lá»i báº¡n khÃ´ng thá» xá»­ lÃ½.

> **Thá»­ cÃ¡ch nÃ y trÆ°á»c.** Náº¿u mÃ¡y báº¡n cÃ³ 4â8 GB RAM, báº¡n váº«n cháº¡y ÄÆ°á»£c lab **local** vá»i
> model nhá»:
>
> ```bash
> LAB_MODEL=qwen35-0.8b make setup
> ```
>
> Qwen3.5 0.8B chá» ~0.9 GB vÃ  cáº§n 4 GB RAM. Cháº¡y local luÃ´n tá»t hÆ¡n cloud vÃ¬ báº¡n Äo ÄÆ°á»£c
> chÃ­nh mÃ¡y mÃ¬nh â ÄÃ³ lÃ  má»¥c ÄÃ­ch cá»§a lab.

## DÃ¹ng cloud khÃ´ng máº¥t Äiá»m

Rubric cháº¥m Äá» rÃµ rÃ ng cá»§a setup, phÃ©p Äo vÃ  láº­p luáº­n. Rubric khÃ´ng cháº¥m tá»c Äá» tuyá»t
Äá»i vÃ  khÃ´ng giáº£ Äá»nh hai sinh viÃªn cÃ³ pháº§n cá»©ng giá»ng nhau.

Tuy nhiÃªn, báº¡n **báº¯t buá»c pháº£i khai bÃ¡o** trong **REFLECTION Â§1** ráº±ng mÃ¬nh dÃ¹ng cloud
fallback vÃ  nÃªu lÃ½ do. Viá»c khai bÃ¡o **khÃ´ng lÃ m máº¥t Äiá»m**. Notebook tá»± ghi
`runtime_environment: "colab"` hoáº·c `"kaggle"` vÃ o `hardware.json`, nÃªn báº¡n chá» cáº§n
thÃªm má»t dÃ²ng giáº£i thÃ­ch.

## Má» notebook

| Ná»n táº£ng | CÃ¡ch má» |
|---|---|
| **Colab** | Má» trá»±c tiáº¿p: [colab.research.google.com/github/VinUni-AI20k/Day20-Track2-ModelServing/blob/main/cloud/Day20-lab.ipynb](https://colab.research.google.com/github/VinUni-AI20k/Day20-Track2-ModelServing/blob/main/cloud/Day20-lab.ipynb) â hoáº·c File â Open notebook â GitHub â paste URL repo |
| **Kaggle** | Má» [kaggle.com/code](https://www.kaggle.com/code) â New Notebook â File â Import Notebook â upload `cloud/Day20-lab.ipynb` |

**TrÃªn Kaggle, pháº£i báº­t Internet** trong settings sidebar trÆ°á»c khi cháº¡y. Náº¿u Internet
táº¯t, notebook khÃ´ng thá» táº£i model.

Cell Äáº§u tiÃªn ÄÃ£ trá» sáºµn tá»i repo gá»c (public) nÃªn báº¡n cháº¡y ÄÆ°á»£c ngay. Äá»i `REPO_URL`
sang fork cá»§a báº¡n náº¿u muá»n â khÃ´ng báº¯t buá»c, vÃ¬ artifact ÄÆ°á»£c sinh trong VM rá»i báº¡n
táº£i zip vá» mÃ¡y.

## CPU hay GPU?

TrÃªn VM 2 vCPU, model nhá» lÃ  lá»±a chá»n há»£p lÃ½ hÆ¡n. Set trong cell Äáº§u:
`LAB_MODEL = 'qwen35-0.8b'` â táº£i nhanh hÆ¡n ~6 láº§n vÃ  decode nhanh hÆ¡n, nÃªn cáº£ notebook
cháº¡y xong nhanh hÆ¡n nhiá»u.

Notebook máº·c Äá»nh dÃ¹ng `RUNTIME = 'cpu'`. ÄÃ¢y lÃ  cáº¥u hÃ¬nh chá»§ ÄÃ­ch vÃ  cháº¡y ÄÆ°á»£c toÃ n bá»
base track, nhÆ°ng cháº­m hÆ¡n. Vá»i 2 vCPU, má»i benchmark cÃ³ thá» máº¥t vÃ i phÃºt.

Notebook khÃ´ng máº·c Äá»nh dÃ¹ng GPU vÃ¬ llama.cpp **khÃ´ng cung cáº¥p prebuilt Linux CUDA
binary**. Image Colab/Kaggle cÅ©ng **khÃ´ng cÃ³ Vulkan driver**. VÃ¬ váº­y cÃ¡c prebuilt asset
tÄng tá»c khÃ´ng cÃ³ backend phÃ¹ há»£p Äá» sá»­ dá»¥ng.

Muá»n dÃ¹ng T4, báº¡n pháº£i compile vá»i `-DGGML_CUDA=ON`. Cell 4b thá»±c hiá»n viá»c nÃ y trong
khoáº£ng 8 phÃºt.

Pháº§n compile khÃ´ng bá» lÃ£ng phÃ­: nÃ³ Äáº¡t bonus **B1**. Khi cÃ³ cáº£ CUDA build vÃ  Vulkan
prebuilt trÃªn cÃ¹ng má»t mÃ¡y, báº¡n cÅ©ng cÃ³ sáºµn Äiá»u kiá»n cho challenge **C6**.

## Artifact vÃ  filename khÃ´ng Äá»i

Notebook cháº¡y cÃ¹ng cÃ¡c script vá»i cÃ¡ch lÃ m trÃªn laptop, nÃªn sinh ÄÃºng cÃ¡c file sau:

```
hardware.json
models/active.json
benchmarks/01-quickstart-results.md
benchmarks/01-tuning-tg128.md
benchmarks/02-server-results.md
benchmarks/02-server-batching-u50.md  +  02-server-metrics-u50.csv
benchmarks/locust-10_stats.csv  Â·  locust-50_stats.csv
```

`scripts/verify.py` khÃ´ng cáº§n nhÃ¡nh xá»­ lÃ½ riÃªng cho cloud.

## HoÃ n táº¥t bÃ i trÃªn mÃ¡y local

Cell cuá»i cÃ¹ng nÃ©n cÃ¡c file báº±ng chá»©ng, khÃ´ng nÃ©n model weights. Download file zip, giáº£i
nÃ©n vÃ o clone local cá»§a báº¡n, rá»i lÃ m láº§n lÆ°á»£t:

1. Thay má»i section **"required -- replace this line"** trong `benchmarks/*.md` báº±ng
   nháº­n xÃ©t cá»§a báº¡n. Náº¿u cÃ²n báº¥t ká»³ section nÃ o, `make verify` sáº½ fail.
2. Äiá»n `submission/REFLECTION.md`, gá»m cáº£ khai bÃ¡o cloud trong Â§1.
3. ThÃªm 5 screenshots tá»« output cá»§a cÃ¡c notebook cell.
4. Cháº¡y `make verify` vÃ  báº£o Äáº£m lá»nh **exit 0**. Sau ÄÃ³ push lÃªn repo **public** vÃ 
   submit URL.

## Lá»i thÆ°á»ng gáº·p

| Váº¥n Äá» | CÃ¡ch xá»­ lÃ½ |
|---|---|
| Session ngáº¯t giá»¯a chá»«ng | Cháº¡y láº¡i tá»« section 3. BÆ°á»c clone vÃ  download sáº½ bá» qua pháº§n ÄÃ£ cÃ³ trÃªn disk. |
| Kaggle bÃ¡o "no internet" | Settings sidebar â Internet â On. |
| Colab free tier háº¿t thá»i gian | RÃºt ngáº¯n load test: set `LOAD_DURATION = '30s'` trong cell 1. |
| `unknown model architecture: 'gemma4'` | BÆ°á»c táº£i runtime ÄÃ£ bá» bá» qua hoáº·c fail. Cháº¡y láº¡i section 4. |
| `couldn't bind HTTP server socket ... port: 8080` | Colab ÄÃ£ chiáº¿m port 8080. Notebook ÄÃ£ set `LAB_SERVER_PORT = '8090'` sáºµn â náº¿u báº¡n sá»­a dÃ²ng ÄÃ³ thÃ¬ chá»n port cÃ²n trá»ng khÃ¡c. |
| Háº¿t disk | Free tier thÆ°á»ng Äá»§ cho 5.2 GB. Náº¿u buá»c pháº£i xÃ³a, xÃ³a `models/*Q2*`; báº¡n sáº½ máº¥t hÃ ng quantization thá»© hai cá»§a rubric 3â5. |

## Sá» Äo tháº­t trÃªn Colab (ÄÃ£ kiá»m chá»©ng)

ToÃ n bá» base track ÄÃ£ ÄÆ°á»£c cháº¡y end-to-end trÃªn má»t Colab CPU runtime. ÄÃ¢y lÃ  káº¿t quáº£
tháº­t, Äá» báº¡n biáº¿t trÆ°á»c cÃ¡i gÃ¬ lÃ  bÃ¬nh thÆ°á»ng:

| | Colab CPU runtime |
|---|--:|
| CPU | Intel Xeon @ 2.20 GHz, **1 physical / 2 logical** core, AVX2 |
| RAM | 12.7 GB |
| Model load (Qwen3.5 0.8B Q4_K_M) | ~3.5 s |
| Decode | **~8â10 tok/s** |
| 1 request 48 token | **~6â7 s** |
| Tráº§n throughput | **~0.15 request/s** â chá» 1 core, thÃªm slot khÃ´ng giÃºp |
| Request hoÃ n thÃ nh trong 1 phÃºt load | **~7â10** |
| `requests_deferred` lÃºc 50 user | **46** |

Hai Äiá»u rÃºt ra:

1. **Percentile sáº½ má»ng.** Ãt máº«u thÃ¬ percentile khÃ´ng cháº¯c, vÃ  `load-report` tá»± cáº£nh bÃ¡o
   Äiá»u ÄÃ³. Muá»n sá» cháº¯c hÆ¡n thÃ¬ Äáº·t `LOAD_DURATION = '3m'` á» cell 1.
2. **Báº±ng chá»©ng saturation láº¡i rÃµ hÆ¡n trÃªn mÃ¡y cháº­m.** `processing=4` cÃ¹ng vá»i
   `deferred=46` lÃ  hÃ¬nh áº£nh trá»±c tiáº¿p cá»§a queue time â ÄÃºng chá» goodput bá» máº¥t mÃ  deck
   Â§8 nÃ³i tá»i. TrÃªn laptop nhanh, gauge nÃ y thÆ°á»ng báº±ng 0 vÃ  bÃ i há»c khÃ³ tháº¥y hÆ¡n.

TrÃªn Colab, `verify` cÅ©ng bÃ¡o `hardware.json` vÃ  cÃ¡c file `locust-*_stats.csv` lÃ 
`NOT committed`. BÃ¬nh thÆ°á»ng: clone trong VM khÃ´ng pháº£i repo cá»§a báº¡n. Sau khi giáº£i nÃ©n
zip vÃ o clone local vÃ  `git add`, cÃ¡c dÃ²ng ÄÃ³ sáº½ háº¿t.

Thread sweep (`tune`) trÃªn VM 1 core cho grid ráº¥t ngáº¯n â thÆ°á»ng chá» `[1, 2]` vá»i spread
~1.07x. Váº«n há»£p lá»; pháº§n giáº£i thÃ­ch má»i lÃ  chá» ÄÆ°á»£c cháº¥m.

## Giá»i háº¡n cáº§n nÃªu trong REFLECTION

Cloud VM khÃ´ng pháº£i laptop cá»§a báº¡n. VM cÃ³ core count vÃ  memory bandwidth khÃ¡c, cháº¡y
qua hypervisor, vÃ  cÃ³ thá» chia sáº» host vá»i workload cá»§a ngÆ°á»i khÃ¡c. VÃ¬ váº­y, káº¿t quáº£
tuning mÃ´ táº£ **VM ÄÆ°á»£c cáº¥p**, khÃ´ng mÃ´ táº£ laptop cá»§a báº¡n. Thread-count curve cÅ©ng cÃ³
thá» ráº¥t khÃ¡c mÃ¡y váº­t lÃ½.

HÃ£y nÃªu giá»i háº¡n nÃ y trong **REFLECTION Â§5**. ÄÃ¢y lÃ  má»t pháº§n quan trá»ng khi diá»n giáº£i
sá» liá»u, Äáº·c biá»t náº¿u báº¡n dÃ¹ng cloud fallback.
