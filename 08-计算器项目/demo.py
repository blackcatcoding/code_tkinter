# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 17:08
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import tkinter as tk

tmp_str = ''
def add_str(s):
    global show_str, tmp_str
    tmp_str += s
    show_str.set(tmp_str)

def calc():
    global show_str
    try:
        res = eval(entry.get())
        show_str.set(str(res))
    except:
        print('输入数学表达式不合法')

    # tmp_str = ''
    # show_str.set(tmp_str)

def clear_str():

    global show_str, tmp_str
    entry.delete(0, tk.END)
    tmp_str = ''
    show_str.set(tmp_str)

w = tk.Tk()
w.iconbitmap('cat32.ico')
w.title('黑猫编程')
w.resizable(0, 0)

#　绑定变量
show_str = tk.StringVar()
entry = tk.Entry(w, text='', bg='yellow', width=20, textvariable=show_str)

btn7 = tk.Button(w, text='7', width=3, command=lambda : add_str('7'))
btn8 = tk.Button(w, text='8', width=3, command=lambda : add_str('8'))
btn9 = tk.Button(w, text='9', width=3, command=lambda : add_str('9'))
btn_star = tk.Button(w, text='*', width=3, command=lambda : add_str('*'))

btn4 = tk.Button(w, text='4', width=3, command=lambda : add_str('4'))
btn5 = tk.Button(w, text='5', width=3, command=lambda : add_str('5'))
btn6 = tk.Button(w, text='6', width=3, command=lambda : add_str('6'))
btn_minus = tk.Button(w, text='-', width=3, command=lambda : add_str('-'))

btn1 = tk.Button(w, text='1', width=3, command=lambda : add_str('1'))
btn2 = tk.Button(w, text='2', width=3, command=lambda : add_str('2'))
btn3 = tk.Button(w, text='3', width=3, command=lambda : add_str('3'))
btn_plus = tk.Button(w, text='+', width=3, command=lambda : add_str('+'))

btn0 = tk.Button(w, text='0', width=3, command=lambda : add_str('0'))
btn_dot = tk.Button(w, text='.', width=3, command=lambda : add_str('.'))
btn_clear = tk.Button(w, text='cls', width=3, command=clear_str)
btn_calc = tk.Button(w, text='=', width=3, command=calc)

entry.grid(row=0, column=0, columnspan=4)
btn7.grid(row=1, column=0, padx=5)
btn8.grid(row=1, column=1, padx=5)
btn9.grid(row=1, column=2, padx=5)
btn_star.grid(row=1, column=3, padx=5)

btn4.grid(row=2, column=0, padx=5)
btn5.grid(row=2, column=1, padx=5)
btn6.grid(row=2, column=2, padx=5)
btn_minus.grid(row=2, column=3, padx=5)

btn1.grid(row=3, column=0, padx=5)
btn2.grid(row=3, column=1, padx=5)
btn3.grid(row=3, column=2, padx=5)
btn_plus.grid(row=3, column=3, padx=5)

btn0.grid(row=4, column=0, padx=5)
btn_dot.grid(row=4, column=1, padx=5)
btn_clear.grid(row=4, column=2, padx=5)
btn_calc.grid(row=4, column=3, padx=5)

w.mainloop()