# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 17:11
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def click():
    print('Radiobutton value is', v.get())

def click2():
    print('Radiobutton value is', v2.get())

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

v = tk.IntVar()
tk.Radiobutton(w, text='A', variable=v, value=1, command=click).pack()
tk.Radiobutton(w, text='B', variable=v, value=2, command=click).pack()
tk.Radiobutton(w, text='C', variable=v, value=3, command=click).pack()
tk.Radiobutton(w, text='D', variable=v, value=4, command=click).pack()

v2 = tk.IntVar()
tk.Radiobutton(w, text='A', variable=v2, value=1, command=click2).pack()
tk.Radiobutton(w, text='B', variable=v2, value=2, command=click2).pack()
tk.Radiobutton(w, text='C', variable=v2, value=3, command=click2).pack()
tk.Radiobutton(w, text='D', variable=v2, value=4, command=click2).pack()

w.mainloop()