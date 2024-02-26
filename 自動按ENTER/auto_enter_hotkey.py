import keyboard
import time
import threading
import os

n=100
# 定義當熱鍵觸發時要執行的函數
def press_enter_repeatedly():
    print("熱鍵ALT+1被觸發，將自動按下ENTER鍵100次。")
    
    
    for i in range(n):
        print(i)
        keyboard.send('enter')
        if keyboard.is_pressed('ALT+2'):
            exit_script()
        time.sleep(1)  # 在連續按鍵之間添加小延遲，以防過快輸入

def exit_script():
    print("熱鍵ALT+2被觸發，停止")
    os._exit(0)
# 設定熱鍵和對應的處理函數
print('running')
keyboard.add_hotkey('alt+1', press_enter_repeatedly)
keyboard.add_hotkey('alt+2', exit_script)
print("腳本運行中，按下ALT+1觸發自動按ENTER。")



try:
    
    keyboard.wait('esc')
except KeyboardInterrupt:
    print('123')


print('finish')
