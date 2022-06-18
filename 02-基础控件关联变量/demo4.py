# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 23:24
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import tkinter as tk

w = tk.Tk()

w.iconbitmap('cat32.ico')

v = tk.StringVar()

entry = tk.Entry(w, textvariable=v)
v.set("请输入......")

entry.pack()

w.mainloop()