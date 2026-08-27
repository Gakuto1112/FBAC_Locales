言語: 　[English](./CONTRIBUTING.md)　|　**日本語**

# 翻訳の作業方法

## 翻訳方法

この章では、FBACアバターをお使いの言語に翻訳する方法を説明します。

### /src/index.json

- FBACアバターが作成中の翻訳データを正常に読み込めるように、`localeVersion`フィールドを、現行の翻訳データバージョンよりも高い値にしてください。
- `availableLocales`フィールドに追加する言語を、IDをキー、表示名を値として追加してください。
   言語IDはFiguraを導入したうえでゲーム内で以下のコマンドを実行すると取得できます：

   ```mcfunction
   /figura run print(client:getActiveLang())
   ```

   値はゲームの言語設定ページで確認できる名称を入力してください。
   括弧内の地域表記も忘れないでください。

   ![ゲームの言語設定ページ](./readme_images/locale_settings.jpg)

### /src/core/ および /src/avatars/

- 既存の翻訳データのjsonファイルをコピーし、ファイル名を"${対象の言語ID}.json"に変更し、中の訳文を全て対象の言語で翻訳してください。
- 上記作業を"[/src/core/](./src/core/)"および"[/src/avatars/](./src/avatars/)"内の全てのサブディレクトリ内に対して、繰り返し行なってください。

## ゲーム内での訳文の確認方法

実際にゲーム内で、アバターの言語表示を確認するには、ローカル環境上で翻訳データの配信サーバーを構築します。
ここでは[Python](https://www.python.org)ツールを用いた説明になりますが、Webサーバーを構築できるのであれば何を使用しても構いません。
なお、手順内にあるコマンド例はMac/Linux準拠になります。

1. カレントディレクトリを"/src/"に設定します。

   ```sh
   cd ${path_to_repository_root_directory}/src/
   ```

2. 以下のコマンドを入力してWebサーバーを起動します。

   ```sh
   python -m http.server 80
   ```

3. FBACコアの"[locale.lua](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/src/core/scripts/locale.lua)"を開き、`REMOTE_LOCALE_ENDPOINT`のURLをローカルサーバーのものに書き換えてください。

   ```lua
   local Locale = {
      ...
      REMOTE_LOCALE_ENDPOINT = "https://localhost/";
      ...
   }
   ```

4. FBACアバターをビルドし、手順3の変更がされたアバターを作成してください。
   FBACアバターのビルド方法は[こちら](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/build_scripts/README_jp.md)を参照してください。

5. ゲーム内のFigura設定で、ローカルサーバーのドメイン（`localhost`など）をネットワークフィルターの許可リストに登録するなどし、ローカルサーバーとの通信を許可してください。

6. もし以前の言語データをキャッシュしている場合は、[アクションホイールから言語データのキャッシュを削除](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/README_jp.md#アクション4-言語データの再読み込み)してください。
