# Showcase prompts

All images were generated with GPT Image 2.5 (`gpt-image-2.5-flare` / `gpt-image-2.5-sunburst`) through an OpenAI-compatible endpoint using `scripts/generate.py`. Sizes: 1024×1024, 1024×1536 or 1536×1024.

## Input product photo (text-to-image, Flare)

```text
Casual smartphone photo of a real product on a cluttered home office desk: a matte sage-green insulated stainless steel water bottle, 750ml, cylindrical with a natural bamboo screw lid and a short black carry loop, small white printed wordmark 'AURA' near the top of the bottle and a thin white line below it. Slightly off-center, mixed indoor lighting, a laptop edge, a pen and a coffee mug in the background, mild shadows, slight perspective tilt, everyday amateur product snapshot, photorealistic.
```

## Identity lock used in every bottle prompt

```text
PRODUCT IDENTITY LOCK (do not change): the exact bottle from the reference photo — matte sage-green insulated stainless steel bottle, tall cylinder with rounded shoulders, natural bamboo screw lid, short black carry loop, thin black ring under the lid, small white wordmark 'AURA' with a short white line below it centered on the upper body, small white '750ml' near the bottom. Keep shape, proportions, colour, logo text and placement identical.
```

## 01-white-bg.png

```text
Amazon main image. {IDENTITY_LOCK} Remove the desk and all other objects. Product alone, upright, centered, front view, on a pure white seamless background (#FFFFFF, RGB 255,255,255 everywhere outside the product). Product fills about 87% of the frame height. Soft diffused studio lighting, very subtle natural contact shadow, crisp edges, true colour. No text other than what is printed on the product, no props, no watermark, no border.
```

## 02-lifestyle.png

```text
Lifestyle product photo for an ecommerce listing. {IDENTITY_LOCK} Scene: a sunny morning trail-side picnic — the bottle stands on a flat granite rock beside a folded linen trail map and a small backpack strap, soft golden-hour backlight, shallow depth of field with green forest bokeh, condensation-free matte finish. A young hiker's hand is just reaching for the bottle from the right edge. Product is the clear hero, sharp, about 45% of the frame, realistic scale. Photorealistic, editorial outdoor brand style, no added text.
```

## 03-infographic.png

```text
Ecommerce selling-point infographic, portrait 2:3. {IDENTITY_LOCK} Bottle on the left half on a soft sage-to-cream gradient background with gentle studio light. Right half: clean modern layout with a bold headline 'KEEPS ICE 24H' and three feature rows, each with a thin line icon and short label: '24h cold / 12h hot', 'Leak-proof bamboo lid', 'BPA-free 18/8 steel'. Thin callout lines from the labels to the lid and body. Sans-serif typography, high contrast, readable on mobile, generous whitespace, premium minimal brand style. Spell all text exactly as given.
```

## 05-xhs-cover.png

```text
Xiaohongshu (RED) note cover, 3:4 portrait. {IDENTITY_LOCK} Bright airy flat-lay on a cream linen tablecloth: the bottle lying diagonally with a sprig of mint, sliced lemon, a pair of sunglasses and a gym towel. Large bold Chinese headline at the top in a rounded friendly font: '一整天都冰的水杯' and a smaller tag below: '通勤 · 健身 · 露营'. A small hand-drawn style circle sticker in the corner reading '亲测24h'. Fresh, cozy lifestyle aesthetic, soft natural window light, high saturation but natural, eye-catching, text clearly legible, product sharp.
```

## 06-sale-banner.png

```text
Ecommerce sale banner, wide 3:2 landscape for a Shopee / TikTok Shop store front. {IDENTITY_LOCK} Three bottles of the same product in a row on a sage-green podium (the middle one larger), splash of ice cubes and water droplets frozen mid-air, background a vivid gradient from deep teal to warm orange with subtle confetti. Left side big bold text '11.11 MEGA SALE', below it 'UP TO 50% OFF' and a rounded button shape reading 'SHOP NOW'. Commercial advertising style, punchy lighting, crisp, all text spelled exactly.
```

## input-hoodie.png

```text
Plain overhead flat-lay smartphone photo of a real garment on a light grey bedsheet: a sage-green oversized cotton hoodie with kangaroo pocket, drawstrings with matte black tips, ribbed cuffs and hem, a small white embroidered wordmark 'AURA' on the left chest. Even daylight, slightly wrinkled, honest amateur product photo, photorealistic.
```

## 04-model-tryon.png

```text
On-model ecommerce photo. GARMENT IDENTITY LOCK: the exact hoodie from the reference — sage-green oversized cotton hoodie, kangaroo pocket, drawstrings with matte black tips, ribbed cuffs and hem, small white embroidered 'AURA' wordmark on the left chest; keep colour, fit, details and logo placement identical. Dress a natural-looking East Asian female model in her mid-20s in this hoodie with light-wash straight jeans and white sneakers, relaxed standing pose, one hand in the pocket, three-quarter view, full body. Plain warm light-grey studio backdrop, soft key light, catalog photography, realistic fabric texture and folds.
```
