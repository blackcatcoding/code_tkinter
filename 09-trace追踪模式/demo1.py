# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 10:16
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def callback(*args):
    print(s1.get(), args)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

s1 = tk.StringVar()
entry = tk.Entry(w, textvariable=s1)
entry.pack(padx=10, pady=5)

s1.trace('w', callback)

w.mainloop()