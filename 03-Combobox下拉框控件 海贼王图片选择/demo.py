# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/18 21:25
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

# 定义事件函数
def showImg(*args):

    print(cbx.get())

    if cbx.get() == '路飞':
        bgImg = ImageTk.PhotoImage(file='images/lufei.jpg')
    elif cbx.get() == '罗':
        bgImg = ImageTk.PhotoImage(file='images/luo.jpg')
    elif cbx.get() == '索隆':
        bgImg = ImageTk.PhotoImage(file='images/suolong.jpg')
    else:
        bgImg = ImageTk.PhotoImage(file='images/haizei.jpg')

    # 更新背景图片
    bg.config(image=bgImg)
    bg.image = bgImg

w = tk.Tk()
w.iconbitmap('images/cat32.ico')
w.geometry('800x600')
w.resizable(0, 0)
w.title('海贼王')

# 显示背景图片
bgImg = ImageTk.PhotoImage(file='images/haizei.jpg')
bg = tk.Label(w, width=800, height=600, image=bgImg)
bg.pack()

# 下拉框控件
cbx = ttk.Combobox(w, width=15)
cbx['values'] = ['请选择人物', '路飞', '罗', '索隆']
cbx.place(x=0, y=0)

cbx.current(0)
cbx['state'] = 'readonly'

# 绑定事件
cbx.bind('<<ComboboxSelected>>', showImg)


w.mainloop()