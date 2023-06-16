import fitz

def extract_text_from_pdf(pdf_path: str, page_numbers: list, output_file: str) -> list:
    """PDFファイルからテキストを抽出して保存する

    Args:
        pdf_path (str): pdfファイルのパス
        page_numbers (list): 読み取りたいページ番号（0から始まるインデックス）
        output_file (str): 出力ファイル名

    Returns:
        texts (list): ページのテキストを要素とするリスト
    """
    texts = [] # ページのテキストを要素とするリストを格納するリスト
    doc = fitz.open(pdf_path) # PDFを読み込む
    
    # ページのテキストを抽出して保存、リストに格納
    with open(output_file, 'w', encoding='utf-8') as file:
        for page_number in page_numbers:
            page = doc[page_number]
            text = page.get_text()
            texts.append(text)
            file.write(text)
            file.write('\n--- Page Break ---\n')
    
    return texts

def main():
    # ページのテキストを抽出して保存
    texts = extract_text_from_pdf(
        pdf_path='1912.06218.pdf',
        page_numbers=[0],
        output_file='output.txt')
    print(texts)

if __name__ == "__main__":
    main()