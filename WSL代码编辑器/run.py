def rgwtgxrg():
    exit()
def exit():
    f1=open('exit.txt','w')
    f1.close()
import win32api,win32con
import tkinter
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.colorchooser
import tkinter.simpledialog
import time
import easygui as g
import tkinter
import tkinter.messagebox
import os
#import virtkey
import psutil
import threading
import idlelib.colorizer as idc
import idlelib.percolator as idp
from pynput.keyboard import Key, Controller
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from threading import Thread
from tkinter.ttk import *

# ----------------------------------------一、创建窗口-------------------------------------------------
filename = ""  # 定义空文件名
f1=open('run_file.txt','r')
filename=f1.read()
f1.close()
f1=open('run_file.txt','w')
f1.write('')
f1.close()
win = tk.Tk()#.overrideredirect(True)#root.overrideredirect(True)#win.overrideredirect(True)
win.title('WSL代码编辑器')
win["height"] = 400
win["width"] = 600
# ----------------------------------------特殊---------------------------------------------------------
run="""import threading
def ercegeg():
    while True:
        try:
            f =open("run.py")
            f.close()
        except FileNotFoundError:
            exit()
rctrex = threading.Thread(target=ercegeg, daemon=True)
# daemon=True 表示创建的子线程守护主线程，主线程退出子线程直接销毁
rctrex.start()"""
def Tkinter_ScrolledText_Code(txtContent):
    import idlelib.colorizer as idc
    import idlelib.percolator as idp
    txtContent.focus_set()
    idc.color_config(txtContent)
    txtContent.focus_set()
    #txtContent.config(bg='white',fg='black')
    p = idp.Percolator(txtContent)
    d = idc.ColorDelegator()
    p.insertfilter(d)
def mycopy(file1,file2):#定义一个mycopy函数用于复制文件
    import os#调出os库
    #global run
    #file11 = os.path.join(dir1,f)
    #file22 = os.path.join(dir2,f)
    #os.mkdir(file2)
    f = open(file2, 'w')
    f.close()
    f1=open(file1,"rb")#以读取模式打开file1
    f2=open(file2,"wb")#以清空写模式打开file2
    f3=open('myrun.py',"rb")
    #print(run)
    f2.write(f3.read())
    content = f1.readline()#将第一行数据赋给content
    while len(content)>0:#如果读取到的数据长度不为0则循环执行
        f2.write(content)#在file2里写下content
        content=f1.readline()#再读一行赋给content
 
    f1.close()#关闭file1
    f2.close()
    f3.close

def new():
    #os.startfile(".\WSL文件编辑器.py")
    os.startfile(os.path.basename(__file__))
def quit_exit():
    global filename
    if textChanged.get():
        yesno = tk.messagebox.askyesno(
            title="提醒", message="你想保存吗?")  # 询问框
        if yesno == tkinter.YES:
            if not filename:
                SaveAs()
            else:
                Save()
        else:
            try:
                (filepath,tempfilename) = os.path.split(filename)
                (file_name,extension) = os.path.splitext(tempfilename)
                os.rename(filename,filepath+file_name+'.py')
            except Exception as e:
                pass
            exit()
            #win.destroy()
    else:
        try:
            (filepath,tempfilename) = os.path.split(filename)
            (file_name,extension) = os.path.splitext(tempfilename)
            os.rename(filename,filepath+file_name+'.py')
        except Exception as e:
            pass
        exit()
        #win.destroy()
    try:
        (filepath,tempfilename) = os.path.split(filename)
        (file_name,extension) = os.path.splitext(tempfilename)
        os.rename(filename,filepath+file_name+'.py')
    except Exception as e:
        pass
    exit()
    #win.destroy()

def popup(event):
    right.post(event.x_root,event.y_root)
def kill(pid):
    # 本函数用于中止传入pid所对应的进程
    if os.name == 'nt':
        # Windows系统
        cmd = 'taskkill /pid  /f'# + str(pid) +
        cmd='taskkill /F /IM '+str(pid)
        try:
            os.system(cmd)
            print(pid, 'killed')
        except Exception as e:
            print(e)
    elif os.name == 'posix':
        # Linux系统
        cmd = 'kill ' + str(pid)
        try:
            os.system(cmd)
            print(pid, 'killed')
        except Exception as e:
            print(e)
    else:
        print('Undefined os.name')
    
# ---------------------------------------二、功能定义区---------------------------------------------

mylist=[]

# -----------------------------------------1.菜单栏 File-----------------------------------------------------------

textChanged = tk.IntVar(value=0)  # 字符串计数器

# 1.打开


def Open():
    global filename
    # 1.获取字符，是否保存原来的文档
    if textChanged.get():
        yesno = tk.messagebox.askyesno(
            title="提醒", message="你想保存吗?")  # 询问框

        if yesno == tkinter.YES:
            Save()
        #filename = tkinter.filedialog.askopenfilename(
        #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
        #filename = g.fileopenbox(default="*.txt")
    # 2.打开新的文档
    
    #filename = g.fileopenbox("打开","","*.txt")
    
    filename = tkinter.filedialog.askopenfilename(
        title="打开", filetypes=[("Text files", "*.py")])  # 打开路径框
    if filename:
        mylist.append(filename)
        (filepath,tempfilename) = os.path.split(filename)
        (file_name,extension) = os.path.splitext(tempfilename)
        if filename!="":
            win.title('WSL代码编辑器-'+file_name)
        else:
            win.title('WSL代码编辑器')
        txtContent.delete(0.0, tk.END)  # 删除原来的文本
        #filename = tkinter.filedialog.askopenfilename(
        #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
        #filename = g.fileopenbox(default="*.txt")
        fp = open(filename,'r',encoding='utf-8',errors='ignore')  # 读取文本
        txtContent.insert(1.0, fp.read())  # 解码插入到文本编辑器
        fp.close()  # 关闭指针
        #textChanged.set(0)  # 字符串置0
def Open1(): #读取文件
    global filename
    filename = tkinter.filedialog.askopenfilename(
        title="打开", filetypes=[("Text files", "*.py")])  # 打开路径框
    if filename != '':
        textChanged.delete(1.0,tk.END)#delete all
        f = open(filename,'r',encoding='utf-8',errors='ignore')
        txtContent.insert(1.0,f.read())
        f.close()

# 2.保存


def Save():
    global filename
    if not filename:
        SaveAs()

    elif textChanged.get():
        fp = open(filename, "w")  # 创建文本
        fp.write(txtContent.get(0.0, tkinter.END))  # 将文本框的内容导入文件
        fp.close()  # 关闭
        #win32api.MessageBox(0, "保存完毕", "WSL文件编辑器·保存",win32con.MB_OK)
        textChanged.set(0)  # 计数器置0
        #win32api.MessageBox(0, "保存完毕", "WSL文件编辑器·保存",win32con.MB_OK)
        #windows=Tk()
        #windows.title("使用说明")
        #windows.geometry("200x100+200+100")
        #name="""保存完毕"""
        #listbox = ScrolledText(windows)
        #listbox.place(x=0, y=0, width=500, height=300)
        #listbox.insert(tkinter.END, name)
        #listbox.insert(tkinter.END, name)
        #listbox.see(tkinter.END)                                    # ScrolledText组件方法，自动定位到结尾，否则只有消息在涨，窗口拖动条不动
        #listbox.update()
        #time.sleep(3)
        #windows.destroy()
    if filename:
        win32api.MessageBox(0, "保存完毕", "WSL代码编辑器·保存",win32con.MB_OK)

# 3.保存到


def SaveAs():
    global filename
    # 创建对话框，默认对应的路径和文件名
    newfilename = tkinter.filedialog.asksaveasfilename(
        title="另存为", initialdir=r"c:\\", initialfile="new.py")

    # 写入文件内容
    if newfilename:
        print(newfilename)
        filename = newfilename
        mylist.append(filename)
        (filepath,tempfilename) = os.path.split(newfilename)
        (file_name,extension) = os.path.splitext(tempfilename)
        win.title('WSL代码编辑器-'+file_name)
        fp = open(newfilename, "w")
        print(txtContent.get(0.0, tkinter.END))
        fp.write(txtContent.get(0.0, tkinter.END))#txtContent.get(0.0, tkinter.END)
        fp.close()
        filename = newfilename

        textChanged.set(0)

# 4.删除


def Remove():
    global filename
    if filename!="":
        os.remove(filename)
        #filename = tkinter.filedialog.askopenfilename(
        #    title="打开", filetypes=[("Text files", "*.txt")])  # 打开路径框
        filename=""
        win.title('WSL代码编辑器')
        if filename:
            mylist.append(filename)
            #submenu4.add_command(label=filename)#, command=
            (filepath,tempfilename) = os.path.split(filename)
            (file_name,extension) = os.path.splitext(tempfilename)
            os.rename(filename,filepath+file_name+'.txt')
            if filename!="":
                win.title('WSL代码编辑器-'+file_name)
            else:
                win.title('WSL代码编辑器')
            txtContent.delete(0.0, tk.END)  # 删除原来的文本
            #filename = tkinter.filedialog.askopenfilename(
            #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
            #filename = g.fileopenbox(default="*.txt")
            txtContent.insert(1.0, '')
            #fp = open(filename, "rb")  # 读取文本
            #txtContent.insert(tkinter.INSERT, "".join(
            #    fp.read().decode('GBK')))  # 解码插入到文本编辑器
            #fp.close()  # 关闭指针
            #textChanged.set(0)  # 字符串置0
        else:
            win.title('WSL代码编辑器')
    else:
        messagebox.showerror("WSL代码编辑器","未打开文件 ")
# 5.关闭


def Close():
    global filename
    Save()  # 保存
    txtContent.delete(0.0, tkinter.END)  # 区域置空
    filename = ""  # 文件名置空
    (filepath,tempfilename) = os.path.split(filename)
    (file_name,extension) = os.path.splitext(tempfilename)
    os.rename(filename,filepath+file_name+'.py')
    if filename!="":
        win.title('WSL代码编辑器-'+file_name)
    else:
        win.title('WSL代码编辑器')


# -------------------------------------------2.菜单栏 Edit-----------------------------------------------------------

def Run():
    global filename
    global write1
    global write2
    def colorprint(textMess,txt, color='black'):
        #global textMess
        if textMess != None:
            if color != 'black':
                textMess.tag_config(color, foreground=color)
            textMess.insert(tk.END, txt, color)
            textMess.see(tk.END)
    def run_name(listbox):
        def colorprint(textMess,txt, color='black'):
            #global textMess
            if textMess != None:
                if color != 'black':
                    textMess.tag_config(color, foreground=color)
                textMess.insert(tk.END, txt, color)
                textMess.see(tk.END)
        try:
            import run
        except Exception as e:
            colorprint(listbox,e, color='red')
        #global run
    if filename:
        runfilename='run.py'
        mycopy(filename,runfilename)
        #rctrex = threading.Thread(target=run_name, args=(listbox,),daemon=True)
        #rctrex.join()
        windows=Tk()
        windows.title("WSL代码编辑器·正在运行")
        windows.geometry("500x300+200+100")
        name1="Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32"+"\n"+"========= RESTART: "+filename+" ========="
        name=name1
        listbox = ScrolledText(windows)
        listbox.place(x=0, y=0, width=500, height=300)
        colorprint(listbox,name, color='black')
        listbox.config(state=tk.DISABLED)
        name2=''
        def e():
            global filename,write1,write2
            f1=open('run_file.txt','w')
            f1.write(filename)
            f1.close()
            f1=open('run_size.txt','w')
            f1.write(str(write1))
            f1.close()
            f1=open('run_write.txt','w')
            f1.write(write2)
            f1.close()
            os.startfile(os.path.basename(__file__))
            exit()
        windows.protocol("WM_DELETE_WINDOW", e)
        rctrex = threading.Thread(target=run_name, args=(listbox,),daemon=True)
        rctrex.join()
        while True:
            try:
                import os
                f1=open('exit.txt','r')
                f1.close()
                os.remove('exit.txt')
                e()
            except Exception as e:
                pass
        #try:
        #    import run
        #except Exception as e:
        #    colorprint(listbox,e, color='red')
        #try:
        #    while True:
        #        name=name1+run.ghfthtrhtdehe
        #        """if run.gcrcberfegg==True:
        #            def awe():
        #                run.dfxregfwf=entry.get()
        #                r1.destroy()
        #            #windows=Tk()
        #            #windows.title("WSL代码编辑器·正在运行·input")
        #            #windows.geometry("500x300+200+100")
        #            r1=Tk()
        #            r1.title('WSL代码编辑器·正在运行·input')
        #            r1.geometry('300x250+300+300')

        #            #内容
        #            label=Label(r1,text=run.ehc5yh5h5h)#进入聊天室之前，先起一个
        #            label.pack(anchor='c',pady=20)

        #            #输入框
        #            entry=Entry(r1,width=18)
        #            entry.pack(anchor='c',pady=20)

        #            #按钮
        #            button=Button(r1,text='确认',command=awe)
        #            button.pack(anchor='c',pady=20)
        #            r1.mainloop()"""
        #        #wc=txtContent.get(0.0, tkinter.END)
        #        #name2=wc-name
        #        #print(run.ghfthtrhtdehe)
        #        #listbox.config(bg='white',fg='blue')
        #        listbox.insert(tkinter.END, name)
        #        #listbox.config(bg='white',fg='black')
        #        #listbox.insert(tkinter.END, name2)
        #        wc=txtContent.get(0.0, tkinter.END)
        #        #if len(name) <= len(wc):
        #        #    name2=''
        #        #    for i in range(0,len(wc)):
        #        #        print(wc[i]+'/n'+name[i])
        #        #        if name[i]!=wc[i]:
        #        #            name2+=wc[i]
        #        listbox.see(tkinter.END)                                    # ScrolledText组件方法，自动定位到结尾，否则只有消息在涨，窗口拖动条不动
        #        listbox.update()
        #        #time.sleep(0.01)
        #        listbox.delete(0.0, tk.END)
        #except Exception as e:
        #    #print(e)
        #    pass
        f1=open('run_file.txt','w')
        f1.write(filename)
        f1.close()
        f1=open('run_size.txt','w')
        f1.write(str(write1))
        f1.close()
        f1=open('run_write.txt','w')
        f1.write(write2)
        f1.close()
        os.startfile(os.path.basename(__file__))
        exit()
        import sys
        import run
        #run.rgwtgxrg()
        #sys.modules.pop('run')
        #del run
        #rctrex.join()
        #try:
        #    abc='rd/s/q run.py'
        #    ​os.system(abc)
        #except Exception as e:
        #    pass
        #kill(runfilename)
        #os.remove(runfilename)
        #process.kill(filename)
        #[process.kill() for process in psutil.process_iter() if process.name() == filename]
        #kill(filename)

def Insretimage():
    myfilename=tkinter.filedialog.askopenfilename(
        title="打开", filetypes=[("Text files", "*.png")])  # 打开路径框

    photo=PhotoImage(file=myfilename)
    txtContent.image_create(INSERT,image=photo)
    
    mainloop()

# 1.回退
def Undo():
    txtContent["undo"] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass

# 2.前进


def Redo():
    txtContent["undo"] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass

# 3.复制


def Copy():
    try:
        txtContent.clipboard_clear()  # 清空缓冲区
        txtContent.clipboard_append(txtContent.selection_get())  # 保存到缓冲区#txtContent.selection_get()
    except Exception as e:
        pass
    pass

# 4.剪切


def Cut():
    Copy()  # 复制文本
    try:
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)  # 删除文本编译器的选中文本
    except Exception as e:
        pass

# 5.粘贴
def paste():
    time.sleep (0.1)
    keyboard = Controller()
    keyboard.press(Key.ctrl.value )#Key.cmd.value
    keyboard.press('v')
    keyboard.release('v')
    #time.sleep (0.5)
    keyboard.release(Key.ctrl.value )
def Paste():
    #time.sleep (0.1)
    #keyboard = Controller()
    #keyboard.press(Key.ctrl.value )#Key.cmd.value
    #keyboard.press('v')
    #keyboard.release('v')
    #time.sleep (0.5)
    #keyboard.release(Key.ctrl.value )
    #keyboard.release('v')
    try:
        txtContent.insert(tkinter.SEL_FIRST,
                          txtContent.clipboard_get())  # 获取缓冲区文本
        #time.sleep (0.3)
        #keyboard = Controller()
        #keyboard.press(Key.cmd.value )#Key.ctrl.value
        #keyboard.press(tkinter.SEL_FIRST)
        #time.sleep (0.5)
        #keyboard.release(Key.ctrl.value )
        #keyboard.release('v')
        #v = virtkey.virtkey()
        #v.press_keysym(65507) #Ctrl键位
        #v.press_unicode(ord('v')) #模拟字母V
        #v.release_unicode(ord('v'))
        #v.release_keysym(65507)
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)  # 删除选中文本
        return
    except Exception as e:
        paste()
        pass

# 6.查找


def Search():
    textToSearch = tkinter.simpledialog.askstring(
        title="查找", prompt="你想找什么?")
    try:
        start = txtContent.search(textToSearch, 0.0, tkinter.END)
        if start:  # 查找到时，返回yes
            tkinter.messagebox.showinfo(title="存在", message="存在")
    except Exception as e:
        pass


# --------------------------------------------3.菜单栏 Help-----------------------------------------------------------
# 1，关于
def About():
    #tkinter.messagebox.showinfo(
    #    title="关于", message="作者:Wesley")  # 弹出信息框
    win32api.MessageBox(0, "作者:Wesley", "关于",win32con.MB_OK)
    pass

#使用说明

def Explain():
    windows=Tk()
    windows.title("使用说明")
    windows.geometry("500x300+200+100")
    #windows.overrideredirect(True)
    name="""
    			WSL代码编辑器使用说明

    [文件]功能:新建窗口、打开、保存、另存为、删除、关闭
    [编辑]功能:运行、上一部、下一步、复制、剪切、粘贴、查找
    [帮助]功能:关于、说明、字体"""
    listbox = ScrolledText(windows)
    listbox.place(x=0, y=0, width=500, height=300)
    listbox.insert(tkinter.END, name)
    listbox.update()
    listbox.config(state=tk.DISABLED)
    #try:
    #    while True:
    #        pass
    #        #listbox.insert(tkinter.END, name)
    #        #listbox.config(state=tk.DISABLED)
    #        #listbox.insert(tkinter.END, name)
    #        #listbox.see(tkinter.END)                                    # ScrolledText组件方法，自动定位到结尾，否则只有消息在涨，窗口拖动条不动
    #        #listbox.update()
    #        #time.sleep(0.01)
    #        #listbox.delete(0.0, tk.END)
    #except Exception as e:
    #    pass
    
#
write1=10
write2='宋体'
def Write1():
    global filename
    global txtContent
    global write1
    global write2
    def awe():
        global filename
        global txtContent
        global write1
        global write2
        #txtContent.destroy()
        if entry.get()!="":
            if int(entry.get())>3 and int(entry.get())<85:
                txtContent.config(font=(write2, int(entry.get())))
                write1=int(entry.get())
        """txtContent = tk.scrolledtext.ScrolledText(win, wrap=tk.WORD,font=("宋体",int(entry.get())))
        txtContent.pack(fill=tk.BOTH, expand=tkinter.YES)
        win.geometry('600x400+600+400')
        if filename:
            (filepath,tempfilename) = os.path.split(filename)
            (file_name,extension) = os.path.splitext(tempfilename)
            if filename!="":
                win.title('WSL文件编辑器-'+file_name)
            else:
                win.title('WSL文件编辑器')
            txtContent.delete(0.0, tk.END)  # 删除原来的文本
            #filename = tkinter.filedialog.askopenfilename(
            #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
            #filename = g.fileopenbox(default="*.txt")
            fp = open(filename, "rb")  # 读取文本
            txtContent.insert(tkinter.INSERT, "".join(
                fp.read().decode('GBK')))  # 解码插入到文本编辑器
            fp.close()  # 关闭指针
            textChanged.set(0)  # 字符串置0"""
    def 重置():
        global write1
        global write2
        write1=10
        txtContent.config(font=(write2, 10))
    r1=Tk()
    r1.title('WSL代码编辑器·字体')
    r1.geometry('300x270+300+300')

    #内容
    label=Label(r1,text='字体大小(4到84之内):')#进入聊天室之前，先起一个
    label.pack(anchor='c',pady=20)

    #输入框
    entry=Entry(r1,width=18)
    entry.pack(anchor='c',pady=20)

    #按钮
    button=Button(r1,text='确认',command=awe)
    button.pack(anchor='c',pady=20)

    button=Button(r1,text='重置',command=重置)
    button.pack(anchor='c',pady=20)
    #r1.mainloop()
def Write2():
    global filename
    global txtContent
    global write1
    global write2
    def awe():
        global filename
        global txtContent
        global write1
        global write2
        #txtContent.destroy()
        try:
            if entry.get()!="":
                if int(entry.get())>3 and int(entry.get())<85:
                    txtContent.config(font=(entry.get(), write1))
                    write2=entry.get()
        except Exception as e:
            pass
        """txtContent = tk.scrolledtext.ScrolledText(win, wrap=tk.WORD,font=("宋体",int(entry.get())))
        txtContent.pack(fill=tk.BOTH, expand=tkinter.YES)
        win.geometry('600x400+600+400')
        if filename:
            (filepath,tempfilename) = os.path.split(filename)
            (file_name,extension) = os.path.splitext(tempfilename)
            if filename!="":
                win.title('WSL文件编辑器-'+file_name)
            else:
                win.title('WSL文件编辑器')
            txtContent.delete(0.0, tk.END)  # 删除原来的文本
            #filename = tkinter.filedialog.askopenfilename(
            #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
            #filename = g.fileopenbox(default="*.txt")
            fp = open(filename, "rb")  # 读取文本
            txtContent.insert(tkinter.INSERT, "".join(
                fp.read().decode('GBK')))  # 解码插入到文本编辑器
            fp.close()  # 关闭指针
            textChanged.set(0)  # 字符串置0"""
    def 重置():
        global write1
        global write2
        write2="宋体"
        txtContent.config(font=("宋体", write1))
    r1=Tk()
    r1.title('WSL代码编辑器·字体')
    r1.geometry('300x270+300+300')

    #内容
    label=Label(r1,text='字体样貌:')#进入聊天室之前，先起一个
    label.pack(anchor='c',pady=20)

    #输入框
    entry=Entry(r1,width=18)
    entry.pack(anchor='c',pady=20)

    #按钮
    button=Button(r1,text='确认',command=awe)
    button.pack(anchor='c',pady=20)

    button=Button(r1,text='重置',command=重置)
    button.pack(anchor='c',pady=20)
    #r1.mainloop()
def Write():
    r1=Tk()
    r1.title('WSL代码编辑器·字体')
    r1.geometry('300x200+300+300')

    #内容
    #label=Label(r1,text='字体大小(4到84之内):')#进入聊天室之前，先起一个
    #label.pack(anchor='c',pady=20)

    #输入框
    #entry=Entry(r1,width=18)
    #entry.pack(anchor='c',pady=20)

    #按钮
    button=Button(r1,text='字体大小',command=Write1)
    button.pack(anchor='c',pady=20)

    button=Button(r1,text='字体样貌',command=Write2)
    button.pack(anchor='c',pady=20)
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------三、菜单栏框架----------------------------------
menu1 = tk.Menu(win)

# 菜单1 File
# ---------------------------------------------------------------------
submenu = tk.Menu(menu1, tearoff=0)

submenu.add_command(label="新建窗口", command=new)
#submenu.add_separator()
submenu.add_command(label="打开", command=Open)
#submenu.add_separator()
submenu.add_command(label="保存", command=Save)
#submenu.add_separator()
submenu.add_command(label="另存为", command=SaveAs)
#submenu.add_separator()
submenu.add_command(label="删除", command=Remove)
#submenu.add_separator()
submenu.add_command(label="关闭", command=Close)

menu1.add_cascade(label="文件", menu=submenu)
# -----------------------------------------------------------------------


# 菜单2  Edit
# -----------------------------------------------------------------------
submenu2 = tk.Menu(menu1, tearoff=0)

submenu2.add_command(label="运行", command=Run)
#submenu2.add_separator()
#submenu2.add_command(label="插入图片", command=Insretimage)
#submenu2.add_separator()
submenu2.add_command(label="上一步", command=Undo)
#submenu2.add_separator()
submenu2.add_command(label="下一步", command=Redo)
#submenu2.add_separator()
submenu2.add_command(label="复制", command=Copy)
#submenu2.add_separator()
submenu2.add_command(label="剪切", command=Cut)
#submenu2.add_separator()
submenu2.add_command(label="粘贴", command=Paste)
#submenu2.add_separator()
submenu2.add_command(label="查找", command=Search)

menu1.add_cascade(label="编辑", menu=submenu2)
# ------------------------------------------------------------------------


# 菜单3 Help
# ------------------------------------------------------------------------
submenu3 = tk.Menu(menu1, tearoff=0)

submenu3.add_command(label="关于", command=About)

submenu3.add_command(label="说明", command=Explain)

submenu3.add_command(label="字体", command=Write)

menu1.add_cascade(label="帮助", menu=submenu3)
# ------------------------------------------------------------------------


# 右键菜单
# ----------------------------------------------------------------------------------------------------------
right = tk.Menu(menu1, tearoff=0)
#1
#right.add_command(label="打开", command=Open)
#submenu.add_separator()
#right.add_command(label="保存", command=Save)
#submenu.add_separator()
#right.add_command(label="另存为", command=SaveAs)
#submenu.add_separator()
#right.add_command(label="删除", command=Remove)
#submenu.add_separator()
#right.add_command(label="关闭", command=Close)
#
#right.add_separator()
#2
right.add_command(label="上一步", command=Undo)
#submenu2.add_separator()
right.add_command(label="下一步", command=Redo)
#submenu2.add_separator()
right.add_command(label="复制", command=Copy)
#submenu2.add_separator()
right.add_command(label="剪切", command=Cut)
#submenu2.add_separator()
right.add_command(label="粘贴", command=Paste)
#submenu2.add_separator()
right.add_command(label="查找", command=Search)
#
#right.add_separator()
#3
#right.add_command(label="关于", command=About)
#right.add_command(label="说明", command=Explain)
#right.add_command(label="字体", command=Write)

# ------------------------------------------四、总体结构---------------------------------
# 1.菜单栏
win.config(menu=menu1)

# 2.滑动文本框

key=False
def keyPress(event):
    global key
    if key==False:
        textChanged.set(1)

def keydown(event):
    global key
    #print("c")
    def a():
        global key
        time.sleep(0.5)
        key=False
    key=True
    #t1=Thread(target=a)
    #t1.start()
"""
def key_():
    if key==True:
    key=False
"""
def key_s(event):
    global key
    if key==True:
        Save()
    key=False
def key_z(event):
    global key
    if key==True:
        Undo()
    key=False
def new_key_z(event):
    Undo()
def keykey(event):
    Redo()
def save(event):
    Save()
def keyup(event):
    global key
    key=False
#def key_():
win.protocol("WM_DELETE_WINDOW", quit_exit)
f1=open('run_size.txt','r')
write1=int(f1.read())
f1.close()
f1=open('run_size.txt','w')
f1.write('10')
f1.close()
f1=open('run_write.txt','r')
write2=f1.read()
f1.close()
f1=open('run_write.txt','w')
f1.write('宋体')
f1.close()
txtContent = tk.scrolledtext.ScrolledText(win, wrap=tk.WORD)#txtContent = tk.scrolledtext.ScrolledText(window, width=70, height=13,font=("宋体",18))
txtContent.pack(fill=tk.BOTH, expand=tkinter.YES)  # 创建
txtContent.config(font=(write2, write1))
Tkinter_ScrolledText_Code(txtContent)
#txtContent.focus_set()
#idc.color_config(txtContent)
#txtContent.focus_set()
#txtContent.config(bg='white',fg='black')
#p = idp.Percolator(txtContent)
#d = idc.ColorDelegator()
#p.insertfilter(d)

txtContent.bind("<Key>", keyPress)  # 绑定按键识别器
txtContent.bind("<Control_L>", keydown)
txtContent.bind("s", key_s)
txtContent.bind('<KeyRelease-Control_L>', keyup)
txtContent.bind("z", key_z)
#txtContent.bind("Control-KeyPress-S", save)
#txtContent.bind("Control-KeyPress-Z", new_key_z)
txtContent.bind("<Control-Shift-KeyPress-Z>", keykey)
#txtContent.bind("<Shift_L>", key_shift)
txtContent.bind("<Button-3>",popup)
#txtContent.bind("", key_)
#<Control_L>
if filename:
    mylist.append(filename)
    (filepath,tempfilename) = os.path.split(filename)
    (file_name,extension) = os.path.splitext(tempfilename)
    if filename!="":
        win.title('WSL文件编辑器-'+file_name)
    else:
        win.title('WSL文件编辑器')
    txtContent.delete(0.0, tk.END)  # 删除原来的文本
    #filename = tkinter.filedialog.askopenfilename(
    #    title="Open file", filetypes=[("Text files", "*.txt")])  # 打开路径框
    #filename = g.fileopenbox(default="*.txt")
    fp = open(filename,'r',encoding='utf-8',errors='ignore')  # 读取文本
    txtContent.insert(1.0, fp.read())  # 解码插入到文本编辑器
    fp.close()  # 关闭指针
    #textChanged.set(0)  # 字符串置0
win.mainloop()
"""
try:
    pass
except Exception as e:
    pass
"""
#raise Exception("")
