# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 22:25
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
# w.resizable(0, 0)

tk.Label(w, text='账号').grid(row=0, sticky=tk.W, padx=2)
tk.Label(w, text='密码').grid(row=1, sticky=tk.W, padx=2)

tk.Entry(w).grid(row=0, column=1, sticky=tk.E)
tk.Entry(w).grid(row=1, column=1, sticky=tk.E)

tk.Button(w, text='Login').grid(row=2, column=1, sticky=tk.E)

w.mainloop()