# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 17:14
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def add(a, b):
    print(a + b)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

tk.Button(w, text='点击我', command=lambda : add(1, 2)).pack()

w.mainloop()