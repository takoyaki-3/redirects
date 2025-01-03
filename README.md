# URL Redirect Service

このサービスは、指定されたIDに基づいてURLリダイレクトを行うシンプルなWebアプリケーションです。Dockerコンテナ内で実行するように設計されており、`redirects.json` ファイルでリダイレクトルールを管理します。

## 特徴

* シンプルで軽量なURLリダイレクトサービス
* Docker Composeを使った簡単なデプロイ
* `redirects.json` による柔軟なリダイレクト設定
* 404エラーハンドリング

## プロジェクト構成

```
.
├── Dockerfile
├── app.py
├── docker-compose.yml
└── redirects.json
```

* **Dockerfile:** Dockerイメージの構築定義
* **app.py:** Flaskアプリケーションのソースコード
* **docker-compose.yml:** Dockerコンテナの起動設定
* **redirects.json:** リダイレクトルールのJSONファイル


## インストールと実行

1. **DockerとDocker Composeのインストール:** DockerとDocker Composeがシステムにインストールされていることを確認してください。

2. **リポジトリのクローン:** このリポジトリをクローンします。

   ```bash
   git clone <リポジトリURL>
   ```

3. **redirects.jsonの作成と編集:** リダイレクトルールを定義する `redirects.json` ファイルを作成します。以下は例です。

   ```json
   {
     "example": "https://www.example.com",
     "google": "https://www.google.com"
   }
   ```

   この例では、`/example` にアクセスすると `https://www.example.com` へ、`/google` にアクセスすると `https://www.google.com` へリダイレクトされます。

4. **Dockerコンテナの起動:** プロジェクトディレクトリで以下のコマンドを実行します。

   ```bash
   docker-compose up -d
   ```

5. **動作確認:**  `http://localhost:5246/<id>` にアクセスし、リダイレクトが正しく動作することを確認します。`<id>` は `redirects.json` で定義したキーに置き換えてください。例えば、`http://localhost:5246/example` にアクセスすると、`https://www.example.com` にリダイレクトされます。


## 環境変数

このアプリケーションでは環境変数は使用していません。


## APIエンドポイント

* `/ <id>`:  `id` に対応するURLへ302リダイレクトを行います。`id` が `redirects.json` に存在しない場合は、404エラーを返します。



## 設定ファイル

* **redirects.json:** リダイレクトルールを定義するJSONファイル。キーはリダイレクトID、値はリダイレクト先のURLです。


## コマンド実行例

* **Docker Composeによるコンテナ起動:**
    ```bash
    docker-compose up -d
    ```

* **Docker Composeによるコンテナ停止:**
    ```bash
    docker-compose down
    ```

* **Docker Composeによるコンテナ再構築:**
    ```bash
    docker-compose up --build -d
    ```


## ライセンス

このプロジェクトは、MITライセンスの下で配布されています。ライセンスの詳細については、LICENSEファイルを参照してください。
