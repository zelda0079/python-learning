import requests  # 運行前請看安裝 pip install requests
import re  # 運行前請看安裝 pip install re, 正則表達式
import pandas  # 運行前請看安裝 pip install openpyxl, pip install pandas, 處理EXCEL模組

table1=[]
pn=1 #開始第幾頁
count=1
#偽裝 看第13, 14行如何找user-agent, Accept-Language非必要

import requests

#https://xueqiu.com/hq/detail?name=%E6%B2%AA%E6%B7%B1%E4%B8%80%E8%A7%88&market=CN&first_name=0&second_name=0&type=sh_sz
#行情->行情中心->沪深一览

while True:
    
    cookies = {
        'xq_a_token': '76d4e5ee97f60e0be2c9b6c094156d577fba5c5b',
        'xqat': '76d4e5ee97f60e0be2c9b6c094156d577fba5c5b',
        'xq_r_token': '2537d01490f74c00d7d4a37578ac84f1b7481ca1',
        'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxMTA2ODM4MiwiY3RtIjoxNzA4NTczMjI4NzExLCJjaWQiOiJkOWQwbjRBWnVwIn0.MPsrKHTH9WCWBVyK_VnCnVuPnZUJudqj2RBaL4v9SSo1vQjaRCB4c1sByQXoDdyzutMe1wTYUMOiI0LnFYi0yR4NGQYsNGEihmbz22E47rD_F1weFHzj5jTtRVZaFh4A13Z20uwpzEDHppni6CF5Ya1LyWNhu0_aCTj12lZy9cjNMkD30k-9zplFaLlzFp8cTqfr4xKOl3uYgs7dsvZphGYP2QGzGVj-34Ycjjn_WZygoEJqKL0CoUQK6mKAByWTcUgV2FWYsEeafg7iMYBcwYI0bwrIt_SfQB9RorbbpZP6djQkFlp8Tpk_frFxhtn9KLNNzaqr-2XuxsPFAoISMQ',
        'cookiesu': '381708573281478',
        'u': '381708573281478',
        'device_id': '9d43ff4896898ab327099451c7aaffd5',
        'is_overseas': '0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
        'Connection': 'keep-alive',
        # 'Cookie': 'xq_a_token=76d4e5ee97f60e0be2c9b6c094156d577fba5c5b; xqat=76d4e5ee97f60e0be2c9b6c094156d577fba5c5b; xq_r_token=2537d01490f74c00d7d4a37578ac84f1b7481ca1; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxMTA2ODM4MiwiY3RtIjoxNzA4NTczMjI4NzExLCJjaWQiOiJkOWQwbjRBWnVwIn0.MPsrKHTH9WCWBVyK_VnCnVuPnZUJudqj2RBaL4v9SSo1vQjaRCB4c1sByQXoDdyzutMe1wTYUMOiI0LnFYi0yR4NGQYsNGEihmbz22E47rD_F1weFHzj5jTtRVZaFh4A13Z20uwpzEDHppni6CF5Ya1LyWNhu0_aCTj12lZy9cjNMkD30k-9zplFaLlzFp8cTqfr4xKOl3uYgs7dsvZphGYP2QGzGVj-34Ycjjn_WZygoEJqKL0CoUQK6mKAByWTcUgV2FWYsEeafg7iMYBcwYI0bwrIt_SfQB9RorbbpZP6djQkFlp8Tpk_frFxhtn9KLNNzaqr-2XuxsPFAoISMQ; cookiesu=381708573281478; u=381708573281478; device_id=9d43ff4896898ab327099451c7aaffd5; is_overseas=0',
        'Origin': 'https://xueqiu.com',
        'Referer': 'https://xueqiu.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'page': f'{pn}',
        'size': '90',
        'order': 'desc',
        'order_by': 'percent',
        'market': 'CN',
        'type': 'sh_sz',
    }

    response = requests.get(
        'https://stock.xueqiu.com/v5/stock/screener/quote/list.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    josn_data=response.json()
    #print(josn_data['data'])
    if josn_data['data']=={}:
        print("finish")
        break
    data_list=josn_data['data']['list']
    for i in range(0,len(data_list)):
        symbol=data_list[i]['symbol']
        stock_name=data_list[i]['name']
        stock_percent=data_list[i]['percent']
        stock_current=data_list[i]['current']
        table1.append([count, symbol, stock_name, stock_percent, stock_current])  #合併成1個LIST
        count+=1
    pn +=1
    print(pn)
    
table2=pandas.DataFrame(table1)  
#print(table2)

table2.to_excel('stock_xueqiu.xlsx',index=False , header=['順序', '股號', '公司名', '漲跌百分比', '現價'])



