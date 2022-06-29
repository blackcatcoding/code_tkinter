# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 23:12
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

def callback(event, a, b):

    print(event.type, event.num, a, b)

frame = tk.Frame(w, bg='lightyellow', width=100, height=80)
# frame.bind('<Button-1>', callback)
frame.bind('<Button-1>', lambda event : callback(event, 1, 2))
frame.pack()

w.mainloop()