# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 15:33
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def onclick():
    print(scale1.get(), scale2.get())

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

scale1 = tk.Scale(w, from_=0, to=10, length=300, troughcolor='yellow', width='30', label='scale1', tickinterval=2, orient=tk.VERTICAL)
scale1.pack()

scale2 = tk.Scale(w, from_=0, to=10, length=300, troughcolor='yellow', width='30', label='scale2', tickinterval=2, orient=tk.HORIZONTAL)
scale2.pack()

tk.Button(w, text='Print', command=onclick).pack()

w.mainloop()