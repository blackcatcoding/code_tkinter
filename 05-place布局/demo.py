# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 14:34
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

w.geometry('600x400')

tk.Label(w, text='label1', fg='white', bg='green', width=10, height=3).place(x=10, y=10)
tk.Label(w, text='label1', fg='white', bg='green', width=10, height=3).place(relx=0.5, rely=0.5)
tk.Label(w, text='label1', fg='white', bg='green').place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
print(w.place_slaves())

w.mainloop()