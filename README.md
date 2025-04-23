# FastAPI 開発環境セットアップガイド

このプロジェクトは、FastAPI を利用した Python アプリケーションの開発環境を提供します。開発環境は Docker Compose を利用し、Poetry によるパッケージ管理を行っています。

---

### 📂 プロジェクト構造

```
.
├── app
│   └── main.py
├── .devcontainer
│ └── devcontainer.json
├── .vscode
│ └── launch.json
├── compose.yaml
├── Dockerfile
├── pyproject.toml
└── poetry.lock
```

---

### 🚀 クイックスタート

1. 開発環境の起動（VSCode 推奨）

   1. Visual Studio Code でプロジェクトを開きます。
   1. 拡張機能 Dev Containers がインストール済みであることを確認してください。
   1. コマンドパレット(Cmd⌘/Ctrl + Shift + P)から以下を実行します。

   ```
   Dev Containers: Get Started with Dev Containers
   ```

   これにより、自動的に以下の処理が実行されます。

   - Docker Compose を使用してコンテナをビルド
   - 必要な Python パッケージを Poetry でインストール
   - VSCode の拡張機能が自動的にインストールされます。

1. FastAPI アプリケーションの起動

   - 以下のコマンドで FastAPI サーバを起動できます。

   ```
   poetry run start
   ```

   - デバッグ付きで実行したい場合、`実行とデバッグ/デバッグの開始`を実行します

   ブラウザで次の URL にアクセスして、動作確認を行います。

   - http://localhost:8000

   Swagger UI

   - http://localhost:8000/docs

   ReDoc

   - http://localhost:8000/redoc

### 🛠️ 技術スタックと設定詳細

**Docker 環境**

- Python イメージ: python:3.13-bookworm

**Python パッケージ管理 (Poetry)**

- パッケージ設定は pyproject.toml を参照します。

**FastAPI**

- FastAPI バージョン: 0.110.0
- サーバ起動には Uvicorn (0.29.0) を利用します。
- 環境変数管理に python-dotenv を使用。

---

### ⚙️ コンテナ設定詳細

- 作業ディレクトリ : /workspace
- コンテナ内のユーザ: root
- フォワードポート : 8000 番ポート

---

### 📦 Docker Compose サービス定義

- コンテナ名: fastapi-app
- ポートマッピング: 8000:8000
- ホストとコンテナ間でソースコードを同期 (.:/workspace)
- 環境変数を.env ファイルから読み込みます（ファイルが存在する場合）。

---

### 💡 備考

- プロジェクトの環境変数は.env ファイルに記載します。
- 新規パッケージを追加する場合、`poetry add パッケージ名`をコンテナ内で実行します。
- pyproject.toml の変更後は、以下のコマンドで依存関係を再インストールします。

```
poetry install
```

---

以上でセットアップ完了です。快適な開発環境で FastAPI アプリケーションの開発を進めてください！
