import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
# 彈窗確認函數
def confirm_and_press_enter():
    # 創建主視窗並隱藏
    root = tk.Tk()
    root.withdraw()
    # 彈窗確認
    response = messagebox.askyesno("確認", "確認後將自動按N次Enter，是否繼續？")
    # 如果用戶確認
    if response:
        # 設定需要按Enter的次數
        n = 100
        # 給用戶時間切換到目標窗口
        time.sleep(2)
        # 自動按Enter
        for _ in range(n):
            pyautogui.press('enter')
            # 可以在這裡設置每次按鍵之間的間隔
            time.sleep(0.5)
        print("已完成按Enter操作。")
    else:
        print("用戶取消操作。")
    # 關閉主視窗
    root.destroy()
# 呼叫彈窗確認並按Enter的函數
confirm_and_press_enter()
