import requests
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  #SSL問題處理

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
all_mode=False   #是否要拿全部
page=1  #起始頁
page_end=1 #最後一頁
while True:
    if not all_mode:
        if page > page_end:
            print('爬蟲完成')
            break
    
    if page==1:
        url='https://www.ypppt.com/moban/'
    else:
        url=f'https://www.ypppt.com/moban/list-{page}.html'
    response = requests.get(url=url, headers=headers)
    # print(response.text)

    ids=re.findall('<a href="/article/.*?/(.*?)\.html"', response.text)
#     print(ids)
    if not ids:
        print('爬蟲完成')
        break

    count=0

    for id in ids:
        count+=1
        if count %2==0:
            continue
        url_ppt=f'https://www.ypppt.com/p/d.php?aid={id}'
        response = requests.get(url_ppt, headers=headers)
        download_url=re.findall('<a href="(.*?)">下载地址', response.text)
        file_name=re.findall('<title>(.*?)\s-\s下载页</title>', response.text)
        file_name_ext=download_url[0].split('.')[-1]
        file_name=f'{file_name[0]}.{file_name_ext}'
        print(download_url[0], file_name)
    #     response = requests.get(download_url[0], headers=headers, verify=False )
    #     with open(f'ppt\{file_name}','wb') as f:
    #         f.write(response.content)        #下載用命令
        print(f'已經下載{file_name}')
        
    page+=1

        