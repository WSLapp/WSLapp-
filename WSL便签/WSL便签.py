'''from tkinter import *
# 创建主窗口
win = Tk()
win.title("C语言中文网")
win.geometry('250x180')
#win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建滚动条
s = Scrollbar(win)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side = RIGHT,fill = Y)

# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 =Listbox(win,height =8, yscrollcommand = s.set)
# i 表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(range(1,16)):
    listbox1.insert(i,'便签'+str(item))
listbox1.pack()
# 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s.config(command = listbox1.yview)

# 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
bt = Button(win,text='删除',command = lambda x = listbox1:x.delete(ACTIVE))
# 将按钮放置在底部
bt.pack(side = BOTTOM)
# 显示窗口
win.mainloop()'''
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import *

window = tk.Tk()

window.title("WSL便签")
window.geometry('250x180')
s = Scrollbar(window)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side = RIGHT,fill = Y)
#window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')

# 创建变量，用var1用来接收鼠标点击的具体选项内容
var1 = tk.StringVar()
l = tk.Label(window, bg='#B0B0B0', font=('微软雅黑', 15), width=20, textvariable=var1)
l.pack()

# 创建一个按钮的点击事件
def click_button():
    # 使用 curselection来选中文本
    try:
        val = lb.get(lb.curselection())
    # 设置label值
        var1.set(val)
        a=val
        #os.startfile('.\WSL'+val)
        val='.\WSL'+val+'\WSL便签.py'
        #print(val)
        #f1=open('who.txt','w')
        #f1.write(a)
        #f1.close()
        os.startfile(val)
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e,'没有选择任何条目')

# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='添加到桌面', command=click_button)
b1.pack()


# 创建Listbox并为其添加内容
var2 = tk.StringVar()
#var2.set(("C语言辅导班", "Python答疑辅导", "Java答疑辅导", "C++辅导"))
# 创建Listbox，通过 listvariable来传递变量
lb = tk.Listbox(window)#var2)
# 新建一个序列，然后将值循环添加到Listbox控件中
#items = ["C", "Java", "Python", "C#", "Golang", "Runby"]
for i,item in enumerate(range(1,16)):
    lb.insert(i,'便签'+str(item))
s.config(command = lb.yview)
#for i in items:
#    lb.insert('end', i)  # 从最后一个位置开始加入值
#lb.insert(0, '编程学习')  # 在第一个位置插入一段字符串
#lb.delete(4)  # 删除第2个位置处的索引
lb.pack()

#主窗显示
window.mainloop()
