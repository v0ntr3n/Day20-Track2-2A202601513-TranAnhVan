# Hardware Guide

> CÃ¡ch lÃ m lab tá»«ng bÆ°á»c: **[GUIDE.md](GUIDE.md)** Â· Cháº¥m Äiá»m: [`rubric.md`](rubric.md)

> **Laptop cá»§a báº¡n *lÃ * lab.** KhÃ´ng cÃ³ shared sandbox. Rubric thÆ°á»ng Äá» rÃµ rÃ ng
> cá»§a *your own before/after*, khÃ´ng pháº£i absolute throughput. Äá»«ng so sá» vá»i báº¡n
> cÃ¹ng lá»p â so vá»i `make bench` láº§n Äáº§u cá»§a chÃ­nh báº¡n.

## 1. Äiá»u kiá»n tá»i thiá»u

| | YÃªu cáº§u |
|---|---|
| RAM | **8 GB** vá»i Gemma 4 E2B Â· **4 GB** vá»i Qwen3.5 0.8B (`LAB_MODEL=qwen35-0.8b`) |
| ÄÄ©a trá»ng | ~10 GB (Gemma) hoáº·c ~3 GB (Qwen3.5 0.8B), gá»m runtime + deps |
| Python | â¥ 3.10 |
| GPU | **khÃ´ng cáº§n** |
| Compiler | **khÃ´ng cáº§n** (chá» bonus B1 má»i cáº§n cmake) |
| Docker | **khÃ´ng cáº§n bao giá»** |

**RAM < 8 GB?** Cháº¡y local vá»i model nhá»: `LAB_MODEL=qwen35-0.8b make setup`.
**RAM < 4 GB?** DÃ¹ng [`cloud/`](cloud/README.md) (Colab hoáº·c Kaggle) vÃ  khai bÃ¡o á»
REFLECTION Â§1. Äiá»m khÃ´ng bá» áº£nh hÆ°á»ng â rubric cháº¥m láº­p luáº­n, khÃ´ng cháº¥m pháº§n cá»©ng.

## 2. Model â chá»n má»t trong hai

Cáº£ hai Apache-2.0, **khÃ´ng gated**: khÃ´ng token, khÃ´ng accept license.

| | **Gemma 4 E2B** *(máº·c Äá»nh)* | **Qwen3.5 0.8B** |
|---|---|---|
| Repo | [unsloth/gemma-4-E2B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E2B-it-GGUF) | [unsloth/Qwen3.5-0.8B-GGUF](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) |
| `LAB_MODEL=` | `gemma4-e2b` | `qwen35-0.8b` |
| primary | `gemma-4-E2B-it-UD-Q4_K_XL.gguf` â 2.97 GB | `Qwen3.5-0.8B-Q4_K_M.gguf` â 0.50 GB |
| compare | `gemma-4-E2B-it-UD-Q2_K_XL.gguf` â 2.24 GB | `Qwen3.5-0.8B-UD-Q2_K_XL.gguf` â 0.39 GB |
| Tá»ng táº£i | ~5.2 GB | **~0.9 GB** |
| RAM tá»i thiá»u | 8 GB | **4 GB** |
| Context | 128K | 256K |
| Bonus C1 (MTP) | cÃ³ `mtp-gemma-4-E2B-it.gguf` | khÃ´ng cÃ³ |
| Bonus B5 (MLX) | `unsloth/gemma-4-E2B-it-UD-MLX-4bit` | `mlx-community/Qwen3.5-0.8B-4bit` |

**Gemma 4 E2B**: "E2B" = *effective* 2B tham sá». Model dÃ¹ng per-layer embeddings nÃªn tá»ng
tham sá» lá»n hÆ¡n 2B, cÃ²n chi phÃ­ tÃ­nh toÃ¡n má»i token tÆ°Æ¡ng ÄÆ°Æ¡ng má»t model 2B. ÄÃ³ lÃ  lÃ½ do
file 4-bit ~3 GB chá»© khÃ´ng pháº£i ~1.2 GB.

**Qwen3.5 0.8B**: nhá» hÆ¡n ~6 láº§n, load nhanh hÆ¡n gáº¥p ÄÃ´i, decode nhanh hÆ¡n ~1.5 láº§n trÃªn
cÃ¹ng mÃ¡y. ÄÃ¡nh Äá»i lÃ  cháº¥t lÆ°á»£ng cÃ¢u tráº£ lá»i â 0.8B tham sá» thÃ¬ ÄÃºng nhÆ° 0.8B tham sá». Vá»i
má»t lab vá» **latency vÃ  throughput** thÃ¬ ÄÃ¢y lÃ  ÄÃ¡nh Äá»i hoÃ n toÃ n há»£p lÃ½, vÃ  báº£n thÃ¢n viá»c
so hai model cÅ©ng lÃ  má»t quan sÃ¡t ÄÃ¡ng viáº¿t.

**"UD"** = Unsloth Dynamic: cÃ¡c layer nháº¡y cáº£m ÄÆ°á»£c giá»¯ á» precision cao hÆ¡n, nÃªn báº£n 2-bit
dÃ¹ng ÄÆ°á»£c tháº­t thay vÃ¬ há»ng háº³n nhÆ° `Q2_K` pháº³ng. RiÃªng Qwen3.5 0.8B dÃ¹ng `Q4_K_M` chuáº©n
lÃ m primary (repo khÃ´ng cÃ³ `Q2_K` pháº³ng Äá» so, nÃªn compare lÃ  `UD-Q2_K_XL`).

Cáº£ lab chá» cáº§n 2 file. Bonus `make sweep-quant` má»i táº£i thÃªm.

## 3. Runtime â prebuilt, khÃ´ng compile

`labs/00-setup/fetch-runtime.py` Äá»c `hardware.json`, há»i GitHub release API cá»§a
llama.cpp (pin á» build **`b10488`**), rá»i chá»n asset ÄÃºng cho mÃ¡y báº¡n:

| MÃ¡y | Asset ÄÆ°á»£c chá»n | Táº£i vá» |
|---|---|--:|
| macOS Apple Silicon | `bin-macos-arm64` (Metal cÃ³ sáºµn) | 11 MB |
| macOS Intel | `bin-macos-x64` | ~12 MB |
| Linux x64, CPU | `bin-ubuntu-x64` | 16 MB |
| Linux x64 + GPU báº¥t ká»³ | `bin-ubuntu-vulkan-x64` | 32 MB |
| Linux ARM64 | `bin-ubuntu-arm64` | ~15 MB |
| Windows x64, CPU | `bin-win-cpu-x64` | 18 MB |
| Windows + NVIDIA | `bin-win-cuda-<ver>-x64` + CUDA runtime DLLs | ~140â240 MB |
| Windows + AMD | `bin-win-rocm-7.14-x64` | 188 MB |
| Windows ARM64 | `bin-win-cpu-arm64` | ~17 MB |

Vá»i NVIDIA trÃªn Windows, script Äá»c CUDA version mÃ  driver há» trá»£ (`nvidia-smi`) vÃ 
chá»n build cao nháº¥t mÃ  driver cháº¡y ÄÆ°á»£c, kÃ¨m `cudart` DLLs.

> **Linux + NVIDIA:** llama.cpp **khÃ´ng** publish prebuilt CUDA cho Linux. Script sáº½
> chá»n **Vulkan** â cháº¡y tá»t trÃªn NVIDIA, chá» cháº­m hÆ¡n CUDA má»t chÃºt. Muá»n CUDA tháº­t
> thÃ¬ compile: `LLAMA_CMAKE_FLAGS=-DGGML_CUDA=ON make build-llama`. ÄÃ¢y chÃ­nh lÃ 
> bonus **C6** (Vulkan vs CUDA head-to-head) â báº¡n cÃ³ sáºµn cáº£ hai Äá» so.

Ghi ÄÃ¨ lá»±a chá»n tá»± Äá»ng:

```bash
.venv/bin/python labs/00-setup/fetch-runtime.py --list                       # xem háº¿t asset
.venv/bin/python labs/00-setup/fetch-runtime.py --asset <tÃªn> --force        # chá»n tay
```

## 4. Backend nÃ o cho pháº§n cá»©ng nÃ o

| Accelerator | Prebuilt cÃ³? | cmake flag (bonus B1) |
|---|---|---|
| CPU (má»i OS) | â luÃ´n cÃ³ | *(default)* + `-DGGML_NATIVE=ON` |
| Apple Metal | â trong build macOS-arm64 | `-DGGML_METAL=ON` |
| NVIDIA CUDA | â Windows Â· â Linux (dÃ¹ng Vulkan) | `-DGGML_CUDA=ON` |
| AMD ROCm | â Windows Â· â Linux (dÃ¹ng Vulkan) | `-DGGML_HIPBLAS=ON` |
| Vulkan (Intel Arc, AMD, NVIDIA) | â Linux + Windows | `-DGGML_VULKAN=ON` |

`make probe` ÄÃ£ chá»n giÃºp báº¡n â cá»t cmake chá» dÃ¹ng khi lÃ m bonus B1.

## 5. Náº¿u laptop báº¡n lÃ  mÃ¡y yáº¿u nháº¥t lá»p

ÄÃ³ lÃ  **lá»£i tháº¿** á» bonus track, khÃ´ng pháº£i báº¥t lá»£i:

- `make tune` (core) â thread count lÃ  knob lá»n nháº¥t trÃªn CPU. Curve rÃµ nháº¥t trÃªn
  mÃ¡y nhiá»u core nhÆ°ng bandwidth háº¹p.
- `make build-llama && make compare-builds` (B1) â prebuilt binary ÄÆ°á»£c compile cho
  CPU baseline chung. Build riÃªng cho CPU cá»§a báº¡n vá»i `-DGGML_NATIVE=ON` thÆ°á»ng lÃ 
  speedup lá»n nháº¥t cáº£ lab, vÃ  **cÃ ng rÃµ trÃªn mÃ¡y yáº¿u**.
- `make sweep-quant` (B2) â RAM cháº­t thÃ¬ ÄÃ¢y lÃ  quyáº¿t Äá»nh tháº­t, khÃ´ng pháº£i bÃ i táº­p.

## 6. Network

- Hugging Face cÃ³ thá» bá» cháº·n á» máº¡ng trÆ°á»ng. Náº¿u `make setup` fail á» bÆ°á»c model,
  xem [`labs/00-setup/MANUAL-DOWNLOAD.md`](labs/00-setup/MANUAL-DOWNLOAD.md).
- GitHub release API giá»i háº¡n 60 request/giá»/IP. Cáº£ lá»p cÃ¹ng NAT cÃ³ thá» cháº¡m giá»i
  háº¡n â script tá»± fallback sang báº£ng tÃªn asset cÃ³ sáºµn, nÃªn váº«n táº£i ÄÆ°á»£c.
- KhÃ´ng cÃ³ Docker pull nÃ o trong toÃ n bá» lab.

## 7. MLX, MLC, ExecuTorch?

**MLX** lÃ  bonus B5 cho Apple Silicon â Unsloth publish Gemma 4 E2B á» cáº£ GGUF vÃ 
MLX, nÃªn ÄÃ³ lÃ  so sÃ¡nh *runtime* tháº­t (cÃ¹ng model, cÃ¹ng 4-bit), khÃ´ng pháº£i so hai
model khÃ¡c nhau. MLC LLM / ExecuTorch / Core ML ÄÆ°á»£c deck nháº¯c nhÆ°ng khÃ´ng build vÃ o
lab; chá»n lÃ m stretch project náº¿u báº¡n xong sá»m.
