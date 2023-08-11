from pyquery import PyQuery
import requests
import json

def get_taipeispot_table(specific_key):
    #specific_key = input("請輸入景點名稱:")
    s = requests.session()
    s.headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    result = []

    for page in range(1,17):
        https = s.get(f"https://www.travel.taipei/open-api/zh-tw/Attractions/All?page={page}")
        table = json.loads(https.text)
        data = table['data']
        

        for x in data:
            if specific_key in x['name']:
                #print(f"景點名稱: {x['name']}  電話: {x['tel']}" + "\n" + f"地址: {x['address']}" )
                result.append(x)

    return result