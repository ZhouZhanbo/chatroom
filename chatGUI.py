import tkinter as tk
from tkinter import scrolledtext
import chat
# 全局变量
user = "user"
root = []
listbox = []
listbox1 = []
a = []
entry = []

# 聊天界面创建
def create_chatGUI():
    global user, root, listbox, listbox1, a, entry
    root = tk.Tk()
    root.title(user)  # 窗口命名为用户名
    root['height'] = 400
    root['width'] = 580
    root.resizable(0, 0)  # 限制窗口大小
    # 更改logo
    root.iconphoto(False, tk.PhotoImage(file='icon/logo.png'))
    # 创建多行文本框
    listbox = scrolledtext.ScrolledText(root)
    listbox.place(x=5, y=0, width=570, height=320)
    # 文本框使用的字体颜色
    listbox.tag_config('red', foreground='red')
    listbox.tag_config('blue', foreground='blue')
    listbox.tag_config('green', foreground='green')
    listbox.tag_config('pink', foreground='pink')
    listbox.insert(tk.END, '欢迎加入聊天室(默认为群聊) ！', 'red')

    # 列表动，滚动条跟着动
    listbox1 = tk.Listbox(root)
    # 创建多行文本框, 显示在线用户
    listbox1.place(x=445, y=0, width=130, height=320)
    # 创建用户列表的滚动条
    sc1 = tk.Scrollbar(listbox1)
    sc1.pack(side=tk.RIGHT,  fill=tk.Y)
    # 滚动条动，列表跟着动
    sc1.config(command=listbox1.yview)

    # 创建输入文本框和关联变量
    a = tk.StringVar()
    a.set('')
    entry = tk.Entry(root, width=300, textvariable=a)
    entry.place(x=5, y=350, width=570, height=40)

    # 关闭窗口按钮
    but1 = tk.Button(entry, text='关闭', command=root.destroy, font=15)
    but1.place(x=445, y=10, width=50, height=30)
    # 传输文件按钮
    but2 = tk.Button(root, command="")
    but2.config(image=tk.PhotoImage(file=".\\icon\\voice.png"))
    but2.place(x=10, y=320, width=30, height=30)
    # 语音通话按钮
    but3 = tk.Button(root, text='语音通话', command="", font=15)
    but3.place(x=110, y=320, width=100, height=30)
    # 视频通话按钮
    but4 = tk.Button(root, text='视频通话', command="", font=15)
    but4.place(x=210, y=320, width=100, height=30)