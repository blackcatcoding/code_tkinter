# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 10:21
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk


def callbackW(*args):
    # print(s1.get(), args)
    s2.set(s1.get())

def callbackR(*args):
    print('正在读取数据ing')

def read_data():
    print('读取数据', s1.get())

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

s1 = tk.StringVar()
entry = tk.Entry(w, textvariable=s1)
entry.pack(padx=10, pady=5)
s1.trace('w', callbackW)
s1.trace('r', callbackR)

s2 = tk.StringVar()
label = tk.Label(w, textvariable=s2)
s2.set('同步显示')
label.pack(padx=10, pady=5)

btn = tk.Button(w, text='读取', command=read_data)
btn.pack(pady=5)

w.mainloop()