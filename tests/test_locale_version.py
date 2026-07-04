import json
import os
from pathlib import Path
from typing import TypedDict
import unittest


class IndexJsonData(TypedDict):
    """
    `src/index.json`のデータ構造を表す型定義
    """

    localeVersion: str
    """
    ロケールデータのバージョン
    """

    availableLocales: dict[str, str]
    """
    利用可能なロケールの辞書型
    キー： ロケールのゲーム内部名称（例: "en_us"）
    値: ローケルの表示名(例: "English (United States)")
    """

class TestLocaleVersion(unittest.TestCase):
    tag_name: str|None = os.getenv("LOCALE_TAG_NAME")
    """
    比較を行うタグ（バージョン）の名前
    """

    def test_locale_version(self) -> None:
        """
        "src/index.json"内の`localeVersion`フィールドが、指定されたタグ名と一致することを確認する。
        """

        print(f"Target tag name: {self.tag_name}")

        if self.tag_name is None or len(self.tag_name) == 0:
            self.skipTest("Target tag name is not provided. Skipping locale version test.")

        index_path = Path("../src/index.json")

        if not index_path.exists():
            self.fail(f"\"src/index.json\" does not exist.")

        index_data: IndexJsonData = json.loads(index_path.read_text(encoding="utf-8"))

        locale_version = index_data.get("localeVersion")

        if locale_version is None:
            self.fail(f"Field \"localeVersion\" does not exist in \"src/index.json\".")

        self.assertEqual(locale_version, self.tag_name, f"Locale version mismatch detected.")

if __name__ == "__main__":
	unittest.main()
