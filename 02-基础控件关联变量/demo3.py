# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 23:22
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import tkinter as tk

w = tk.Tk()

w.iconbitmap('cat32.ico')

def onClick():
    print("radiobutton value is ", v.get())

v = tk.IntVar()

tk.Radiobutton(w, text="男", variable=v, value=3, command=onClick).pack(anchor=tk.W)
tk.Radiobutton(w, text="女", variable=v, value=4, command=onClick).pack(anchor=tk.W)

w.mainloop()