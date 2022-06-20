# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 17:07
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com
import tkinter as tk

counter = 0
def run_counter(labelobj):

    def counting():
        global counter
        counter += 1
        labelobj.config(text=str(counter))
        labelobj.after(1000, counting)
    counting()

w = tk.Tk()
w.iconbitmap("cat32.ico")

label = tk.Label(w, fg="red", bg="yellow", width=10, height=3, cursor="heart")\

label.pack()

run_counter(label)
w.mainloop()
