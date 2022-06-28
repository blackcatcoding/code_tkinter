# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 10:27
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def onclick():

    w = tk.Toplevel()
    tk.Label(w, text='我是新窗口').pack()

    w.transient(root)
    w.mainloop()

root = tk.Tk()
tk.Button(root, text='打开窗口', command=onclick).pack()

root.mainloop()