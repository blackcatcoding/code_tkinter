# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 17:41
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk
from tkinter import messagebox

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

messagebox.askokcancel('标题1', '内容', parent=w)
messagebox.askquestion('标题2', '问题')
messagebox.askretrycancel('标题3', '重试 取消')
messagebox.showwarning('标题4', '警告')
messagebox.showerror('标题5', '错误')
messagebox.showinfo('标题6', 'info')

w.mainloop()