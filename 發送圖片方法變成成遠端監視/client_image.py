import os.path
import threading
from socket import*
from PIL import ImageGrab #pip install Pillow

s=socket()
s.connect(('192.168.0.195', 8888))  #'192.168.0.3'是SERVER IP

#以上代不是遠程連接

def send_image(s):

    while True:
    # 1.截圖
        image=ImageGrab.grab()
        image=image.resize((960, 540))
        image.save('1.jpg')
        # 2.圖像大小告訴SERVER
        size=os.path.getsize('1.jpg')
        s.send(str(size).encode())
        # 3.等待SERVER確認
        s.recv(1024).decode()
        # 4.發送圖像
        with open('1.jpg', 'rb') as file:
            for line in file:
                s.send(line)
        # 5.等待SERVER確認        
        s.recv(1024).decode()
    
# 開啟線程
threading.Thread(target=send_image,args=(s,)).start()
