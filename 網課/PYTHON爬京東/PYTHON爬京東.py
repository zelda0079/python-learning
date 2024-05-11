#PYTHON爬京東商品, 可能有反爬或奇怪的情況無法運作
#2024年1月30日, 京東1版(page1&2)有30個商店

import requests   #運行前pip install requests
import  lxml.etree  #運行前pip install lxml
import pandas  # 運行前請看安裝 pip install openpyxl, pip install pandas, 處理EXCEL模組
import urllib.parse  #中文KEYWORD轉網址文字用

data_total=[]
pn=1  #初始頁
pn2=10 #看你想要爬幾頁
count=1
pn2=pn2*2  #20即10版
# 京東搜索商品網址, 按F12, 找search, 第1條就是, 不過其實和你所在的網址差不多, 只是少一點參數
# 複製Request URL, User-Agent, Cookie
keyword1='筆記本'
keyword1=urllib.parse.quote(keyword1)
#print(keyword1)

while True:
    #注意網址page=pn
    url=f"https://search.jd.com/Search?keyword={keyword1}99&enc=utf-8&wq={keyword1}&page={pn}"

    hds={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Cookie':'你的Cookie'
         #'host'=''   #沒有用到
         #'referer'='' #沒有用到
        }

    res=requests.get(url, headers=hds)

    html_jd=lxml.etree.HTML(res.text)

    #對著店名右鍵>檢查, 會跳去Elements對應位置, 右鍵->copy->copy XPath
    #li表示第幾個商品, 以*的話就會輸入一堆商品進LIST
    store_name=html_jd.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[5]/span/a/@title')
    # print(store_name) #結果:['维达京东自营官方旗舰店']  (*=1的結果)
    price=html_jd.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[2]/strong/i/text()')
    # print(price) #沒有TITLE所以寫text(), 結果:['24.90']
    product_name=html_jd.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[3]/a/em/text()')
    #print(product_name) #沒有TITLE所以寫text(), 結果:['维达（Vinda）无芯卷纸 超韧4层140克12卷 加厚升级 卫生纸卷筒纸 纸巾卷纸']
    product_link=html_jd.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[3]/a/@href')
    # print(product_link) #沒有TITLE所以寫text(), 結果://item.jd.com/1131257.html
    img_link=html_jd.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[1]/a[1]/img/@data-lazy-img')
    # print(img_link) #沒有TITLE所以寫text(), 結果:['24.90']



    for i in range(len(price)):
        product_link[i]='https:'+product_link[i] #+HTTPS:
        img_link[i]='https:'+img_link[i]
        #print(store_name[i], price[i], product_link[i], img_link[i]) #測試數據
        data_total.append([store_name[i], price[i], product_name[i], product_link[i], img_link[i]])
        print(count)
        count+=1
        #print(data_total)
    
    pn+=2  #換另一版
    #print("doing"+str(pn))  #測試用
    if pn>pn2: #找幾版
        break

table1=pandas.DataFrame(data_total)
table1.to_excel('jd.xlsx',index=False , header=['商店名', '價格', '商品名', '鏈接', '圖片鏈接'])  #原地生成XLSX

