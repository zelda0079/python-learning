import requests
import os.path

#爬全部需要登入帳號, 否則中間會出錯

host_url=input("請輸入博主網址:")  #https://www.kuaishou.com/profile/3xn4hjcuknfn269
userid=host_url.split('/')[-1]

#例子https://www.kuaishou.com/profile/3xn4hjcuknfn269

#以下單一下載的方法
# headers = {
#     'accept': '*/*',
#     'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
#     'origin': 'https://www.kuaishou.com',
#     'range': 'bytes=0-',
#     'referer': 'https://www.kuaishou.com/new-reco',
#     'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'video',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'cross-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
# }
# 
# params = {
#     'pkey': 'AAV4HzqN9AtL3Bnbto9WacJF2H2FIdfur7PnfJM0nkHd0eaFK_IYfJfv2zTe0rMKz2q8xPLFwIfFJWrp9GnvvpLuNieV3CHNIKS7-RbYmAmuHrtFKcpoHPqt7fdc2o08xMs',
#     'tag': '1-1711265190-unknown-0-xpdz8v1ybo-bdeba35a6aff437f',
#     'clientCacheKey': '3xq6pncb8f4ggva_hd15.mp4',
#     'di': '3cf6b25b',
#     'bp': '14944',
#     'tt': 'hd15',
#     'ss': 'vp',
# }

# response = requests.get(
#     'https://v2.kwaicdn.com/ksc2/qNez2sctthP_y9sNOWBDISmU4Vae1kA3Teca2_XbUDqKG8E1eMIWWHhLliyvHqnKgtQdUPgAuk3eD1uv2u2rlIWCCPWzxtGsvJZ0h9sxNqN6uLcHmyU4mfH5UozQMS4H9ltzSVW43y84ko-Z3DJxwYQoUCfmX3vwYZZXCJO3Vn9a-CUpUJlmZK8ycrDK7Cez.mp4',
#     params=params,
#     headers=headers,
# )
# 
# open('video.mp4'.'wb').write(response.content)
#以下單一下載的方法

cookies = {
XXXXXXXXXXXXXX
}

headers = {
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-CN;q=0.5',
    'Connection': 'keep-alive',
    # 'Cookie': 'kpf=PC_WEB; clientid=3; did=web_a57f52d5e92e83d1dee1ea3238353041; userId=4056500421; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABa9R8ZVbZ2Zo61yuvyj6IhFRHDVAQWvb64EXVLvzgXah1KFd7oW4ogaFk1-ij6DAqLDx17FMJfrfZ-k8_MYLLsiOKQ72KqL0PaU_ifpjCnpv0vo8U-UbKK96JEokaZEzfmAMgOPKR5Ns0_-pwZ6ObRc37_leLBklUZpvtgNEEC_UkpHg-smeWb_pMa-FOR_oNuLystwp6oJp98BQ39wumZxoS7YoRGiN2PM_7zCD1Dj9m5oYoIiBo3LDKaMLBqZCQ8PUnZS1B-_49nwHWoQA5HLs1ONNf8CgFMAE; kuaishou.server.web_ph=0518008e949fc974c4cc188f317401c75384; kpn=KUAISHOU_VISION',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/profile/3xckmpzvbh7wfuw',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'accept': '*/*',
    'content-type': 'application/json',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



url='https://www.kuaishou.com/graphql'


count=1
pcursor=''
if not os.path.exists('videos'):
    os.makedirs('videos')

while True:
    
    json_data = {
    'operationName': 'visionProfilePhotoList',
    'variables': {
        'userId': userid,
        'pcursor': pcursor,
        'page': 'profile',
        },
    'query': 'fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n',
    }
    res = requests.post(
        url=url,
        cookies=cookies, headers=headers, json=json_data)
    #上面可以用多少LIKE來搜索, 例如170.2萬搜170.2, 找到https://www.kuaishou.com/graphql, 再COPY CURL複製去curlconverter得到
    # print(res.text)
    
    json_text=res.json()
    # print(json_text)
    video_data=json_text['data']['visionProfilePhotoList']['feeds']
        
        
    for video in video_data:
        video_single=video['photo']['photoH265Url']
        video_name=video['photo']['caption']
        print(f'{count}  : videos/{video_name}.mp4')
        print(f'{count}  : {video_single}')
    #     res2=requests.get(video_single, headers=headers)    #需要下載用這句
    #     open(f'videos/{video_name}.mp4','wb').write(res2.content)  #需要下載用這句
        count+=1

        
    pcursor=json_text['data']['visionProfilePhotoList']['pcursor']
    print(pcursor)
    if pcursor=="no_more":
        break

