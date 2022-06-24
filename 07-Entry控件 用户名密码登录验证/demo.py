# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/22 18:16
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk
import easygui

def check_info():

    # print(usernameEntry.get(), passwdEntry.get())
    if usernameEntry.get() == 'cat' and passwdEntry.get() == '123456':
        easygui.msgbox('恭喜你，登陆成功')
    else:
        easygui.msgbox('登录失败，请再次输入')

def clear_info():
    usernameEntry.delete(0, tk.END)
    passwdEntry.delete(0, tk.END)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')

welcome = tk.Label(w, text='欢迎来到黑猫编程在线测评系统')

usernameLabel = tk.Label(w, text='用户名')
usernameEntry = tk.Entry(w)
# usernameEntry.insert(0, '请输入你的用户名')

passwdLabel = tk.Label(w, text='密码')
passwdEntry = tk.Entry(w, show='*')

loginBtn = tk.Button(w, text='Login', command=check_info)
quitBtn = tk.Button(w, text='Exit', command=w.quit)
clearInput = tk.Button(w, text='Clear', command=clear_info)

welcome.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
usernameLabel.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1)
passwdLabel.grid(row=2, column=0)
passwdEntry.grid(row=2, column=1)

quitBtn.grid(row=3, column=0, columnspan=2, sticky=tk.E)
loginBtn.grid(row=3, column=0, columnspan=2, sticky=tk.E, padx=40)
clearInput.grid(row=3, column=0, columnspan=2, sticky=tk.E, padx=80)

w.mainloop()