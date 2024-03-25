import requests
from urllib import request

vidoeo_n=5 #影片數
'''
例子 https://www.douyin.com/user/MS4wLjABAAAADaWLkULZNGROordjpRjKq7x0JJ58gQQpk9WxkF1lbWw
先按一條片進去, F12開控制台, 選MEDIA, 找出影片, 找出關鍵字, 例如影片https://www.douyin.com/video/7349852114576772406
https://v3-web.douyinvod.com/4ebdefa7c46b05574b575bbdb5c105a7/66019d07/video/tos/cn/tos-cn-ve-15/oI3tipM2RDG9YfP1CuA5mf8eA23kXEHEbAVofA/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=397&bt=397&cs=2&ds=6&ft=YZkApY0071_vvjjF-wUCn.5yW.CoMbx0P-IpiX&mime_type=video_mp4&qs=11&rc=OTYzZ2k1ZGY3NmU7OWk6ZEBpamZsamc6Zjt4cTMzNGkzM0AuLy0yMmAxXy8xXmFeXjEwYSNuYW8ucjRnaXNgLS1kLTBzcw%3D%3D&btag=e00028000&cquery=100a_100w_100B_100x_100z&dy_q=1711378048&feature_id=9bcd3da4752f92402ca306ab9cd46f9b&l=20240325224728DBFC47FEDB3DCF1A07A7
上面的關鍵字是oI3tipM2RDG9YfP1CuA5mf8eA23kXEHEbAVofA
再回去上面例子user的網址
找這關鍵字
找到是下面requests的連結
對相關項目右鍵COPY->CURL，放去curlconverter得到相關的header和cookie
再觀察JSON去提取影片
'''
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
    'cookie': 'XXXXX'
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAADaWLkULZNGROordjpRjKq7x0JJ58gQQpk9WxkF1lbWw',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAADaWLkULZNGROordjpRjKq7x0JJ58gQQpk9WxkF1lbWw&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-TW&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=0&webid=7332920781460014629&msToken=out9DM4tnRyuJaJtO4Uy7oYItzY3SaXgno4kRLV59izxPhr6QqOu_h1MyKQZc4FUSqfiWGXvKprvhBgXe7yysAjpaOR-aNZTLyD18lcMrRi40LZ2hf0WymA=&X-Bogus=DFSzspjOIOvANS/qt-XQoaD31nl/',
    headers=headers,
)


n=0
json_text=response.json()
# print(json_text)
video_data=json_text['aweme_list']
for i in video_data:
    desc=i['desc']
    aweme_id=i['aweme_id']
    link='https://www.douyin.com/video/7349852114576772406'+aweme_id
    video=i['video']['play_addr']['url_list'][0]  #下載網址
#     request.urlretrieve(video,r'videos\\'+aweme_id+desc+'.mp4')   #下載用的
    print(desc, link, video)
    n=n+1
    if n>=5:break
    
