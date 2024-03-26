import re
import requests                     
# from bs4 import BeautifulSoup

cookies = {
    XXXXX
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'XXXXXXXXX'
    'referer': 'https://live.douyin.com/600058894899',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
#上面隨便右鍵COPYCURL再拿去CURLCONVERT取得

url='https://live.douyin.com/921169302662'   #直播網址
res = requests.get(url, cookies=cookies, headers=headers)
html_text=res.text
# soup = BeautifulSoup(html_text, "html.parser")
# test=soup.find_all('script')[-3].prettify()
# print(test)


#觀察下方連結知道這3項是關鍵
sec_anchor_id=re.search('sec_uid\\\\":\\\\"(.*?)\\\\",\\\\"nickname', html_text)
roomId=re.search('roomId\\\\":\\\\"(.*?)\\\\",\\\\"web_rid', html_text)
anchor=re.search('anchor\\\\":{\\\\"id_str\\\\":\\\\"(.*?)\\\\",\\\\"sec_uid', html_text)

#F12找榜首的名字取得
url = f'https://live.douyin.com/webcast/ranklist/audience/?aid=6383&app_name=douyin_web&live_id=1&device_platform=web&language=zh-TW&enter_from=page_refresh&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-TW&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&webcast_sdk_version=2450&room_id={roomId[1]}&anchor_id={anchor[1]}&sec_anchor_id={sec_anchor_id[1]}&rank_type=30'

res = requests.get(url, cookies=cookies, headers=headers)
json_text=res.json()
# print(json_text)
all_user_data=json_text['data']['ranks']
for i in all_user_data:
    sec_uid=i['user']['sec_uid']
    link='https://www.douyin.com/user/'+sec_uid
    nickname=i['user']['nickname']
    pay_level=i['user']['pay_grade']['level']  #課金等級
    print(nickname, link, pay_level)
