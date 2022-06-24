# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 17:16
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def callback():
    print('按钮被点击了')

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.geometry('300x200')
w.resizable(0, 0)

def set_bgcolor(color):

    w.config(bg=color)

exitbtn = tk.Button(w, text='Exit', command=w.destroy)
bluebtn = tk.Button(w, text='Blue', command=lambda : set_bgcolor('blue'))
yellowbtn = tk.Button(w, text='Yellow', command=lambda : set_bgcolor('yellow'))

exitbtn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
bluebtn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
yellowbtn.pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

w.mainloop()