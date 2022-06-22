# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 19:05
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

w.geometry('300x180')

okLabel = tk.Label(w, text='OK', font=('Arial', 20, 'bold'), fg='white', bg='blue')
okLabel.pack(anchor=tk.S, side=tk.RIGHT, padx=10, pady=10)

noLabel = tk.Label(w, text='NO', font=('Arial', 20, 'bold'), fg='white', bg='red')
noLabel.pack(anchor=tk.S, side=tk.RIGHT, pady=10)

w.mainloop()