# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 22:40
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

# Frame LabelFrame

fr1 = tk.Frame(w, bg='lightyellow', relief=tk.RAISED, borderwidth=5)
fr1.pack()

btn1 = tk.Button(fr1, text='red', fg='red')
btn1.pack(side=tk.LEFT, padx=5, pady=5)
btn2 = tk.Button(fr1, text='green', fg='green')
btn2.pack(side=tk.LEFT, padx=5, pady=5)
btn3 = tk.Button(fr1, text='blue', fg='blue')
btn3.pack(side=tk.LEFT, padx=5, pady=5)

fr2 = tk.Frame(w, bg='lightblue', relief=tk.GROOVE, borderwidth=5)
fr2.pack(pady=5)

btn4 = tk.Button(fr2, text='purple', fg='purple')
btn4.pack(side=tk.LEFT, padx=5, pady=5)

fr3 = tk.LabelFrame(w, text='黑猫编程', bg='red')
fr3.pack(pady=5)

label = tk.Label(fr3, text='C++ Python Java')
label.pack()

w.mainloop()