# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 22:39
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

w.rowconfigure(1, weight=1)
w.columnconfigure(0, weight=1)

tk.Label(w, text='label1', bg='pink').grid(row=0, column=0, sticky=tk.W + tk.E)
tk.Label(w, text='label2', bg='red').grid(row=0, column=1)
tk.Label(w, text='label3', bg='green').grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S)
w.mainloop()