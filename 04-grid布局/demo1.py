# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 22:20
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

tk.Label(w, width=15, height=3, bg='red').grid(row=0, column=0, rowspan=2, sticky='ns')
tk.Label(w, width=15, height=3, bg='green').grid(row=0, column=1, columnspan=2, sticky='we')
# tk.Label(w, width=15, height=3, bg='pink').grid(row=0, column=2)

# tk.Label(w, width=15, height=3, bg='blue').grid(row=1, column=0)
tk.Label(w, width=15, height=3, bg='orange').grid(row=1, column=1)
tk.Label(w, width=15, height=3, bg='brown').grid(row=1, column=2)

w.mainloop()