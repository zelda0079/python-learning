import tkinter  #pip install tk
from PIL import Image, ImageTk  # pip install Pillow
import pygame  #pip install pygame

def close_window():
    root.destroy()
# 创建Tkinter窗口
x=y=0
curframe=0
frames=[]

root = tkinter.Tk()
root.overrideredirect(True)  #無邊框
root.geometry('150x180')
root.wm_attributes('-topmost', True)  #窗口設在最前
root.attributes('-transparentcolor','black')  #窗口黑色地方變透明

pygame.mixer.init()  #初始化
pygame.mixer.music.load('123.mp3')


gif = Image.open('123.gif')
try:
    while True :
        frame= gif.copy().convert('RGBA')
        frames.append(ImageTk.PhotoImage(frame))
        gif.seek(len(frames))
except EOFError:  #EOF文件結尾
    pass

# 创建一个按钮，点击后会关闭窗口
exit_button = tkinter.Button(root, text="退出", command=close_window)
exit_button.pack()
cavas = tkinter.Canvas(root, borderwidth=0, highlightthickness=0)   #畫布
cavas.pack()  #放到窗口
cavas.create_image(0,0, anchor='nw', image=frames[-1])

#回調函數
def get_pos(event):
    global x, y
    x=event.x
    y=event.y

def move_window(event):
    root.geometry(f'+{event.x_root-x}+{event.y_root-y}')
    
def play_gif():
    global curframe
    try:
        cavas.create_image(0,0, anchor='nw', image=frames[curframe])
    except IndexError:  #EOF文件結尾
        pass
    curframe+=1
    if curframe >=len(frames):
        return 
    cavas.after(100, play_gif)

def touch_fish(event):
    global curframe
    curframe=0
    pygame.mixer.music.play()
    play_gif()
    
    
    
root.bind('<Button-1>', get_pos)
root.bind('<B1-Motion>', move_window)
root.bind('<ButtonRelease-1>', touch_fish)
# 运行事件循环
root.mainloop()
