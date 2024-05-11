import requests
import re


def get_pic(num):
    if not os.path.exists('pics'):
        os.makedirs('pics')

    cookies = {
        XXXXXX
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    #cookies和headers都用https://curlconverter.com/取得

    url=f'https://www.pkdoutu.com/article/list/?page={num}'
    res = requests.get(url=url, cookies=cookies, headers=headers)
    # print(res.text)
    imgurl=re.compile(r'data-original="(.*?)"')
    imgurl_list=imgurl.findall(res.text)
    for i in  imgurl_list:
        print(i)
        name=i.split('_')[-1]
        img=requests.get(url=i,  headers=headers).content
        open(f'pics/{name}','wb').write(img)
        print(f'<{name}>下載成功')

num=int(input('需要下載的頁數:'))
for j in range(num):
    num=num+1
    get_pic(num)


