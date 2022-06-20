# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 16:49
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk
from tkinter import ttk

w = tk.Tk()
w.iconbitmap("cat32.ico")

# 换行 wraplength 宽度达到多少像素就换行
label = tk.Label(w, text="黑猫编程abcd", fg="red", bg="yellow", width=10, height=3, anchor=tk.CENTER, wraplength=60, justify="left", relief="solid")
label2 = tk.Label(w, bitmap="hourglass", text='A', compound="top")
label3 = tk.Label(w, text="黑猫编程", fg="red", bg="yellow", padx=20, pady=5)

sep = ttk.Separator(w, orient=tk.HORIZONTAL)
sep2 = ttk.Separator(w, orient=tk.HORIZONTAL)
label.pack()
sep.pack(fill=tk.X, pady=10)
label2.pack()
sep2.pack(fill=tk.X, pady=10)
label3.pack()

print(label.keys())
w.mainloop()