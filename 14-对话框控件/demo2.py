# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 17:47
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk
from tkinter import filedialog, colorchooser

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

def open_file():

    file_name = filedialog.askopenfilename(title='打开文件', initialdir='./', filetype=[('PNG', '.png'), ('文本文档', '.txt')])
    print(file_name)

def save_file():

    file_name = filedialog.asksaveasfilename(title='保存文件', initialdir='./')
    print(file_name)

def open_dir():

    dir_name = filedialog.askdirectory()
    print(dir_name)

def select_color():

    ret = colorchooser.askcolor()
    print(ret)

tk.Button(w, text='open', command=open_file).pack()
tk.Button(w, text='save', command=save_file).pack()
tk.Button(w, text='open directory', command=open_dir).pack()
tk.Button(w, text='color', command=select_color).pack()

w.mainloop()