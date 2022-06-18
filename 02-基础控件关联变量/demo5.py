# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 23:27
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import tkinter as tk

w = tk.Tk()

w.iconbitmap('cat32.ico')

# from_:设置最小值 to:设置最大值
# tickinterval:设置刻度 length:设置滑块长度，单位是像素

v = tk.IntVar()

tk.Scale(w, orient='horizontal', variable=v, from_=0, to=200, tickinterval=50, length=200).pack()

w.mainloop()