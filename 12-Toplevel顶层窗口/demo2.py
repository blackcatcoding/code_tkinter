# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 10:31
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def work(w):

    w.iconify()

def onclick():

    w = tk.Toplevel()
    w.title('顶层窗口')
    w.geometry('+300+300')

    tk.Button(w, text='点击我', command=lambda : work(w)).pack()
    # w.transient(root)
    w.mainloop()

root = tk.Tk()
root.title('主窗口')
root.geometry('200x200+200+200')

root.resizable(0, 0)

tk.Button(root, text='打开窗口', command=onclick).pack()

root.mainloop()