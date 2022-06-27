# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 17:08
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def click():
    print('Checkbutton value is', v.get())

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

v = tk.IntVar()
tk.Checkbutton(w, text='A', variable=v, command=click).pack()
tk.Checkbutton(w, text='B').pack()
tk.Checkbutton(w, text='C').pack()
tk.Checkbutton(w, text='D').pack()
w.mainloop()