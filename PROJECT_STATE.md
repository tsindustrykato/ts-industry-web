# TSIndustry サイト制作 - プロジェクト現状（2026-03-05時点）

## 完了済みタスク

### 基本構築
- [x] SWELLカスタム子テーマ `swell-child-tsindustry` 作成
- [x] Google Fonts（Sora + Noto Sans JP）読み込み
- [x] CSSカスタムプロパティ設計（カラー・フォント）
- [x] ナビゲーションメニュー構築（Services ドロップダウン付き）
- [x] フッター（4カラム：ロゴ・SERVICES・COMPANY・CONTACT）

### ページ実装（全6ページ）
- [x] **ホーム**（ID:7）: hero / strength / services / technology / recruit / CTA
- [x] **抜き型/木型**（ID:8）: hero / overview / products(6種) / workflow(4step) / CTA
- [x] **ウォータージェット**（ID:15）: hero / overview / features(4種) / materials(8種) / CTA
- [x] **会社概要**（ID:16）: hero / numbers / 会社情報テーブル / philosophy / access(2拠点)
- [x] **採用情報**（ID:17）: hero / message / positions(2職種) / CTA(entry)
- [x] **お問い合わせ**（ID:18）: hero / CF7フォーム / 電話セクション

### 機能
- [x] Contact Form 7 インストール・フォーム作成（ID:52）
  - フィールド: 名前*, 会社名, メール*, 電話, 件名*(select), メッセージ*
  - 管理者通知 + 自動返信メール設定済み
- [x] ファビコン設定（favicon.jpg, attachment ID:55）
- [x] wpautop無効化（サブページのカスタムHTMLが崩れる問題を修正）

### 画像最適化
- [x] PNG→JPEG変換（Python Pillow使用、1920px幅 quality:85）

### デザインv2大幅刷新（2026-03-05 Opus対応）
- [x] **カラーパレット全面変更:** ブルー系 → ダークネイビー×ゴールド軸
- [x] **キャッチコピー刷新:** 「精度で、信頼を刻む。」/ 「Precision beyond expectation」
- [x] **Intro → Strengthセクション:** 「品質と精度で選ばれる、抜き型の駆け込み寺」+ 3つの強み
- [x] **Technologyセクション刷新:** CAブレード / アン・アフェクトシステム / DP2ステンレス
- [x] **デザインディテール:** 角丸→シャープ(2px)、ボタン→エッジ(0px)、ゴールド上ボーダー統一
- [x] **ヒーロー:** 80vh → 100vh、スクロールインジケーター追加
- [x] **CTA:** ゴールドボタン、「他社製品のトラブルご相談」文言追加
- [x] **フッター:** ダークネイビー統一、カテゴリタイトルをゴールドに

### サブページv2リニューアル（2026-03-05 Opus対応）
- [x] **トップページ:** Numbersセクション削除（Aboutに移動）
- [x] **抜き型/木型:** Overview（ブランドメッセージ反映）+ Products 6カード（CAブレード/点字/彫刻刃/アン・アフェクトシステム/DP2ステンレス/リード罫）+ Workflow 4ステップ + CTA
- [x] **ウォータージェット:** Overview + Features 4カード（熱影響ゼロ/多素材対応/高精度CNC制御/試作・小ロット対応）+ Materials 8素材タグ + CTA
- [x] **会社概要:** Numbers統合（30年以上/2拠点/500社以上/0件）+ 会社情報テーブル + Philosophy（a concept is Speed + ブランド理念文）+ Access（2拠点 Google Maps）
- [x] **採用情報:** Message（代表メッセージ - ブランド価値反映）+ Positions 2職種（抜き型製造スタッフ/ウォータージェットオペレーター）+ CTA(Entry)
- [x] **お問い合わせ:** 「他社製の型でお困りの方もお気軽にご相談ください」追加 + フォーム + 電話セクション
- [x] **CSSバグ修正:** `.tsi-page-hero__overlay--solid` / `--accent` に `position: absolute; inset: 0;` 追加

## ブランド方向性（確定）

### コアバリュー
- 品質と精度が最優先。安易な価格競争には参加しない
- 顧客の現場での「圧倒的な使いやすさ」と「時短」を実現
- 「他社製の型でトラブルが起きたらTSindustryに相談しよう」と言われる駆け込み寺
- 独自素材: CAブレード / アン・アフェクトシステム / DP2ステンレス

### デザイントーン
- プレミアム × プロフェッショナル × 洗練された機能美
- 高度な技術力を感じさせるモダンデザイン
- 適切なホワイトスペース
- シャープなエッジ（丸みを抑えた精密感）

## カラーパレット v2

```css
--tsi-navy: #1A3A5C        /* メインカラー（ダークネイビー） */
--tsi-navy-deep: #0D1117   /* ヒーロー・フッター背景 */
--tsi-navy-light: #243B55  /* ホバー・アクセント */
--tsi-blue: #3B7DD8        /* インタラクション用サブカラー */
--tsi-blue-light: #EDF3FA  /* 薄いブルー背景 */
--tsi-gold: #C4944A        /* アクセントカラー（ゴールド） */
--tsi-gold-light: #D4A85C  /* ゴールドホバー */
--tsi-dark: #1A1A2E        /* テキスト */
--tsi-sub: #4A4A5A         /* サブテキスト */
--tsi-warm: #F7F8FA         /* 薄グレー背景 */
```

## トップページ構成 v2.1

```
Hero「精度で、信頼を刻む。」(100vh)
  ↓
Strength - 選ばれる3つの理由（妥協なき品質 / 圧倒的な使いやすさ / 信頼されるパートナー）
  ↓
Services（抜き型 / ウォータージェット）
  ↓
Technology（CAブレード / アン・アフェクトシステム / DP2ステンレス）
  ↓
Recruit（採用情報 - 4カードリンク）
  ↓
CTA（お問い合わせ - ゴールドボタン）
```

※ Numbersセクションはトップページから削除し、会社概要ページに移動済み

## サブページ構成 v2

### 抜き型/木型（/dieboard/）
```
Hero「妥協なき品質で、現場のトラブルをゼロにする」
  ↓ Overview（事業概要 - ブランドメッセージ + 駆け込み寺ポジショニング）
  ↓ Products（製品ラインナップ - 3×2グリッド 6カード）
  ↓ Workflow（製造フロー - 4ステップ横並び）
  ↓ CTA（TEL + お見積もり・ご相談）
```

### ウォータージェット（/waterjet/）
```
Hero「超高圧水流による精密切断で、あらゆる素材に対応」
  ↓ Overview（事業概要）
  ↓ Features（特長・強み - 2×2グリッド 4カード）
  ↓ Materials（対応素材 - 8素材タグ）
  ↓ CTA（TEL + お見積もり・ご相談）
```

### 会社概要（/about/）
```
Hero「会社概要」
  ↓ Numbers（30年以上 / 2拠点 / 500社以上 / 0件）
  ↓ Company（会社情報テーブル）
  ↓ Philosophy（企業理念 - a concept is Speed）
  ↓ Access（アクセス - 本社 + 神奈川営業所）
```

### 採用情報（/recruit/）
```
Hero「品質に妥協しない仲間を求めています」
  ↓ Message（代表メッセージ）
  ↓ Positions（募集職種 - 2カラム 2職種）
  ↓ CTA - Entry（TEL + 応募フォーム）
```

### お問い合わせ（/contact/）
```
Hero「お問い合わせ」
  ↓ フォーム（CF7 ID:52 - 他社製の型トラブル相談も歓迎）
  ↓ 電話セクション
```

## WordPressナビゲーション（メニューID:2）

```
Services（親、href=#）
  ├ 抜き型/木型（/dieboard/）
  └ ウォータージェット（/waterjet/）
About（/about/）
Recruit（/recruit/）
Contact（/contact/）
```

## 画像について

現在使用されている画像はすべてダミー（picsum.photos / Gemini nano banana生成）。
実際の写真は方向性確定後、社内撮影 or AI生成で差し替え予定。

## 今後のタスク（未着手）

- [ ] スマホ対応の確認・調整
- [ ] SEO基本設定（メタタイトル・ディスクリプション）
- [ ] 実際の写真の方向性決定 → 撮影 or 生成
- [ ] 会社概要の※プレースホルダーを実データに（代表者名・設立年月・資本金・従業員数）
- [ ] Numbers セクションの数値を実データに確定
- [ ] 電話番号プレースホルダー（052-XXX-XXXX）を実番号に差し替え

## 技術メモ

### SWELL子テーマ設定
```php
swell_meta_show_sidebar = 'hide'
swell_meta_no_mb = '1'
```

### 一時PHPスクリプトパターン
WordPressのDB操作は `wp-content/themes/` か `public/` に一時PHPファイルを作り
curlで実行 → 実行後即削除、という手順で行う。

### SWELLテーマ h2/h3 装飾リセット
```css
.page:not(.top) .post_content h2:where(:not([class^="swell-block-"])...) {
  background: none !important; padding: 0 !important;
}
```

### CSSバグ修正メモ
サブページヒーローのオーバーレイvariant（`--solid`, `--accent`）はベースクラス（`.tsi-page-hero__overlay`）の
プロパティを継承しないため、`position: absolute; inset: 0;` を直接記述する必要がある。
