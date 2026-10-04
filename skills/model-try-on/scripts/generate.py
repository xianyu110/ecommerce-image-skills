#!/usr/bin/env python3
"""Minimal GPT Image 2.5 client for any OpenAI-compatible endpoint.

Env:
  GPTIMAGE_API_KEY   (required)  your API key
  GPTIMAGE_BASE_URL  (optional)  default https://api.openai.com  (any OpenAI-compatible gateway works)
  GPTIMAGE_MODEL     (optional)  overrides --model

Examples:
  # text-to-image (Flare)
  python scripts/generate.py --prompt "..." --size 1024x1024 --out out/main.png
  # edit with product reference(s) (Sunburst keeps logos/text better)
  python scripts/generate.py --model sunburst --image product.jpg --prompt "..." --out out/main.png

No dependencies beyond the Python standard library.
"""
import argparse, base64, json, mimetypes, os, sys, uuid, urllib.request, urllib.error

ALIASES = {
    "flare": "gpt-image-2.5-flare",
    "sunburst": "gpt-image-2.5-sunburst",
}


def _post(url, body, headers, timeout):
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:500]}")


def _multipart(fields, files):
    boundary = uuid.uuid4().hex
    out = bytearray()
    for k, v in fields.items():
        out += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    for k, path in files:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as f:
            data = f.read()
        out += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; "
                f"filename=\"{os.path.basename(path)}\"\r\nContent-Type: {mime}\r\n\r\n").encode()
        out += data + b"\r\n"
    out += f"--{boundary}--\r\n".encode()
    return bytes(out), f"multipart/form-data; boundary={boundary}"


def generate(prompt, model="flare", size="1024x1024", images=None, n=1, quality=None, timeout=300):
    key = os.environ.get("GPTIMAGE_API_KEY")
    if not key:
        sys.exit("GPTIMAGE_API_KEY is not set. Without a key, open the one-click link printed by the skill instead.")
    base = os.environ.get("GPTIMAGE_BASE_URL", "https://api.openai.com").rstrip("/")
    if base.endswith("/v1"):
        base = base[:-3]
    model = os.environ.get("GPTIMAGE_MODEL") or ALIASES.get(model, model)
    auth = {"Authorization": f"Bearer {key}"}
    if images:
        fields = {"model": model, "prompt": prompt, "size": size, "n": str(n)}
        if quality:
            fields["quality"] = quality
        body, ctype = _multipart(fields, [("image[]", p) for p in images])
        res = _post(f"{base}/v1/images/edits", body, {**auth, "Content-Type": ctype}, timeout)
    else:
        payload = {"model": model, "prompt": prompt, "size": size, "n": n}
        if quality:
            payload["quality"] = quality
        res = _post(f"{base}/v1/images/generations", json.dumps(payload).encode(),
                    {**auth, "Content-Type": "application/json"}, timeout)
    outs = []
    for item in res.get("data", []):
        if item.get("b64_json"):
            outs.append(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            with urllib.request.urlopen(item["url"], timeout=timeout) as r:
                outs.append(r.read())
    if not outs:
        sys.exit(f"No image in response: {json.dumps(res)[:500]}")
    return outs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prompt", help="prompt text (or use --prompt-file)")
    ap.add_argument("--prompt-file")
    ap.add_argument("--model", default="flare", help="flare | sunburst | any model id (default flare)")
    ap.add_argument("--size", default="1024x1024", help="1024x1024 | 1024x1536 | 1536x1024 | 2048x2048 ...")
    ap.add_argument("--image", action="append", help="reference image(s); switches to /v1/images/edits")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--quality", choices=["low", "medium", "high", "auto"])
    ap.add_argument("--out", default="out/image.png")
    a = ap.parse_args()
    prompt = a.prompt or (open(a.prompt_file, encoding="utf-8").read() if a.prompt_file else None)
    if not prompt:
        ap.error("--prompt or --prompt-file is required")
    imgs = generate(prompt, a.model, a.size, a.image, a.n, a.quality)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    root, ext = os.path.splitext(a.out)
    for i, data in enumerate(imgs):
        path = a.out if i == 0 else f"{root}-{i+1}{ext or '.png'}"
        with open(path, "wb") as f:
            f.write(data)
        print(path)


if __name__ == "__main__":
    main()
