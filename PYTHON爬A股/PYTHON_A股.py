import requests
import re
import pandas

table1=[]
pn=275
count=1
#偽裝 看第13, 14行如何找user-agent, Accept-Language非必要
hds={'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

while True:

    # 尋找方法: 去https://quote.eastmoney.com/center/gridlist.html#hs_a_board，按F12，NETWORK，放大鏡，找其中一個股票名字
    # 複製Request URL
    urls=f'https://57.push2delay.eastmoney.com/api/qt/clist/get?cb=jQuery11240509805259929021_1706240666685&pn={pn}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1706240666686'

    res=requests.get(url=urls, headers=hds)
    text1=res.text
    text2=res.status_code
    #print(text1)
    stock_num=re.findall('"f12":"(.*?)","f13"', text1)
    if not stock_num:
        break
    #print(stock_num)
    stock_name=re.findall('"f14":"(.*?)","f15"', text1)
    #print(stock_name)
    stock_up_precentage=re.findall('"f3":(.*?),"f4"', str(text1))
    #print(stock_up_precentage)
    stock_up=re.findall('"f4":(.*?),"f5"', text1)
    #print(stock_up)
    today_open=re.findall('"f17":(.*?),"f18"', text1)
    #print(today_open)
    yesday_close=re.findall('"f16":(.*?),"f17"', text1)
    #print(yesday_close)

    for i in range(len(stock_num)):
        #print(count, stock_num[i], stock_name[i], stock_up_precentage[i], stock_up[i], today_open[i], yesday_close[i] )
        table1.append([count, stock_num[i], stock_name[i], stock_up_precentage[i]+'%', stock_up[i], today_open[i], yesday_close[i]])
        count+=1
    pn +=1
    
    
    #if pn>=30000:
    #   break
    

table2=pandas.DataFrame(table1)
print(table2)
# pip install openpyxl
table2.to_excel('stock_test.xlsx',index=False , header=['順序', '股號', '公司名', '漲跌百分比', '漲跌', '今開', '昨收'])
