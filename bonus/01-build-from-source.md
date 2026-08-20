# Build llama.cpp tá»« mÃ£ nguá»n (bonus B1)

Báº¡n ÄÃ£ cÃ³ llama.cpp hoáº¡t Äá»ng. `make setup` táº£i prebuilt release. Váº­y vÃ¬ sao cáº§n
compile?

**Prebuilt binary ÄÆ°á»£c compile cho má»t CPU cÃ³ thá» khÃ´ng giá»ng CPU cá»§a báº¡n.** Binary ÄÃ³
pháº£i cháº¡y trÃªn má»i mÃ¡y táº£i vá» nÃªn nháº¯m tá»i má»t instruction set baseline tháº­n trá»ng.
CPU cá»§a báº¡n cÃ³ thá» há» trá»£ AVX2, AVX-512 hoáº·c NEON. `-DGGML_NATIVE=ON` cho phÃ©p compiler
dÃ¹ng ÄÃºng instruction set tÃ¬m tháº¥y trÃªn mÃ¡y.

ÄÃ¢y lÃ  thÃ­ nghiá»m cáº§n lÃ m: **cÃ¹ng source revision, cÃ¹ng model, cÃ¹ng runtime flag; chá»
khÃ¡c giáº£ Äá»nh cá»§a compiler.**

```bash
make build-llama       # clone + compile (5-15 min)
make compare-builds    # benchmark both binaries, write the report
```

`compare-builds.py` ghi báº£ng before/after vÃ  tá»· lá» speedup vÃ o
`benchmarks/bonus-build-compare-tg128.md`. Tá»p nÃ y cÃ¹ng pháº§n giáº£i thÃ­ch cá»§a báº¡n ÄÃ¡p á»©ng
B1 vÃ  cÅ©ng cÃ³ thá» ÄÃ¡p á»©ng B3.

B1 yÃªu cáº§u báº¡n **build tá»« mÃ£ nguá»n vÃ  so sÃ¡nh vá»i prebuilt binary**. Chá» cháº¡y
`make build-llama` lÃ  chÆ°a Äá»§. Báº¡n pháº£i cháº¡y thÃªm `make compare-builds`.

Laptop yáº¿u hoáº·c chá» cÃ³ CPU thÆ°á»ng hÆ°á»ng lá»£i nhiá»u nháº¥t. Prebuilt binary nháº¯m tá»i má»t
CPU baseline chung, cÃ²n `-DGGML_NATIVE=ON` nháº¯m ÄÃºng CPU cá»§a báº¡n.

---

## 1. `make build-llama` thá»±c hiá»n gÃ¬

Target nÃ y clone llama.cpp á» build ÄÆ°á»£c cá» Äá»nh lÃ  `b10488`. ÄÃ¢y cÅ©ng lÃ  build cá»§a
prebuilt binary, nhá» ÄÃ³ phÃ©p so sÃ¡nh cÃ´ng báº±ng. Source náº±m trong `bonus/llama.cpp/`.
Sau ÄÃ³ target cháº¡y:

```bash
cmake -B build $LLAMA_CMAKE_FLAGS -DGGML_NATIVE=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --config Release
```

Äiá»u kiá»n cáº§n: **cmake** vÃ  C++ toolchain.

| Há» Äiá»u hÃ nh | CÃ¡ch cÃ i Äáº·t |
|---|---|
| macOS | `xcode-select --install && brew install cmake` |
| Ubuntu/Debian | `sudo apt install cmake build-essential` |
| Fedora | `sudo dnf install cmake gcc-c++` |
| Windows | Visual Studio Build Tools + cmake trong PATH |

## 2. CÃ¡c backend flag

Truyá»n flag bá» sung qua `LLAMA_CMAKE_FLAGS`. Target luÃ´n thÃªm
`-DGGML_NATIVE=ON` vÃ  `-DCMAKE_BUILD_TYPE=Release`.

### Chá» dÃ¹ng CPU â trÆ°á»ng há»£p ÄÃ¡ng Äo nháº¥t cho bonus nÃ y

```bash
make build-llama          # nothing extra needed
```

`-DGGML_NATIVE=ON` táº¡o ra khÃ¡c biá»t. ÄÃ¢y thÆ°á»ng lÃ  nÆ¡i khoáº£ng cÃ¡ch vá»i prebuilt binary
rÃµ nháº¥t.

### DÃ¹ng NVIDIA CUDA

```bash
LLAMA_CMAKE_FLAGS="-DGGML_CUDA=ON" make build-llama
```

Cáº§n CUDA Toolkit 12 trá» lÃªn. Kiá»m tra báº±ng `nvcc --version`. TrÃªn Linux, ÄÃ¢y lÃ  cÃ¡ch
duy nháº¥t Äá» dÃ¹ng CUDA vÃ¬ llama.cpp **khÃ´ng phÃ¡t hÃ nh prebuilt CUDA binary cho Linux**.
Sinh viÃªn Linux cÃ³ NVIDIA cháº¡y prebuilt Vulkan trong core lab. VÃ¬ váº­y, build vá»i
`-DGGML_CUDA=ON` rá»i cháº¡y `make compare-builds` táº¡o ra phÃ©p so sÃ¡nh Vulkan vá»i CUDA vÃ 
Äá»ng thá»i hoÃ n thÃ nh challenge **C6**.

### DÃ¹ng Apple Metal

```bash
LLAMA_CMAKE_FLAGS="-DGGML_METAL=ON" make build-llama
```

Metal ÄÃ£ ÄÆ°á»£c báº­t trong prebuilt macOS-arm64 binary. VÃ¬ váº­y, khoáº£ng cÃ¡ch cÃ³ thá» nhá».
Náº¿u cÃ³ cáº£i thiá»n, nÃ³ thÆ°á»ng Äáº¿n tá»« cÃ¡c ÄÆ°á»ng cháº¡y phÃ­a CPU nhÆ° sampling vÃ  tokenization.
Káº¿t quáº£ gáº§n báº±ng khÃ´ng váº«n há»£p lá» náº¿u báº¡n giáº£i thÃ­ch nguyÃªn nhÃ¢n.

### DÃ¹ng AMD ROCm trÃªn Linux

```bash
LLAMA_CMAKE_FLAGS="-DGGML_HIPBLAS=ON -DAMDGPU_TARGETS=gfx1100 \
  -DCMAKE_C_COMPILER=hipcc -DCMAKE_CXX_COMPILER=hipcc" make build-llama
```

Thay `gfx1100` báº±ng target cá»§a báº¡n. Kiá»m tra báº±ng `rocminfo | grep gfx`. CÃ¡c target
thÆ°á»ng gáº·p gá»m `gfx1030` cho RX 6800/6900, `gfx1100` cho RX 7900 vÃ  `gfx90a`/`gfx942`
cho Instinct.

### DÃ¹ng Vulkan

```bash
LLAMA_CMAKE_FLAGS="-DGGML_VULKAN=ON" make build-llama
```

Cáº§n Vulkan SDK. Lá»nh `vulkaninfo --summary` pháº£i cháº¡y ÄÆ°á»£c.

## 3. CÃ¡c CPU flag khÃ¡c ÄÃ¡ng thá»­

| Flag | TÃ¡c dá»¥ng | Khi nÃªn dÃ¹ng |
|---|---|---|
| `-DGGML_NATIVE=ON` | DÃ¹ng instruction set tháº­t cá»§a CPU | LuÃ´n dÃ¹ng; target tá»± thÃªm |
| `-DGGML_NATIVE=OFF` | Buá»c dÃ¹ng báº£n CPU baseline chung | Challenge C7, lÃ m váº¿ so sÃ¡nh cÃ²n láº¡i |
| `-DGGML_LTO=ON` | Link-time optimization | Chi phÃ­ tháº¥p, ÄÃ´i khi cáº£i thiá»n vÃ i pháº§n trÄm |
| `-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS` | DÃ¹ng BLAS ngoÃ i cho prefill | Khi ÄÃ£ cÃ i OpenBLAS/MKL; thÆ°á»ng giÃºp `pp`, hiáº¿m khi giÃºp `tg` |
| `-DCMAKE_BUILD_TYPE=Release` | `-O3 -DNDEBUG` | LuÃ´n dÃ¹ng; target tá»± thÃªm |

KhÃ´ng bao giá» so sÃ¡nh má»t báº£n Debug vá»i má»t báº£n Release rá»i gá»i chÃªnh lá»ch ÄÃ³ lÃ 
speedup. `make build-llama` luÃ´n truyá»n Release. Náº¿u build thá»§ cÃ´ng, báº¡n pháº£i tá»± kiá»m
tra Äiá»u nÃ y.

## 4. Kiá»m tra báº£n build

```bash
./bonus/llama.cpp/build/bin/llama-cli --version
./bonus/llama.cpp/build/bin/llama-bench \
    -m models/gemma-4-E2B-it-UD-Q4_K_XL.gguf -t 4 -ngl 99
```

`labkit.runtime_bin()` tá»± tÃ¬m `bonus/llama.cpp/` sau khi build. VÃ¬ váº­y, cÃ¡c lab script
sáº½ dÃ¹ng báº£n nÃ y. RiÃªng `compare-builds.py` khÃ´ng dÃ¹ng cÆ¡ cháº¿ tá»± tÃ¬m; script cá» Äá»nh
tá»«ng phÃ­a Äá» giá»¯ phÃ©p so sÃ¡nh trung thá»±c.

## 5. Cháº¡y server báº±ng báº£n build cá»§a báº¡n

```bash
./bonus/llama.cpp/build/bin/llama-server \
    -m models/gemma-4-E2B-it-UD-Q4_K_XL.gguf \
    --host 127.0.0.1 --port 8080 -t <best-from-make-tune> -ngl 99 \
    --parallel 4 --cont-batching --metrics
```

Sau ÄÃ³ cháº¡y láº¡i `make load-50 && make load-report` Äá» kiá»m tra má»©c cáº£i thiá»n khi
compile cÃ³ cÃ²n giá»¯ ÄÆ°á»£c dÆ°á»i concurrency hay khÃ´ng. Káº¿t quáº£ khÃ´ng pháº£i lÃºc nÃ o cÅ©ng
giá»¯ nguyÃªn. Viá»c giáº£i thÃ­ch nguyÃªn nhÃ¢n cÃ³ giÃ¡ trá» hÆ¡n chá» bÃ¡o token/giÃ¢y.

Má»i report ÄÆ°á»£c sinh dÆ°á»i `benchmarks/` Äá»u káº¿t thÃºc báº±ng má»t section cÃ³ ÄÃ¡nh dáº¥u
**"required -- replace this line"**. HÃ£y thay dÃ²ng ÄÃ³ báº±ng nháº­n xÃ©t cá»§a báº¡n. Náº¿u cÃ²n
sÃ³t, `make verify` sáº½ fail.
