# Táº£i model thá»§ cÃ´ng

DÃ¹ng trang nÃ y khi `make setup` khÃ´ng táº£i ÄÆ°á»£c model (máº¡ng trÆ°á»ng cháº·n Hugging Face,
captive portal, máº¡ng quÃ¡ cháº­m).

## Chá»n model trÆ°á»c

Lab cÃ³ hai option â táº£i ÄÃºng bá» cá»§a model báº¡n chá»n (xem [GUIDE.md](../../GUIDE.md) BÆ°á»c 0.2):

| `LAB_MODEL=` | Model | Tá»ng táº£i |
|---|---|--:|
| `gemma4-e2b` *(máº·c Äá»nh)* | Gemma 4 E2B | ~5.2 GB |
| `qwen35-0.8b` | Qwen3.5 0.8B | ~0.9 GB |

## Option A â Gemma 4 E2B (máº·c Äá»nh)

**[unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF)**
â Apache-2.0, **khÃ´ng gated**: khÃ´ng cáº§n login, khÃ´ng cáº§n token, khÃ´ng cáº§n accept license.

Xem toÃ n bá» file: **[tree/main](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/tree/main)**

| Vai trÃ² | File | Size |
|---|---|--:|
| primary (báº¯t buá»c) | `gemma-4-E2B-it-UD-Q4_K_XL.gguf` | 2.97 GB |
| compare (báº¯t buá»c) | `gemma-4-E2B-it-UD-Q2_K_XL.gguf` | 2.24 GB |
| bonus C1 (optional) | `mtp-gemma-4-E2B-it.gguf` | 0.09 GB |

Báº¡n cáº§n **hai file Äáº§u**. Thiáº¿u file `compare` thÃ¬ máº¥t hÃ ng thá»© hai cá»§a rubric 3â5.

## Option B â Qwen3.5 0.8B (nhá», ~0.9 GB)

**[unsloth/Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF)** â Apache-2.0, khÃ´ng gated.
Xem file: [tree/main](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/tree/main)

| Vai trÃ² | File | Size |
|---|---|--:|
| primary | `Qwen3.5-0.8B-Q4_K_M.gguf` | 0.50 GB |
| compare | `Qwen3.5-0.8B-UD-Q2_K_XL.gguf` | 0.39 GB |

```bash
mkdir -p models
curl -L -o models/Qwen3.5-0.8B-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-Q4_K_M.gguf
curl -L -o models/Qwen3.5-0.8B-UD-Q2_K_XL.gguf \
  https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF/resolve/main/Qwen3.5-0.8B-UD-Q2_K_XL.gguf
```

Rá»i ghi manifest vá»i **cÃ¹ng** `LAB_MODEL` báº¡n dÃ¹ng:

```bash
LAB_MODEL=qwen35-0.8b .venv/bin/python labs/00-setup/download-model.py --skip-download
```

---

## CÃ¡ch 1 â curl / wget (cho Gemma 4 E2B)

Cháº¡y á» **repo root**:

```bash
mkdir -p models

curl -L -o models/gemma-4-E2B-it-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q4_K_XL.gguf

curl -L -o models/gemma-4-E2B-it-UD-Q2_K_XL.gguf \
  https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q2_K_XL.gguf
```

`-L` lÃ  báº¯t buá»c â Hugging Face redirect sang CDN. Náº¿u bá» ngáº¯t giá»¯a ÄÆ°á»ng, thÃªm `-C -`
Äá» tiáº¿p tá»¥c thay vÃ¬ táº£i láº¡i tá»« Äáº§u:

```bash
curl -L -C - -o models/gemma-4-E2B-it-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q4_K_XL.gguf
```

Windows PowerShell:

```powershell
mkdir models -Force
curl.exe -L -o models\gemma-4-E2B-it-UD-Q4_K_XL.gguf `
  https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q4_K_XL.gguf
curl.exe -L -o models\gemma-4-E2B-it-UD-Q2_K_XL.gguf `
  https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q2_K_XL.gguf
```

## CÃ¡ch 2 â mirror (khi Hugging Face bá» cháº·n háº³n)

`hf-mirror.com` dÃ¹ng **ÄÃºng ÄÆ°á»ng dáº«n**, chá» Äá»i hostname:

```bash
curl -L -o models/gemma-4-E2B-it-UD-Q4_K_XL.gguf \
  https://hf-mirror.com/unsloth/gemma-4-E2B-it-GGUF/resolve/main/gemma-4-E2B-it-UD-Q4_K_XL.gguf
```

Hoáº·c set biáº¿n mÃ´i trÆ°á»ng rá»i Äá» script tá»± táº£i nhÆ° bÃ¬nh thÆ°á»ng:

```bash
HF_ENDPOINT=https://hf-mirror.com make setup
```

## CÃ¡ch 3 â browser

Má» [tree/main](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF/tree/main), báº¥m icon â¬
cáº¡nh hai file, rá»i copy chÃºng vÃ o `models/` trong repo. ThÆ° má»¥c con thoáº£i mÃ¡i â script
tÃ¬m Äá» quy.

## Sau khi cÃ³ file: ghi manifest

```bash
.venv/bin/python labs/00-setup/download-model.py --skip-download                    # Gemma
LAB_MODEL=qwen35-0.8b .venv/bin/python labs/00-setup/download-model.py --skip-download   # Qwen
```

Lá»nh nÃ y khÃ´ng táº£i gÃ¬, chá» tÃ¬m file vÃ  ghi `models/active.json` (rubric item 2). ThÃªm
`--with-mtp` náº¿u báº¡n cÅ©ng táº£i MTP head.

Kiá»m tra:

```bash
make verify      # má»¥c "Model manifest" pháº£i PASS
```

## Kiá»m tra file cÃ³ nguyÃªn váº¹n khÃ´ng

Náº¿u server bÃ¡o lá»i láº¡ khi load model, kháº£ nÄng cao file bá» táº£i thiáº¿u. So size:

```bash
ls -l models/*.gguf
```

Pháº£i khá»p báº£ng cá»§a model báº¡n chá»n (Gemma: 2.97 + 2.24 GB Â· Qwen: 0.50 + 0.39 GB).
File nhá» hÆ¡n ÄÃ¡ng ká» = táº£i dá», xoÃ¡ vÃ  táº£i láº¡i.

## Náº¿u tÃªn file khÃ´ng khá»p

`--skip-download` tÃ¬m ÄÃºng tÃªn trong báº£ng trÃªn. Unsloth ÄÃ´i khi re-upload vá»i nhÃ£n quant
khÃ¡c. Khi ÄÃ³: Äá»i tÃªn file cho khá»p, **hoáº·c** sá»­a tuple `primary` / `compare` trong dict `MODELS` á»
[`lib/labkit.py`](../../lib/labkit.py) vÃ  ghi láº¡i viá»c ÄÃ³ trong REFLECTION Â§1.

## Runtime binary cÅ©ng bá» cháº·n?

`fetch-runtime.py` táº£i tá»« GitHub Releases, thÆ°á»ng thÃ´ng khi Hugging Face bá» cháº·n. Náº¿u cáº£
GitHub cÅ©ng bá» cháº·n:

```bash
.venv/bin/python labs/00-setup/fetch-runtime.py --list      # in ra tÃªn cÃ¡c asset
```

Táº£i asset ÄÃºng platform cá»§a báº¡n tá»«
<https://github.com/ggml-org/llama.cpp/releases/tag/b10488> rá»i giáº£i nÃ©n vÃ o
`runtime/b10488/`. Layout bÃªn trong khÃ´ng quan trá»ng â lab tÃ¬m binary báº±ng glob.

## Váº«n khÃ´ng ÄÆ°á»£c?

MÃ¡y dÆ°á»i 8 GB RAM: thá»­ `LAB_MODEL=qwen35-0.8b` trÆ°á»c â chá» ~0.9 GB.
DÆ°á»i 4 GB RAM hoáº·c máº¡ng khÃ´ng thÃ´ng: dÃ¹ng [`cloud/`](../../cloud/README.md)
(Colab / Kaggle). Äiá»m khÃ´ng bá» áº£nh hÆ°á»ng, chá» cáº§n khai bÃ¡o á» REFLECTION Â§1.
