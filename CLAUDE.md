# TS Industry 静的サイト制作プロジェクト

このフォルダ（`web\`）はTS Industry（株式会社ティーエスインダストリー）のコーポレートサイト制作プロジェクトです。
このサブプロジェクトで作業する際は、このファイルと PROJECT_STATE.md を最初に読んでください。

> ワークスペース全体の構成は親フォルダの `..\CLAUDE.md` を参照。サイト制作は数ある作業の一つで、固有の内容はここに集約しています。

## 方針

- **WordPress不使用** — 完全な静的HTML/CSS/JSで構築
- 更新はClaude Codeに依頼する運用
- 完成ファイル一式はKH Design（管理会社）に渡してts-i.comにデプロイ

## 環境

- **作業ディレクトリ**: `D:\たぶんごみ\ClaudeCODE\web\`
- **ブラウザ確認**: Chrome拡張（Claude in Chrome）使用
- **デザインモック確認用**: `http://claudesitea.local/design-patterns-v4/`（Local by Flywheel）
- **本番ドメイン**: ts-i.com

## 主要ファイル

| ファイル | パス |
|---|---|
| Web作業フォルダ | `D:\たぶんごみ\ClaudeCODE\web\` |
| プロジェクト現状 | `D:\たぶんごみ\ClaudeCODE\web\PROJECT_STATE.md` |
| ロゴ画像 | `D:\たぶんごみ\ClaudeCODE\web\assets\images\` |
| デザインパターンv4 | `D:\たぶんごみ\ClaudeCODE\web\design-patterns-v4.zip` |
| 参照デザイン | `D:\たぶんごみ\ClaudeCODE\download\Image 2.html` |
| 新規チャット用プロンプト | `D:\たぶんごみ\ClaudeCODE\web\新規チャット用プロンプト.md` |

## 技術スタック

- Tailwind CSS（CDN版）
- Google Fonts: Inter, Noto Sans JP, Roboto Mono
- Material Symbols Outlined
- 各ページ: 単一HTML完結
- フォーム: 外部サービス（Formspree等）

## デザイン方向性

「Precision Archive」ベース — ダークネイビー(#0B1224) + オレンジ(#FF6B00) + ブルー(#135bec)
V4で6パターン作成済み → 方向性選定後、本番制作に入る

詳細な状態は PROJECT_STATE.md を参照。

## Frontend Design ガイドライン（frontend-design skill 相当）

フロントエンド制作時は以下に従い、generic な "AIっぽい" デザインを避け、独自性のある本格的なUIを構築する。

### Design Thinking

コーディング前に、コンテキストを理解し**大胆な美的方向性**を決定する：
- **Purpose**: このUIは何の問題を解決するか？誰が使うか？
- **Tone**: 明確なスタイルを選ぶ — brutally minimal, maximalist, retro-futuristic, luxury/refined, editorial/magazine, brutalist/raw, art deco/geometric, industrial/utilitarian 等
- **Constraints**: 技術要件（フレームワーク、パフォーマンス、アクセシビリティ）
- **Differentiation**: 何が「忘れられない」ポイントになるか？

**重要**: 明確なコンセプト方向を選び、精密に実行する。大胆なmaximalism も洗練されたminimalism もOK — 鍵は意図的であること。

### 美的品質基準

- **Typography**: 美しくユニークなフォントを選ぶ。Arial, Inter等の汎用フォントを避け、個性的な選択でデザインを引き上げる。Display font + Body font のペアリングを意識
- **Color & Theme**: 一貫した美的感覚にコミット。CSS変数で統一。支配的な色 + シャープなアクセントが、均等に分散された控えめなパレットに勝る
- **Motion**: アニメーションとマイクロインタラクションを活用。ページロード時のstaggered reveals（animation-delay）が散発的なmicro-interactionsよりインパクト大。scroll-triggerやhover statesで驚きを
- **Spatial Composition**: 予想外のレイアウト。非対称。オーバーラップ。対角線の流れ。グリッドを壊す要素。大胆なネガティブスペース or コントロールされた密度
- **Backgrounds & Visual Details**: ベタ塗りに逃げず、雰囲気と奥行きを作る。gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, grain overlays等

### NGパターン（避けるべきもの）

- 使い古されたフォント（Inter, Roboto, Arial, system fonts のみの使用）
- クリシェな配色（特に白背景に紫グラデーション）
- 予測可能なレイアウトとコンポーネントパターン
- コンテキスト固有の個性がない量産型デザイン
- 生成ごとに同じフォント（Space Grotesk等）に収束すること

### 実装指針

実装の複雑さを美的ビジョンに合わせる：
- Maximalist → 精巧なコード、豊富なアニメーション・エフェクト
- Minimalist/Refined → 抑制、精度、spacing・typography・繊細なディテールへの注意
- 創造的に解釈し、コンテキストに合った予想外の選択をする
- 同じデザインは二度と作らない。Light/Dark、異なるフォント、異なる美学を使い分ける
