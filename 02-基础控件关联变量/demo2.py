# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 23:17
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import tkinter as tk

w = tk.Tk()

w.iconbitmap('cat32.ico')

def onClick():
    print("checkbutton value is ", v.get())

v = tk.IntVar()

tk.Checkbutton(w, text="我是一个按钮", variable=v, command=onClick).pack()
w.mainloop()