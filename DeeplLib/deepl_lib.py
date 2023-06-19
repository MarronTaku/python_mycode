import deepl
import json

def load_setting():
    """設定ファイルを読み込む
    """
    global master_data, translator

    # デフォルトの設定
    master_data = {
        "auth_key": "",
        "source_lang": "JA",
        "target_lang": "EN"
    }

    # 設定ファイルがあれば読み込む
    try:
        with open("config.json") as fp:
            update_data = json.load(fp)
        for k, v in update_data.items():
            master_data[k] = v
    except Exception as e:
        pass

def translate(source: str):
    """翻訳

    Args:
        source (str): 翻訳元のテキスト
    
    Returns:
        result (str): 翻訳結果のテキスト
    """
    translator = deepl.Translator(auth_key=master_data["auth_key"])
    result = translator.translate_text(
        source,
        source_lang=master_data["source_lang"],
        target_lang=master_data["target_lang"])
    
    return result

def main():
    load_setting()
    translate("This is a pen.")

if __name__ == "__main__":
    main()