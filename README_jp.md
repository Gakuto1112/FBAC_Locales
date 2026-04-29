言語: 　[English](./README.md)　|　**日本語**

# FBAC言語データレポジトリ

このレポジトリには、[Figura Blue Archive Crafters（FBAC）](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters)アバターで使用する言語データ（メッセージやUIで使用する訳文）が格納されています。
FBACアバターは、実行環境からこのレポジトリ内のリソースにアクセスし、ゲーム内でローカライズされたテキストを表示します。

## レポジトリのデータ構造

本レポジトリに格納されているデータは大きく分けて3つあります。

### index.json

「言語データのバージョン」や「対応している言語」の情報が記載されたファイルです。
FBACアバターはまずこのファイルを取得し、キャッシュを使用するのか、新たに言語データをダウンロードするのかを決定します。

`localeVersion`フィールドには、言語データのバージョンをセマンティックバージョニング（Semantic Versioning）で記載します。
先頭には必ず"v"を付けてください。
FBACアバターはキャッシュされた翻訳データのバージョンとこのフィールドを比較し、こちら側（リモート）バージョンが新しければキャッシュを廃棄し、りもーとから再読み込みするようになっています。

`availableLocales`フィールドには、対応している言語が、ゲーム内の言語IDをキー、言語の表示名を値とした、Key-Valueの形式で格納されています。
ゲーム内の言語IDは[Figura](https://modrinth.com/mod/figura)を導入し、下記コマンドを実行することで、現在の言語のものを取得できます：

```mcfunction
/figura run print(client:getActiveLang())
```

値はゲームの言語設定内での表示名になっています。
しかし、この値は現在使用していません。

![ゲームの言語設定ページ](./readme_images/locale_settings.jpg)

### src/core/

FBACアバターのコア部分に関する言語データが格納されています。
ファイル名は"${ゲーム内言語ID}.json"となります。
ゲーム内言語IDは"[index.json](#indexjson)"内で使用したものと同じです。

jsonファイル内は翻訳キー（メッセージID）をキーとし、訳文を値としたKey-Valueの形式で格納されています。

### src/avatars/

FBACアバターのアバター固有部分に関する言語データが格納されています。
キャラクターや[Exスキル](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/README_jp.md#exスキル)の名前の訳文もここに格納されています。
ディレクトリ内には、キャラクターのIDをサブディレクトリがあり、さらにそれらの中に"[src/core/](#srccore)"同様、言語データのjsonファイルが格納されています。
キャラクターサブディレクトリの命名規則は[FBACのキャラクター固有リソースのもの](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/build_scripts/README_jp.md#キャラクター固有部分)と同様です。
また、jsonファイルの命名規則 および ファイル内構造は"[src/core/](#srccore)"と同じです。
