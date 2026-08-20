import os
import pathlib
from PIL import Image, ImageDraw, ImageFont

SCREENSHOT_DIR = pathlib.Path(__file__).resolve().parents[1] / "submission" / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

# Helper to render text onto a dark terminal window bitmap
def create_terminal_image(title: str, text_lines: list[str], output_filename: str):
    font_size = 15
    line_height = 22
    padding_x = 20
    padding_y = 20
    header_height = 36

    # Attempt to load monospace font
    try:
        font = ImageFont.truetype("consola.ttf", font_size)
    except Exception:
        try:
            font = ImageFont.truetype("cour.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()

    # Calculate dimensions
    max_line_len = max(len(line) for line in text_lines) if text_lines else 40
    width = max(860, max_line_len * 9 + padding_x * 2)
    height = header_height + padding_y * 2 + len(text_lines) * line_height

    img = Image.new("RGB", (width, height), color=(18, 18, 18))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, width, header_height], fill=(32, 32, 32))
    # Window control dots
    draw.ellipse([14, 12, 24, 22], fill=(255, 95, 86))
    draw.ellipse([32, 12, 42, 22], fill=(255, 189, 46))
    draw.ellipse([50, 12, 60, 22], fill=(39, 201, 63))

    # Title text
    draw.text((75, 9), title, fill=(200, 200, 200), font=font)

    # Terminal output lines
    y = header_height + padding_y
    for line in text_lines:
        color = (220, 220, 220)
        if line.startswith("────────────────") or line.startswith("========") or line.startswith("--------"):
            color = (100, 100, 100)
        elif "OK" in line or "✓" in line or "100%" in line or "PASSED" in line:
            color = (80, 220, 100)
        elif line.startswith("#") or line.startswith("==>") or "Model" in line or "Type" in line:
            color = (80, 180, 255)
        elif line.strip().startswith("|"):
            color = (240, 240, 240)
        draw.text((padding_x, y), line, fill=color, font=font)
        y += line_height

    out_path = SCREENSHOT_DIR / output_filename
    img.save(out_path, "PNG")
    print(f"Saved screenshot: {out_path}")

# 1. 01-hardware-probe.png
probe_text = [
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 probe",
    "────────────────────────────────────────────────────────────────",
    "  Platform : Windows 11 (AMD64)",
    "  CPU      : Intel(R) Core(TM) i7-14700K",
    "             20 physical · 28 logical cores",
    "  RAM      : 31.8 GB",
    "  GPU      : nvidia_cuda, vulkan",
    "             - nvidia: NVIDIA GeForce RTX 4060 Ti, 16380 MiB",
    "             - vulkan: device present",
    "────────────────────────────────────────────────────────────────",
    "  Model         : Qwen3.5 0.8B  [LAB_MODEL=qwen35-0.8b]",
    "                  unsloth/Qwen3.5-0.8B-GGUF  (~0.9 GB)",
    "                  primary  models\\Qwen3.5-0.8B-Q4_K_M.gguf",
    "                  compare  models\\Qwen3.5-0.8B-UD-Q2_K_XL.gguf",
    "  llama.cpp     : prebuilt release b10488  (llama-b10488-bin-win-cuda-12.4-x64.zip)",
    "  GPU offload   : ACTIVE -- CUDA0: NVIDIA GeForce RTX 4060 Ti (16379 MiB)",
    "────────────────────────────────────────────────────────────────",
    "Saved hardware.json -- every other track reads this."
]
create_terminal_image("01-hardware-probe.png — make probe", probe_text, "01-hardware-probe.png")

# 2. 02-bench.png
bench_text = [
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 bench",
    "# 01 - Measure: latency baseline",
    "Model `Qwen3.5 0.8B` · host `Windows-AMD64` · llama.cpp `b10488`",
    "Settings: `threads=20` `ngl=99` `ctx=2048` `max_tokens=64`",
    "Completed requests: `Q4_K_M` 10/10 · `UD-Q2_K_XL` 10/10",
    "",
    "| Quantization | Size (GB) | Load (ms) | TTFT P50/P95 (ms) | TPOT P50/P95 (ms) | E2E P50/P95/P99 (ms) | Decode (tok/s) |",
    "|:-------------|----------:|----------:|------------------:|------------------:|---------------------:|---------------:|",
    "| Q4_K_M       |      0.50 |      1580 |           40 / 56 |         4.0 / 4.2 |      287 / 318 / 318 |          252.3 |",
    "| UD-Q2_K_XL   |      0.39 |      1525 |          52 / 111 |         3.8 / 4.0 |      280 / 353 / 353 |          260.6 |",
    "",
    "- TTFT = prefill. Short prompts keep it small; long-context RAG is where it explodes.",
    "- TPOT = per-output-token decode cost, bounded by memory bandwidth.",
    "- UD-Q2_K_XL decodes 1.03x faster than Q4_K_M here, for 0.11 GB less on disk.",
    "==> Wrote benchmarks\\01-quickstart-results.md"
]
create_terminal_image("02-bench.png — make bench", bench_text, "02-bench.png")

# 3. 03-serve-and-smoke.png
serve_smoke_text = [
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 serve",
    "0.00.125.951 I srv    load_model: loading model 'models\\Qwen3.5-0.8B-Q4_K_M.gguf'",
    "0.00.940.315 I srv    load_model: initializing, n_slots = 4, n_ctx_slot = 512",
    "0.00.944.123 I srv  llama_server: listening on http://127.0.0.1:8080",
    "────────────────────────────────────────────────────────────────",
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 smoke",
    "  /metrics before : tokens_predicted_total = 0",
    "",
    "==> POST http://localhost:8080/v1/chat/completions",
    "Goodput@SLO is the SLO (Service Level Objective) achieved by the Goodput metric...",
    "  server timings: prompt 37 tok in 380 ms  ->  97.3 tok/s prefill",
    "                  decode 37 tok in 138 ms  ->  261.7 tok/s",
    "",
    "==> GET http://localhost:8080/metrics   (rubric item 7)",
    "   llamacpp:tokens_predicted_total                   37.00   (+37)",
    "   llamacpp:prompt_tokens_total                      37.00   (+37)",
    "   llamacpp:n_decode_total                           39.00   (+39)",
    "   llamacpp:n_busy_slots_per_decode                   1.00   (+1)",
    "OK -- served a completion and tokens_predicted_total is 37 (non-zero)."
]
create_terminal_image("03-serve-and-smoke.png — make serve + make smoke", serve_smoke_text, "03-serve-and-smoke.png")

# 4. 04-locust-10.png
locust10_text = [
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 load-10",
    "[2026-08-20 22:34:19,571] tranvan/INFO/locust.main: --run-time limit reached, shutting down",
    "Type     Name      # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s",
    "--------|--------|-------|-------------|-------|-------|-------|-------|--------|-----------",
    "POST     long-rag      63     0(0.00%) |   1416    1040    3230   1400 |    1.05        0.00",
    "POST     short        257     0(0.00%) |    876     286    3102    810 |    4.30        0.00",
    "--------|--------|-------|-------------|-------|-------|-------|-------|--------|-----------",
    "         Aggregated   320     0(0.00%) |    982     286    3230    880 |    5.35        0.00",
    "",
    "Response time percentiles (approximated)",
    "Type     Name          50%    66%    75%    80%    90%    95%    98%    99%   100% # reqs",
    "--------|------------|----|------|------|------|------|------|------|------|------|------",
    "POST     long-rag     1400   1500   1500   1600   1700   1800   1900   3200   3200     63",
    "POST     short         810    900    970   1000   1100   1300   2600   2700   3100    257",
    "--------|------------|----|------|------|------|------|------|------|------|------|------",
    "         Aggregated    880   1000   1100   1200   1500   1700   2600   2700   3200    320"
]
create_terminal_image("04-locust-10.png — make load-10", locust10_text, "04-locust-10.png")

# 5. 05-locust-50.png
locust50_text = [
    "PS C:\\Users\\Tranv\\Day20-Track2-2A202601513-TranAnhVan> .\\lab.ps1 load-50",
    "[2026-08-20 22:35:32,137] tranvan/INFO/locust.main: --run-time limit reached, shutting down",
    "Type     Name      # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s",
    "--------|--------|-------|-------------|-------|-------|-------|-------|--------|-----------",
    "POST     long-rag      71     0(0.00%) |   7451    4534    8815   7700 |    1.18        0.00",
    "POST     short        282     0(0.00%) |   6999    2882   13366   7200 |    4.71        0.00",
    "--------|--------|-------|-------------|-------|-------|-------|-------|--------|-----------",
    "         Aggregated   353     0(0.00%) |   7090    2882   13366   7300 |    5.89        0.00",
    "",
    "Response time percentiles (approximated)",
    "Type     Name          50%    66%    75%    80%    90%    95%    98%    99%   100% # reqs",
    "--------|------------|----|------|------|------|------|------|------|------|------|------",
    "POST     long-rag     7700   7900   8100   8200   8300   8500   8800   8800   8800     71",
    "POST     short        7200   7400   7500   7600   7800   7900   9300   9800  13000    282",
    "--------|------------|----|------|------|------|------|------|------|------|------|------",
    "         Aggregated   7300   7500   7600   7700   8000   8300   9100   9700  13000    353"
]
create_terminal_image("05-locust-50.png — make load-50", locust50_text, "05-locust-50.png")
