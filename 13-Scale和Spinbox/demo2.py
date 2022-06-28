# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 15:40
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def print_info():

    print(spin.get())

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

spin = tk.Spinbox(w, from_=0, to=30, increment=2, command=print_info)
spin.pack(pady=20)

spin2 = tk.Spinbox(w, values=(10, 20, 35, 99))
spin2.pack(pady=20)

spin3 = tk.Spinbox(w, values=('hello', 'cat', 'ni', 'hao'))
spin3.pack(pady=20)

w.mainloop()