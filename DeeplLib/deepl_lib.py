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

def split_text(source_string: str) -> list:
    """テキストを5000文字ごとに分割する

    Args:
        source_string (str): 分割するテキスト
    Returns:
        sources (list): 分割したテキストのリスト
    """
    sources, tmp = [], []
    cnt = 0

    for s in source_string.splitlines(keepends=True):
        cnt += len(s)
        if cnt > 5000:
            sources.append("".join(tmp))
            tmp = [s]
            cnt = len(s)
        else:
            tmp.append(s)
    else:
        sources.append("".join(tmp))

    return sources

def translate(source: str) -> tuple:
    """翻訳

    Args:
        source (str): 翻訳元のテキスト
    Returns:
        result (str): 翻訳結果のテキスト
        message (str): メッセージ
    """
    # テキストの前処理
    sources = split_text(source)

    # DeepL APIを使って翻訳
    try:
        translator = deepl.Translator(auth_key=master_data["auth_key"])
        result = translator.translate_text(
            sources,
            source_lang=master_data["source_lang"],
            target_lang=master_data["target_lang"])
        usage = translator.get_usage()
        result_txt = "\n".join([r.text for r in result])
    except Exception as ex:
        return "", "DeepL translation error \n" + str(ex)
    
    # 翻訳結果の後処理
    message = ""
    # 翻訳ができた場合は、翻訳結果と文字数の使用状況を表示
    if message == "":
        return result_txt, f"Translate success. \nCharacter usage: {usage.character.count} of {usage.character.limit}"
    else:
        return result_txt, message

def main():
    load_setting()
    result_txt, message = translate("This is a pen.")
    print(result_txt)
    print(message)

if __name__ == "__main__":
    main()