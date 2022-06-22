# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 18:51
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

fr1 = tk.Frame(w)
fr2 = tk.Frame(w)

tk.Label(fr1, text='pack 布局 expend').pack()
tk.Button(fr1, text='A').pack()
tk.Button(fr1, text='B').pack(expand=1, fill=tk.X)
tk.Button(fr1, text='C').pack(expand=1)


tk.Label(fr2, text='pack side 和 fill').pack()
tk.Button(fr2, text='D').pack(side=tk.LEFT, fill=tk.Y)
tk.Button(fr2, text='E').pack(side=tk.LEFT, fill=tk.X)
tk.Button(fr2, text='F').pack(side=tk.RIGHT)
tk.Button(fr2, text='G').pack(side=tk.TOP, fill=tk.BOTH)
tk.Button(fr2, text='H').pack(side=tk.LEFT, fill=tk.X, expand=1)
fr1.pack()
fr2.pack()

w.mainloop()