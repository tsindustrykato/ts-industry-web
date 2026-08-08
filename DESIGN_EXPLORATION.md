# TS Industry サイト デザイン探索プロセス

10案 → 5案 → 1案の流れと、各案のスコアシート。
プロンプトは `AI_DESIGN_PROMPTS.md` を参照。

---

## ルール（毎回の評価基準）

`SITE_REQUIREMENTS.md §3「絶対ルール」`に照らして 5項目×4点満点 = 20点満点で採点する。

| 評価軸 | 4点 | 3点 | 2点 | 1点 |
|---|---|---|---|---|
| **A. AI感の不在** | 完全にプロが作った印象 | やや既視感あり | AIっぽさが残る | テンプレ感がはっきり |
| **B. 製造業BtoB適性** | 仕事中にパッと読める | 概ね読める | やや読みにくい | 装飾過多で見にくい |
| **C. 先進性 × プロ感** | 両立できている | どちらか強い | どちらも弱い | 個人サイト感がある |
| **D. ナビ明瞭性** | どこに何があるか即分かる | だいたい分かる | 探さないと分からない | 隠れていて困る |
| **E. ルール遵守** | アイコン・色数・モーション全て準拠 | 1項目軽微違反 | 2項目違反 | 多項目違反 |

**合格ライン：18点以上**で5案に進める。

---

## 10案の方向性（一覧）

詳細プロンプトは `AI_DESIGN_PROMPTS.md` を参照。

| # | コードネーム | 一言で | 支配色 | アクセント | 日本語フォント | 欧文フォント |
|---|---|---|---|---|---|---|
| 01 | **Industrial Editorial** | 編集記事のような重量感 | ダークネイビー #0B1224 | オレンジ #FF6B00 | Noto Serif JP（明朝） | Manrope |
| 02 | **Precision Black** | 黒一色×加工面マクロ写真 | ピュアブラック #0A0A0A | 白のみ | Shippori Mincho B1 | Inter Tight |
| 03 | **Field Documentary** | 工場ドキュメンタリー誌 | チャコール #1A1A1A | 赤朱 #C33A2C | 源ノ角ゴシック Bold | IBM Plex Sans |
| 04 | **Technical Whitepaper** | 白基調・論文風・極めて静か | オフホワイト #F8F7F2 | インクブラック #111 | Noto Serif JP | IBM Plex Mono + Inter |
| 05 | **Heritage Modern** | 紙テクスチャ＋朱印アクセント | アイボリー #EFE9DC | 朱 #B33A2A | 解ミン宙 | Cormorant Garamond |
| 06 | **Steel & Concrete** | 鉄色・コンクリ質感のフルブリード | 鉄色 #2B2D31 | 銀 #B8B8B8 | Noto Sans JP 900 | Manrope ExtraBold |
| 07 | **Spec Maximalism** | 数値が主役の巨大タイポ | ダークネイビー #0B1224 | サイアン #00C7B7 | Noto Sans JP 900 | Space Grotesk |
| 08 | **Catalog Card** | 製品カタログのWeb版 | ウォームグレー #ECE9E2 | ディープブルー #1A2A4F | Shippori Mincho B1 | IBM Plex Serif |
| 09 | **Drafting Plan** | 図面・断面表記の引用 | 紙白 #F4F1EA | グラファイト #2A2A2A | 凸版文久ゴシック | JetBrains Mono + Inter |
| 10 | **Quiet Showcase** | 圧倒的な余白×加工サンプル一点 | スノーホワイト #FBFBFB | ダークインク #0E0E0E | Noto Serif JP Bold | Inter Tight |

---

## 各案 進捗トラッカー

各案は `web/explorations/{番号}_{コードネーム}/` フォルダに保存していく。
`{番号}_v{バージョン}.png` のように世代を残す（再生成のたびにバージョンを上げる）。

### 01 Industrial Editorial
- [ ] v1 生成（Stitch / GPT image / Gemini）
- [ ] Claude監修コメント
- [ ] v2 生成
- [ ] スコア：A___ B___ C___ D___ E___ ／20

### 02 Precision Black
- [ ] v1 生成
- [ ] Claude監修コメント
- [ ] スコア：__/20

### 03 Field Documentary
- [ ] v1 生成
- [ ] スコア：__/20

### 04 Technical Whitepaper
- [ ] v1 生成
- [ ] スコア：__/20

### 05 Heritage Modern
- [ ] v1 生成
- [ ] スコア：__/20

### 06 Steel & Concrete
- [ ] v1 生成
- [ ] スコア：__/20

### 07 Spec Maximalism
- [ ] v1 生成
- [ ] スコア：__/20

### 08 Catalog Card
- [ ] v1 生成
- [ ] スコア：__/20

### 09 Drafting Plan
- [ ] v1 生成
- [ ] スコア：__/20

### 10 Quiet Showcase
- [ ] v1 生成
- [ ] スコア：__/20

---

## 5案絞り込み（記入欄）

最終5案：
1. ___
2. ___
3. ___
4. ___
5. ___

採用理由メモ：

不採用理由メモ：

---

## いいとこ取りメモ

案間で混ぜたい要素があればここに：

- 例：01のヒーロータイポ × 04の罫線情報設計
- 例：02のマクロ写真 × 09の図面風キャプション

---

## ワークフロー（毎回の手順）

### Phase 1：10案を一通り生成する
1. `AI_DESIGN_PROMPTS.md` から1案ぶんのプロンプトをコピー。
2. **Stitch（Web / Thinking）**、**GPT image 2.0**、**Gemini（nano banana）**のいずれかに投入。
   - Stitch：Webモードでの「画面デザイン」生成
   - GPT image 2.0／Gemini：FVのキービジュアル画像 or 概念ボード生成
3. 結果のスクショ／HTMLを `web/explorations/{番号}_{コードネーム}/v1/` に保存。
4. 上の進捗トラッカーにチェック。

### Phase 2：Claudeに監修依頼
新しいチャットで以下を貼る：
```
SITE_REQUIREMENTS.md と DESIGN_EXPLORATION.md を読んで。
案 ## の v1 を監修してほしい。スクショを添付するので、§3の絶対ルールと
DESIGN_EXPLORATION.md のスコア基準で5項目を採点し、悪い点を具体的に指摘して、
v2用の再生成プロンプト（差分指示）を出して。
```

### Phase 3：再生成 → 反復
監修コメントを基に再生成。スコア18点超えたら採用候補へ。

### Phase 4：5案に絞り、Claude Codeで実装
本番品質のHTMLを各案でトップページぶん作り、横並び比較で1案に絞る。

### Phase 5：1案で全ページ展開、納品
