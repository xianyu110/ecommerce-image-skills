#!/usr/bin/env python3
"""Batch background swap / SKU recolour over a folder, using generate.py (route b).

  python batch_edit.py IN_DIR OUT_DIR --prompt-file swap.txt [--model sunburst] [--size 1024x1024]
                       [--var colour="Navy (#1F2A44)" ...] [--max-images 50] [--retries 2]

- `{name}` placeholders in the prompt are filled from each --var name=value (one output per value).
- Existing outputs are skipped (resume). Results are logged to OUT_DIR/log.csv.
- --max-images is a hard budget cap on API calls.
"""
import argparse, csv, os, re, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import generate  # noqa: E402

EXT = (".png", ".jpg", ".jpeg", ".webp")
ap = argparse.ArgumentParser()
ap.add_argument("in_dir"); ap.add_argument("out_dir")
ap.add_argument("--prompt-file", required=True)
ap.add_argument("--model", default="sunburst")
ap.add_argument("--size", default="1024x1024")
ap.add_argument("--var", action="append", default=[], help='name=value, repeatable')
ap.add_argument("--max-images", type=int, default=50)
ap.add_argument("--retries", type=int, default=2)
a = ap.parse_args()

template = open(a.prompt_file, encoding="utf-8").read()
variants = [dict()] if not a.var else [dict([v.split("=", 1)]) for v in a.var]
files = sorted(f for f in os.listdir(a.in_dir) if f.lower().endswith(EXT))
os.makedirs(a.out_dir, exist_ok=True)
log_path = os.path.join(a.out_dir, "log.csv")
new_log = not os.path.exists(log_path)
calls = 0
with open(log_path, "a", newline="", encoding="utf-8") as lf:
    log = csv.writer(lf)
    if new_log:
        log.writerow(["input", "variant", "output", "status", "seconds"])
    for f in files:
        for var in variants:
            tag = "-".join(re.sub(r"[^A-Za-z0-9]+", "", v)[:20] for v in var.values())
            out = os.path.join(a.out_dir, os.path.splitext(f)[0] + (f"-{tag}" if tag else "") + ".png")
            if os.path.exists(out):
                continue
            if calls >= a.max_images:
                print("budget cap reached (--max-images)"); sys.exit(0)
            prompt = template
            for k, v in var.items():
                prompt = prompt.replace("{" + k + "}", v)
            t = time.time(); status = "fail"
            for attempt in range(a.retries + 1):
                calls += 1
                try:
                    data = generate(prompt, a.model, a.size, [os.path.join(a.in_dir, f)])[0]
                    open(out, "wb").write(data); status = "ok"; break
                except SystemExit as e:
                    print(f"{f}: attempt {attempt+1} failed: {e}")
                    if calls >= a.max_images: break
            log.writerow([f, var, out if status == "ok" else "", status, round(time.time() - t, 1)])
            lf.flush()
            print(status, out)
