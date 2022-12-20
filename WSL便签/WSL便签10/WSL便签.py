import sqlite3
import tkinter as tk
from os.path import exists, expanduser
 
# 生成的数据库文件放到用户目录下
db_path = '%s/markBar' % expanduser("~")
 
#def not_color_window(win):
#    win.config(bg = '#add123')
#    win.wm_attributes('-transparentcolor','#add123')
# 数据库
def db_check(mode, value=None):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    result = 0
    # 初始化选项，创建表，插入初始数据
    if mode == 'init':
        f1=open('text10.txt','w')
        #cursor.execute("CREATE TABLE mark(mark_id VARCHAR NOT NULL,mark_info VARCHAR NOT NULL);")
        f1.write("右键双击切换无边框/边框模式\n\n无边框模式\n|-文本不可编辑\n|-窗口不可移动\n|-窗口大小不可改变\n|-无关闭按钮\n\n数据在程序目录下‘text.txt’文件")
        f1.close()
        #init_text = "重要事情说3遍！\n%s\n右键双击切换无边框/边框模式\n\n无边框模式\n|-文本不可编辑\n|-窗口不可移动\n|-窗口大小不可改变\n|-无关闭按钮\n\n数据在用户目录下markBar文件" % ('切换到无边框以保存备忘信息！\n' * 3)
        #cursor.execute("INSERT INTO mark(mark_id,mark_info) VALUES(\'2021\',\'%s\');" % init_text)
        result = 0
    # 更新选项，更新备注信息
    elif mode == 'update':
        f1=open('text10.txt','w')
        f1.write(value)
        f1.close()
        #cursor.execute("UPDATE mark SET mark_info=\'%s\' WHERE mark_id=\'2021\'" % value)
        result = 0
    # 查询选项，查询备注信息
    elif mode == 'select':
        try:
            f1=open('text10.txt','r')
            #cursor.execute('''SELECT mark_info from mark WHERE mark_id=\'2021\'''')
            result = f1.read()#cursor.fetchall()
            f1.close()
        except:
            db_check('init')
            result=db_check('select')
        #if result:
        #    result = result[0][0]
    # 关闭数据库连接，返回结果
    db.commit()
    db.close()
    return result
 
 
def mark_bar():
    def not_color_window(win):
        win.config(bg = '#add123')
        win.wm_attributes('-transparentcolor','#add123')
        win.overrideredirect(1)
    window = tk.Tk()
    #not_color_window(windows)
    #window = tk.Toplevel(windows)
    #window.transient(windows)
    # 设置为工具条窗口
    window.attributes("-toolwindow", 1)
    # 设置为置顶窗口
    window.attributes('-topmost', 1)
    window.title('WSL便笺')
    # 获取屏幕长宽
    width, height = window.winfo_screenwidth(), window.winfo_screenheight()
    # 按照屏幕比例放置并设置窗口大小
    window.geometry('%dx%d+%d+%d' % (width * 0.16, height * 0.38, width * 0.42, height * 0.1))
    # 字体大小根据屏幕高度变化
    font_size = int(height * 0.015)
    # 一个text组件用于编辑/显示内容（text在disable下仍然可以复制）
    #f1=open('text.txt','r')
    #text_mark = tk.Text(window, font=('微软雅黑', font_size), bg=f1.read())#'#ffefd5')
    #f1.close()
    text_mark = tk.Text(window, font=('微软雅黑', font_size), bg='#ffefd5')
    # 提示按钮，当便签启动时候覆盖在内容上面，点击以后自己关掉。做提示和内容保密的作用
    #bt_notice = tk.Button(window, text='提示\n\n左键单击将我关闭', font=('微软雅黑', 20))
    # 设置一个开关变量，表示边框状态，1为有边框
    var_switch = tk.IntVar(value=1)
 
    # 检测一下，如果数据库文件不存在则新建，存在直接查询便签内容
    if not exists(db_path):
        db_check('init')
        # 往text上插入数据库查询内容
        text_mark.insert('1.0', db_check('select'))
    else:
        # 将窗口设置为无边框
        #window.overrideredirect(1)
        var_switch.set(0)
        # 往text上插入数据库查询内容
        text_mark.insert('1.0', db_check('select'))
        # 将text设置为只读状态
        #text_mark.config(state=tk.DISABLED)
 
    def evt_title_switch(event):
        # 有边框时候,切换到无框，更新备忘数据，设置text为只读
        if var_switch.get():
            window.overrideredirect(1)
            var_switch.set(0)
            mark = text_mark.get('1.0', tk.END)
            db_check('update', mark)
            text_mark.config(state=tk.DISABLED)
        # 无框时候，切换到有框，设置text为可写
        else:
            window.overrideredirect(0)
            var_switch.set(1)
            text_mark.config(state=tk.NORMAL)
 
    # 绑定事件到鼠标右键双击
    window.bind('<Double-Button-3>', evt_title_switch)
 
    # 提示按钮自毁事件
    def evt_close_notice():
        pass
        #bt_notice.destroy()
 
    # 绑定自毁事件到按钮
    #bt_notice.config(command=evt_close_notice)
 
    # 按比例贴图
    text_mark.place(relx=0, rely=0, relwidth=1, relheight=1)
    # 如果启动时候就是有边框，则是第一次运行，不显示提示按钮
    #if not var_switch.get():
        #bt_notice.place(relx=0, rely=0, relwidth=1, relheight=1)
    def upp():
        db_check('update',value=text_mark.get(0.0, tk.END))
        window.destroy()
        #exit()
    window.protocol("WM_DELETE_WINDOW", upp)
    #window.overrideredirect(1)
    window.mainloop()
 
 
if __name__ == '__main__':
    mark_bar()
