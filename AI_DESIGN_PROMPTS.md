# AIデザイン生成用プロンプト集（10案）

Google Stitch（Web / Thinking）／ GPT image 2.0 ／ Gemini（nano banana）に投入する用。
各案ごとに「共通指示」＋「方向性別プロンプト」をまとめてコピペできるようにしてある。

**使い方の基本**
- Stitch：Web モードで Thinking ON。「方向性別プロンプト」をそのまま投入。
- GPT image 2.0：「Hero／Services／Strength の3カット」のキービジュアル生成に使う。文章は英語＋日本語混在で。
- Gemini nano banana：FVのキービジュアル画像 or ムードボード用。
- いずれもロゴ画像（`assets/images/会社ロゴ 反転透過-450x100pix-300dpi.png`）を一緒にアップロードすると精度が上がる。

---

## 共通指示（毎回必ず先頭に付ける）

```
You are designing the corporate website for "TS Industry Co., Ltd." (株式会社ティーエスインダストリー), a 30-year-old Japanese precision-engineering company in Nagoya. They make Thomson dies (抜き型／木型) and provide waterjet cutting services. 25 employees. Two offices: Nagoya HQ + Kanagawa sales office. Their unique technologies: CA Blade, Un-Affect System, DP2 stainless.

Audience: Procurement / engineers at Japanese factories, browsing during work hours. They need to grasp the company in 3 seconds.

Target tagline (Japanese / English):
- 精度で、信頼を刻む。
- Precision beyond expectation.

==== ABSOLUTE DESIGN RULES — DO NOT BREAK ====

DO:
- Two-color palette only: one dominant color + one accent. No more.
- Use real photographs of factories, machined surfaces, raw materials. No stock illustrations.
- Display the company essence in 3 seconds at the fold: what they do, what's special, scale.
- Editorial design: thin rules, numbering, captions, small English labels for rhythm.
- Pair a serious display font with body fonts. Never use Inter alone.
- Quiet motion only. Tiny hover transitions (0.2-0.4s) and gentle scroll fades. Nothing else.
- Generous whitespace.
- Sharp edges (border-radius 0-2px).
- Bold large Japanese headings. Mix kanji-heavy display type with English meta labels.

DO NOT:
- No icons (no gears, wrenches, factory pictograms, no 3-column "speed/quality/trust" feature blocks).
- No colorful palette. No purple gradients, no rainbow accents, no pastels.
- No abstract particle / glowing-mesh / 3D gear / data-grid CG. These scream "AI-generated".
- No flashy animations or "look at me" motion. The user is at work, not playing.
- No template-style hero (blue gradient + smiling stock person + factory icon).
- No pill-shaped buttons. No deep rounded corners.
- Do not present water-jet as secondary to die-board. Treat them as equal.
- Do not look amateur (personal-portfolio vibes). Do not look AI-generated.

==== SITE STRUCTURE (top page sections) ====
1. Hero (100vh) — bold Japanese headline + English meta + 1-2 numbers + clean CTA
2. Services — Thomson Die / Waterjet, equally weighted, real photos
3. Strength — "the place to call when other-maker dies fail"; editorial-style
4. Technology — CA Blade / Un-Affect System / DP2 stainless, with photos & specs
5. Numbers — 30+ years / 2 offices / 500+ clients / 0 complaints
6. Recruit teaser
7. CTA — contact + phone number

Header: logo left, simple nav right (Services dropdown / About / Recruit / Contact). No floating, always-visible.
Footer: dark, 4 columns, dense info, no decoration.
```

---

## 案 01 — Industrial Editorial（編集記事のような重量感）

**支配色 #0B1224（ダークネイビー）／アクセント #FF6B00（オレンジ）／日本語=Noto Serif JP／欧文=Manrope**

```
Direction: "Industrial Editorial". Imagine if a serious financial-news magazine and a precision factory had a baby.

Palette:
- Dominant: dark navy #0B1224 (background)
- Accent: orange #FF6B00 (only on tiny labels and one CTA button)
- Text: #E2E8F0 / Sub: #94A3B8

Typography:
- Japanese display: Noto Serif JP (Mincho), weight 700-900, very large for headlines (kerned tight)
- English display: Manrope ExtraBold, all-caps, wide letter-spacing for section labels (e.g. "01 / SERVICES")
- Body: Noto Sans JP 400, generous line-height
- Mono: Roboto Mono only for spec lines and numbers

Hero:
- 100vh, dark navy background with extremely subtle CAD grid (1px dots, 4% opacity)
- Top-left: small English meta "30 YEARS OF PRECISION — NAGOYA, JAPAN"
- Center-left: huge Japanese mincho headline "精度で、信頼を刻む。" 
- Below it: smaller English in Manrope "Precision beyond expectation."
- Bottom-left: 3 inline metrics in mono: "EST. 1995 / 25 STAFF / 500+ CLIENTS"
- Bottom-right: a single orange-text link "事業を見る →" (no button, just text)
- No imagery in hero. Just typography on dark.

Services section:
- Two large rectangular blocks side-by-side, equal size
- Each has a real photo (factory machinery for Thomson Die / water-jet stream for Waterjet) at the top
- Below: small English caption "01 / DIE BOARD MANUFACTURING" and "02 / WATERJET CUTTING"
- Then large Japanese serif title and 2 lines of body
- A thin orange underline appears on hover. No icons.

Editorial elements throughout:
- Numbered sections (01, 02, 03) in mono on the left margin
- Hairline rules between sections (1px, #1E293B)
- Pull-quotes set in Mincho italic for the "駆け込み寺" message
- Captions under photos in mono, like a print magazine

Motion: only fade-up on scroll (0.6s ease-out, opacity + 12px translate). Nothing else.

Forbidden in this direction: anything cyan/blue accent, any rounded card, any icon, any 3-up feature grid.
```

---

## 案 02 — Precision Black（黒一色×加工面マクロ写真）

**支配色 #0A0A0A（ピュアブラック）／アクセント なし（白のみ）／日本語=Shippori Mincho B1／欧文=Inter Tight**

```
Direction: "Precision Black". An Awwwards-style cinematographic black-only site. Total visual restraint, total photographic power.

Palette:
- Dominant: pure black #0A0A0A
- Accent: pure white #FFFFFF only
- No third color anywhere

Typography:
- Japanese display: Shippori Mincho B1 (very elegant high-contrast Mincho), weight 800
- English: Inter Tight, weight 700, very tight letter-spacing
- Mono: not used

Hero:
- 100vh, full-bleed extreme-close-up macro photograph of a freshly-cut metal edge (Thomson die blade), shot under raking light, mostly dark with one bright highlight
- Top-left: small white text in mono-ish caps "TS INDUSTRY"
- Bottom-left: three lines, large Mincho white text, set tight:
  「精度で、」
  「信頼を刻む。」
- No CTA button in hero. Instead, a subtle white text link with an underline "事業を見る" at the bottom.

Services:
- Full-screen-height alternating layout (each block 100vh)
- Block 1 (Die Board): full-bleed macro photo of paper being cut by a die, on the left half. On the right half, deep black with one large "01" in light gray and the title.
- Block 2 (Waterjet): mirror layout, with a high-shutter-speed photo of waterjet cutting metal, water droplets frozen in air.
- Each block has just three pieces of text: number / title / a single sentence.

Other sections:
- Strength: pure black with one large mincho quote centered, with hairline rules above and below.
- Technology: each technology has its own viewport-height block with one product photo and minimal text.
- Numbers: enormous white digits on black, one per row, with small mincho captions underneath.

Motion: only the photographs fade in slowly (1.2s) on scroll. Text appears instantly. No parallax. No icons anywhere.

Inspiration mood: Hiroshi Sugimoto, Apple's "Shot on iPhone" black series, an architectural photography monograph.
```

---

## 案 03 — Field Documentary（工場ドキュメンタリー誌）

**支配色 #1A1A1A（チャコール）／アクセント #C33A2C（赤朱）／日本語=源ノ角ゴシック Bold／欧文=IBM Plex Sans**

```
Direction: "Field Documentary". A long-form Brand Documentary magazine like Monocle or works that look at industry seriously. Photographs of people and process matter as much as the product.

Palette:
- Dominant: charcoal #1A1A1A
- Accent: dark vermilion #C33A2C (used for one section divider and one button only)
- Text: #F2F2F0 / Sub: #B8B8B5

Typography:
- Japanese display: 源ノ角ゴシック (Source Han Sans) Heavy / Bold, modern industrial-feeling sans
- English: IBM Plex Sans for headings, IBM Plex Sans Condensed for small caps labels
- Body: Noto Sans JP 400, slightly looser tracking

Hero:
- 100vh, autoplaying muted video of a factory floor — workers in motion, sparks, a die press at work, water-jet cutting through metal — high-contrast color-graded toward charcoal/vermilion
- Bottom band: black overlay 40%, with bold gothic headline "現場が答えだ。" plus English subtitle "The shop floor has the answer." 
- Top-right: small caps "EST. 1995 / NAGOYA" in IBM Plex Sans Condensed

Services:
- Two large editorial spreads, scrolling vertically
- Left page: a worker's hands holding a die, B&W
- Right page: large headline "抜き型／木型" + a 200-word essay-like description
- Drop cap on first paragraph (vermilion)

Strength:
- A full-width testimonial-style block: huge serif quote-marks, 3-line italic quote about being the "駆け込み寺" for problem dies, below it a name and role of an imagined customer (or anonymized).

Technology:
- Each technology gets a full editorial page with: full-bleed photo, title, hand-drawn caption arrows pointing to detail (faked with css), specs in a small table.

Numbers:
- A table-like block with hairlines and large mono numerals.

Motion: only video plays in hero. Scroll gives gentle fade. Hover on links shows a thin vermilion underline drawing left-to-right.

No icons. No 3-card grids. The whole site should feel like a printed industrial documentary that happens to be on screen.
```

---

## 案 04 — Technical Whitepaper（白基調・論文風・極めて静か）

**支配色 #F8F7F2（ウォームオフホワイト）／アクセント #111（インクブラック）／日本語=Noto Serif JP／欧文=IBM Plex Mono + Inter**

```
Direction: "Technical Whitepaper". This is an academic/engineering whitepaper translated to the web. Cool, precise, almost no decoration. The reader's job is to read.

Palette:
- Dominant: warm off-white #F8F7F2 (background)
- Accent: ink black #111 (text and one underline color)
- Sub: gray #6B6B68
- Hairlines: #D8D5CD

Typography:
- Japanese display: Noto Serif JP, weight 600 (not too heavy)
- English headings: Inter, weight 600, sentence-case
- Mono: IBM Plex Mono for all numbers, dimensions, dates, labels
- Body: Noto Sans JP 400, comfortable for long reading

Hero:
- 80vh (intentionally less than 100vh — restraint), warm off-white background, NO photo
- A single tight column, max-width 720px, left-aligned
- Pre-title in mono small caps: "TECHNICAL OVERVIEW · v.2026"
- Then a hairline rule
- Title: "精度で、信頼を刻む。" in Mincho, large but not enormous
- Subtitle in Inter italic: "Precision Engineering for Thomson Dies and Waterjet Cutting"
- Below: a 4-row "abstract" block formatted like a paper:
  EST.        — 1995
  STAFF       — 25
  CLIENTS     — 500+
  COMPLAINTS  — 0 (since 2018)

Sections look like:
"§01 Services"
"§02 Strength"
"§03 Technology"
Each section has a numbered heading in mono, a hairline rule, and the content below.

Photographs are used very sparingly: a single black-and-white image per section, with a numbered caption beneath: "Fig. 01 — CA Blade tooth profile, ×40 magnification".

Footer: a sober single-row layout with a tiny address block and copyright in mono.

Motion: nothing more than text fading from 0 to 100% opacity over 0.4s when scrolled into view. Nothing flashy.

No icons. No buttons with rounded corners (use text links with underline-on-hover). No third color. The result must feel like an IEEE paper that happens to be a website.
```

---

## 案 05 — Heritage Modern（紙テクスチャ＋朱印アクセント）

**支配色 #EFE9DC（アイボリー紙色）／アクセント #B33A2A（朱印赤）／日本語=解ミン宙／欧文=Cormorant Garamond**

```
Direction: "Heritage Modern". A 100-year-old craft house meets contemporary editorial. Paper texture, traditional Japanese seals, almost a museum-catalog feeling — but unmistakably modern in layout.

Palette:
- Dominant: ivory paper #EFE9DC (with a very subtle fiber/grain texture overlay)
- Accent: vermilion seal red #B33A2A (used as a literal red square seal stamp in 2-3 places only)
- Text: sumi black #1A1714
- Sub: faded ink #5C5752

Typography:
- Japanese display: 解ミン 宙 or 砧 アンチック Std (a refined modern Mincho with calligraphic feel)
- English display: Cormorant Garamond, italic for accent
- Body: Noto Sans JP 400
- Mono: not used

Hero:
- 90vh, ivory background with a barely-visible washi-paper grain texture
- Top-right corner: a small red square "印" seal with the company kanji or initials
- Center-left: vertical-orientation Japanese type — "精度で、信頼を刻む。" set vertically, Mincho 200pt-equivalent
- Below: in Cormorant italic, "Precision beyond expectation, since 1995."
- A single horizontal black hairline rule
- No photo in hero.

Services:
- Two large modules, side-by-side, each with a generous border of white space. 
- Each features a single dark, moody photo (factory shot, slightly desaturated, paper-like)
- Bilingual title: large Mincho on top, small Cormorant italic English below
- Body text reads like a museum object label — concise, descriptive, technical.

Strength:
- A pull quote in vertical Mincho, ridiculous size, with a red seal stamp at the top.

Technology:
- Three modules, each like a museum exhibit card. Photo + name + descriptive paragraph + a small red seal in the corner indicating "self-developed".

Numbers:
- A table set in Mincho. 30, 2, 500+, 0. Very large. Captions in small Cormorant italic.

Footer: ivory background with a darker ivory border line, sumi-black text, almost like a colophon page in a book.

Motion: text fades in (0.5s). The red seal stamps appear with a tiny scale-bounce (110% to 100%) when scrolled. Nothing else.

This direction must NOT feel kitsch or cliché-Japanese. No cherry blossoms, no waves, no kanji watermarks. The Japaneseness should be in the typography and the seal stamp only, used with restraint.
```

---

## 案 06 — Steel & Concrete（鉄色・コンクリ質感のフルブリード）

**支配色 #2B2D31（鉄色）／アクセント #B8B8B8（銀）／日本語=Noto Sans JP 900／欧文=Manrope ExtraBold**

```
Direction: "Steel & Concrete". The site itself feels like the material the company works with. Rough textures, brutalist confidence.

Palette:
- Dominant: steel gray #2B2D31
- Surface: brushed-metal noise texture overlay (subtle)
- Accent: cool silver #B8B8B8 for links and one CTA outline
- Text: #ECECEC

Typography:
- Japanese display: Noto Sans JP 900 (very heavy)
- English display: Manrope ExtraBold, condensed feel
- Body: Noto Sans JP 400
- Mono: not used; numbers are in Manrope tabular

Hero:
- 100vh, full-bleed concrete or brushed-steel texture as the background (real photo of polished metal surface, very dark)
- Single huge headline center-left, set in Noto Sans JP 900: "精度で、信頼を刻む。" — the type is so heavy it looks like it was forged
- Below in tighter Manrope: "TS INDUSTRY · PRECISION ENGINEERING"
- No button, no link in hero. Just type and material.

Services:
- Two giant horizontal bands, each filling the viewport
- Each band uses a real high-resolution photo of the actual cutting surface (the die blade edge / the waterjet kerf) as a full-bleed background
- A 50% black overlay carries the type
- The transition between Service 1 and Service 2 is a hairline silver rule

Strength:
- Raw concrete-textured background with one massive Japanese headline. The "駆け込み寺" message reads like graffiti carved into concrete (set flat, no actual texture distortion).

Technology:
- Three columns separated by silver hairlines. Each shows a tightly-cropped material photo (CA blade tooth, DP2 stainless surface, Un-Affect mechanism) and a heavy heading.

Numbers:
- Single column. Each number is enormous, set in Manrope ExtraBold, white-on-steel. A tiny caption beneath.

Footer: even darker than the rest, almost black, silver text.

Motion: photos fade in (0.8s). Hover on links: a silver underline draws.

No icons. No softness anywhere. The site should feel like you're inside a precision-engineering plant.
```

---

## 案 07 — Spec Maximalism（数値が主役の巨大タイポ）

**支配色 #0B1224（ダークネイビー）／アクセント #00C7B7（サイアン）／日本語=Noto Sans JP 900／欧文=Space Grotesk**

```
Direction: "Spec Maximalism". The whole site is built around enormous numbers and specifications. The company's competence is communicated through quantities.

Palette:
- Dominant: deep navy #0B1224
- Accent: sharp cyan #00C7B7 for numbers and units
- Text: #E2E8F0
- Hairlines: #1E293B

Typography:
- Japanese display: Noto Sans JP 900
- English headings: Space Grotesk Bold (very characterful)
- Mono: JetBrains Mono for unit labels (mm, μm, kg/cm², °C)

Hero:
- 100vh, dark navy with a faint dot grid
- Layout: a large headline on top — "0.01 mm" — yes, JUST a number, in cyan, enormous (font-size: 14vw)
- Below it: small Japanese gothic "の精度で、信頼を刻む。" — making the meaning click
- To the right margin: a vertical column of specs in mono:
  "PRECISION   ±0.01mm
  THICKNESS   0.3-50mm
  MATERIALS   30+
  LEAD TIME   5 days"
- A single cyan-outlined CTA button: "事業を見る →"

Services:
- Side-by-side blocks, each headed by a giant number ("01" / "02") and a piece of stat:
  "01 — DIE BOARD / 500,000+ pcs/yr"
  "02 — WATERJET / 30+ materials"
- Body has a real photo and 2-line description.

Strength:
- 3 stat columns, each with a giant number and small explanation. Example: "0 — クレーム件数 (since 2018)"

Technology:
- Each technology shows specs like a datasheet:
  "CA BLADE
  Hardness ......... HRC 62
  Cutting life ..... 3× standard
  Lifespan ......... 24 mo+"
- Mono for the stats, gothic for the title.

Numbers:
- Spec-sheet table style. Generous spacing.

Motion: numbers count up (count-up animation) when scrolled into view. Subtle. 0.8s.

No icons. No third color. Cyan is used sparingly — only on numbers and units, plus one button.
```

---

## 案 08 — Catalog Card（製品カタログのWeb版）

**支配色 #ECE9E2（ウォームグレー）／アクセント #1A2A4F（ディープブルー）／日本語=Shippori Mincho B1／欧文=IBM Plex Serif**

```
Direction: "Catalog Card". The site reads like a high-end industrial product catalog (think Vitra, Hermès Industries, or a Japanese sangyō kyōkai catalog). Each product is treated as an object of design.

Palette:
- Dominant: warm gray paper #ECE9E2
- Accent: deep navy blue #1A2A4F
- Text: navy
- Hairlines: #BFB8A8

Typography:
- Japanese display: Shippori Mincho B1 (Bold)
- English headings: IBM Plex Serif (italic for subtitles)
- Body: Noto Sans JP 400
- Mono: IBM Plex Mono for product codes

Hero:
- 80vh, warm gray paper background
- Layout like a catalog cover: the company name in Mincho, large, top-left
- A small navy index "Vol. 30 — 2026" in mono small caps
- Center: a single hero photograph of one product (a polished CA Blade, lit beautifully against gray paper). About 60% of viewport width.
- Right of the photo: a poetic 3-line caption in Mincho, navy.

Services:
- Two products presented like catalog entries: photo on left, text on right with a clear "spec sheet" feel — name, code, description, dimensions, materials, applications.
- Hairline rules separate fields.

Strength:
- A "letter from the founder" style block. Mincho body, navy ink, signed at the bottom.

Technology:
- Three catalog-style entries, with photos and detailed specs. Each has a "Cat. No. CA-001 / UA-001 / DP2" code.

Numbers:
- A table on the inside-cover: "Founded — 1995 / Staff — 25 / Locations — Nagoya & Atsugi / Clients — 500+".

Footer: like a catalog colophon, tiny mono text, navy.

Motion: pages flip (subtle horizontal translate) on scroll between sections. Hover on products: photo subtly enlarges 102%.

No icons (instead, the product photo IS the visual). No bright accents. No 3-card icon grid. The whole site should feel like flipping through a beautifully-designed industrial catalog.
```

---

## 案 09 — Drafting Plan（図面・断面表記の引用）

**支配色 #F4F1EA（紙白）／アクセント #2A2A2A（グラファイト）／日本語=凸版文久ゴシック／欧文=JetBrains Mono + Inter**

```
Direction: "Drafting Plan". The site references engineering drawing conventions (without being literal blueprint imagery). Hairlines, dimension arrows in margins, section markers, drawing-sheet borders, callout numbers.

Palette:
- Dominant: drawing-paper warm white #F4F1EA
- Accent: graphite #2A2A2A
- Hairlines: #C8C2B4
- A single red-orange #D44A1F is used ONLY for dimension callouts and one CTA — sparingly.

Typography:
- Japanese display: 凸版文久ゴシック (a clean, modern technical-feeling gothic)
- English: Inter for headings, JetBrains Mono for all measurements
- Body: Noto Sans JP

Hero:
- 100vh, paper-white
- Around the edge of the viewport: a thin (1px) drawing-sheet border with corner registration marks (small + symbols)
- In the bottom-right corner: a "title block" like a real drawing sheet — TS Industry / Drawing No. 0001 / Scale 1:1 / Date 2026.04
- Center-left: a large headline in 凸版文久ゴシック "精度で、信頼を刻む。"
- Below in mono: "TOLERANCE ±0.01mm"
- Subtle dimension arrows pointing to the headline (using thin hairlines and small mono numbers)

Services:
- Each service block is treated as a "section view" — a drawing-style layout:
  - Section label: "SECTION A-A"
  - A real photograph in the center (like a detail callout)
  - Hairline arrows pointing to the photo with small mono labels: "PRECISION CUT", "CARBON STEEL", etc.
  - Below: title in gothic and 2-line description.

Strength:
- A "specifications" page with hairline-table layout: the "駆け込み寺" message broken into 3 numbered points, each with a graphite icon-less marker.

Technology:
- 3 detail-callout style entries, each with a photo, dimensions, and notes — like real engineering drawings.

Numbers:
- A "Bill of Materials" style table: number / unit / description.

Footer: the bottom drawing-sheet title block expanded. Address, contact, copyright.

Motion: when scrolled, hairline rules draw left-to-right. Dimension arrows fade in. Otherwise still.

No icons. No flat illustrations. The "drawing-ness" comes from layout conventions and hairlines only — never literal blueprint cyan or grid backgrounds.
```

---

## 案 10 — Quiet Showcase（圧倒的な余白×加工サンプル一点）

**支配色 #FBFBFB（スノーホワイト）／アクセント #0E0E0E（ダークインク）／日本語=Noto Serif JP Bold／欧文=Inter Tight**

```
Direction: "Quiet Showcase". The site is almost empty. Each section shows a single object photographed beautifully, and a few lines of text. Like an art gallery's website. Total restraint communicates total confidence.

Palette:
- Dominant: snow white #FBFBFB
- Accent: dark ink #0E0E0E
- Sub gray: #888 (used only for tiny captions)
- No third color.

Typography:
- Japanese display: Noto Serif JP Bold (Mincho)
- English: Inter Tight, weight 700, very tight
- Mono: not used (we want softness in the typography, not technicality)

Hero:
- 100vh, snow white
- Empty viewport except for: one small text in the bottom-left corner — "TS INDUSTRY"
- And one small navigation in the top-right
- The center is intentionally empty — there is nothing here.
- As the user scrolls, the first section appears.

First content section ("精度"):
- 100vh
- Center: a single beautiful, well-lit photograph of a precision CA blade tooth, taken on a white background. The photo is sized to about 40% of the viewport.
- To the right of the photo, a single line of Mincho: "精度で、信頼を刻む。"
- Below: in Inter italic, "Precision beyond expectation."
- No CTA. No button. Just the object and the words.

Each subsequent section uses the same pattern:
- 100vh
- One photograph centered, small to medium size
- One Japanese sentence
- One English sentence
- A tiny caption in gray underneath the photo

Numbers section:
- 100vh, white. Center: huge Mincho "30" with a small caption below "創業からの年数". Then scroll, "500+" with "取引先数". And so on.

Footer: an extremely sparse footer — just the company name in Mincho, address in tiny gray, and a hairline rule.

Motion: photos fade in (0.8s) on scroll. Text fades in 0.2s after. That's all.

This direction's risk: it can feel boring or insufficient. Compensate by making the photographs world-class, and by making the typography exceptionally well-set. There must be no laziness in the void — every detail in the empty pages must be perfect.

No icons. No background textures. No accent color. The site is the photographs and the words.
```

---

## 生成後のフォルダ整理

各案の v1 結果は以下に保存：
```
web/explorations/01_industrial_editorial/v1/{stitch.png, gpt.png, gemini.png, [stitch.html]}
web/explorations/02_precision_black/v1/...
...
```

`DESIGN_EXPLORATION.md`の進捗トラッカーをチェックし、Claudeに監修依頼。
