import tkinter as tk    # 给模块起别名

w = tk.Tk()     # 创建一个根窗口
w.iconbitmap("cat.ico")
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
width = 300
height = 200
x = (screen_width-width) / 2
y = (screen_height-height) / 2
w.geometry("%dx%d+%d+%d" % (width, height, x, y))

w.mainloop()    # 程序进入主循环，否则立即终止