import os.path
import cv2 #pip install opencv-python
import socket


S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(('', 8888))  # 綁定到本機所有可用的接口和8888端口
S.listen()
print("服務器正在運行，等待連接...")
s, addr =S.accept()
#以上代碼是遠程連接
print('running')

while True:
    # 1.接收圖像大小
    size=int(s.recv(1024).decode())
    # 2.發送確認信息
    s.send('ok'.encode())
    # 3.接收圖像數據

    with open('2.jpg','wb') as file:
        cursize=0
        while cursize < size:
            data=s.recv(2048)
            file.write(data)
            cursize+=len(data)
        
    # 4.顯示圖像
    cv2.namedWindow('TEST')
    image =cv2.imread('2.jpg')
    cv2.imshow('TEST',image)
    cv2.waitKey(20) #20毫秒刷新

    # 5.發送確認信息
    s.send('ok'.encode())
