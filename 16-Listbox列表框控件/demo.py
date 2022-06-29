# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 16:52
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

fruits = ['apple', 'banana', 'orange', 'mongo']

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

lb = tk.Listbox(w, selectmode=tk.EXTENDED)

for fruit in fruits:
    lb.insert(tk.END, fruit)

lb.pack()

w.mainloop()