# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 16:52
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def select_items(event):
    obj = event.widget
    # print(obj)
    indexs = obj.curselection()

    for idx in indexs:
        print(obj.get(idx))

    print('-' * 20)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

scrollbar = tk.Scrollbar(w)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lb = tk.Listbox(w, yscrollcommand=scrollbar.set, selectmode=tk.EXTENDED)

for i in range(50):
    lb.insert(tk.END, 'Line ' + str(i))
lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lb.yview)

lb.bind('<<ListboxSelect>>', select_items)

w.mainloop()