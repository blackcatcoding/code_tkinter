# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 23:13
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import tkinter as tk

w = tk.Tk()

w.iconbitmap('cat32.ico')

label = tk.Label(w, text="黑猫编程", fg="red", bg="yellow", width=10, height=3, anchor="n").pack()

w.mainloop()