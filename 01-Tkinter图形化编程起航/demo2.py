import tkinter as tk
from PIL import ImageTk
window = tk.Tk()
window.resizable(0, 0)
w.iconbitmap("cat.ico")
window.title('真相')
truth = '真相只有一个！'
bg = ImageTk.PhotoImage(file="images/truth.png")

#请在下方书写你的代码
#题目：使用tkinter模块实现，完成在界面上显示truth变量中的内容
#提示：字体为'Arial'、字号为：29、字体颜色 foreground 为：'white'、组合方式 compound 为：'center'
text = tk.Label(window,
                image = bg,
                text = truth,
                font = ('Arial',29),
                foreground = 'white',
                compound = 'right')
text.pack()  
window.mainloop()