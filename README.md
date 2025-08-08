# Streamlit Study

Streamlitを使ったWebアプリケーション開発の学習用プロジェクトです。

## 🚀 クイックスタート

### 1. リポジトリをクローン
```bash
git clone git@github.com:Kouta-i5/streamlit-study.git
cd streamlit-study
```

### 2. 依存関係をインストール
```bash
uv sync
```

### 3. アプリを起動
```bash
uv run streamlit run app.py
```

ブラウザで `http://localhost:8501` にアクセスしてアプリを確認できます。

## 📦 プロジェクト構造

```
streamlit-study/
├── app.py              # Streamlitアプリケーションのメインファイル
├── pyproject.toml      # プロジェクト設定と依存関係
├── uv.lock             # 依存関係のロックファイル
├── README.md           # このファイル
├── .gitignore          # Git除外設定
└── .venv/              # 仮想環境（uv syncで自動作成）
```

## 🛠️ uvによる環境管理

### uvとは
uvは高速なPythonパッケージマネージャーで、依存関係の管理と仮想環境の作成を効率的に行います。

### 主要ファイルの役割

#### **pyproject.toml**
- プロジェクト名、バージョン、Python要件、依存パッケージを宣言
- ツール設定（tool.uv セクション等）も記述可能

#### **uv.lock**
- すべての直接・間接依存を特定バージョンで完全固定
- 環境ごとに再現可能な状態を保持
- **手動編集は避け、必ずバージョン管理下に置く**

### パッケージ管理の流れ

#### **依存関係の追加**
```bash
uv add pandas numpy matplotlib plotly
```

#### **環境の同期**
```bash
uv lock    # ロック内容を再解決
uv sync    # .venvに内容を反映
```

#### **スクリプトの実行**
```bash
uv run python app.py
uv run streamlit run app.py
```

## 📱 Streamlitアプリの機能

このアプリには以下の4つのページがあります：

1. **テキスト表示** - 基本的なテキスト表示機能
2. **メディア** - 画像、動画、オーディオの表示
3. **インタラクティブ機能** - ボタン、チェックボックス、スライダーなどのUI要素
4. **データ入出力** - データフレーム、グラフ、CSV出力など

左側のサイドバーから各ページを選択して、Streamlitの様々な機能を試すことができます。

## 🔧 開発環境のセットアップ

### 1. uv initでプロジェクト初期化（新規プロジェクトの場合）
```bash
uv init streamlit-study
cd streamlit-study
```

### 2. 依存関係の追加
```bash
uv add streamlit pandas numpy matplotlib plotly pillow
```

### 3. 開発用依存関係の追加
```bash
uv add --dev pytest black flake8
```

### 4. 仮想環境のアクティベート（オプション）
```bash
source .venv/bin/activate
```

## 📚 参考リンク

- [Streamlit公式ドキュメント](https://docs.streamlit.io/)
- [uv公式ドキュメント](https://docs.astral.sh/uv/)
- [Python公式ドキュメント](https://docs.python.org/)

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成


