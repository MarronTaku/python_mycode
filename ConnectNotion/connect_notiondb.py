import requests
from pprint import pprint
import json

def load_setting():

    # デフォルトの設定
    master_data = {
    "NOTION_ACCESS_TOKEN": "",
    "NOTION_DATABASE_ID": ""
    }
    try:
        with open("config.json") as fp:
            update_data = json.load(fp)
        for k, v in update_data.items():
            master_data[k] = v
    except Exception as e:
        pass

    return master_data

def get_notiondb_info(master_data):
    NOTION_ACCESS_TOKEN = master_data['NOTION_ACCESS_TOKEN']
    NOTION_DATABASE_ID = master_data['NOTION_DATABASE_ID']

    url = f'https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query'
    headers = {
        'Authorization': 'Bearer ' + NOTION_ACCESS_TOKEN,
        'Notion-Version': '2021-05-13',
        'Content-Type': 'application/json'
    }
    r = requests.post(url, headers=headers)
    data = r.json().get('results')

    return data

def save_data(data):
    file_path = "data.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def get_url_from_data(data):
    return data[0]['properties']['PDF']['files'][0]['file']['url']

def get_pdf_from_url(url):
    r = requests.get(url)
    with open("test.pdf", "wb") as file:
        file.write(r.content)

def main():
    master_data = load_setting()
    data = get_notiondb_info(master_data=master_data)
    url = get_url_from_data(data)
    get_pdf_from_url(url)

if __name__ == "__main__":
    main()