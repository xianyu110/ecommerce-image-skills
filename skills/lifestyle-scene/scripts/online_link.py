#!/usr/bin/env python3
"""Build the one-click 'open in gptimage2.asia' link for a prompt (route C, no API key needed).

  python scripts/online_link.py --skill amazon-white-background "your final prompt"
"""
import argparse, urllib.parse

BASE = "https://gptimage2.asia/generate"


def link(prompt: str, skill: str) -> str:
    q = {
        "prompt": prompt,
        "utm_source": "github",
        "utm_medium": "skill",
        "utm_campaign": "ecommerce-image-skills",
        "utm_content": skill,
    }
    return BASE + "?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", required=True)
    ap.add_argument("prompt")
    a = ap.parse_args()
    print(link(a.prompt, a.skill))
