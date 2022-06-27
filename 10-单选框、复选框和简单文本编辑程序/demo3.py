# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 17:14
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

def selAll():

    entry.select_range(0, tk.END)

def deSel():

    entry.select_clear()

def cls():

    entry.delete(0, tk.END)

def readonly():

    if v.get():
        entry.config(state=tk.DISABLED)
    else:
        entry.config(state=tk.NORMAL)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

entry = tk.Entry(w)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W)

btnSel = tk.Button(w, text='全选', command=selAll)
btnSel.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

btnDeSel = tk.Button(w, text='取消选择', command=deSel)
btnDeSel.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

btnCls = tk.Button(w, text='删除', command=cls)
btnCls.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

btnQuit = tk.Button(w, text='结束', command=w.destroy)
btnQuit.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

v = tk.BooleanVar()
v.set(False)

checkBtnReadOnly = tk.Checkbutton(w, text='只读', variable=v, command=readonly)
checkBtnReadOnly.grid(row=2, column=0)

w.mainloop()