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

    # 创建多行文本框
    listbox = scrolledtext.ScrolledText(root)
    listbox.place(x=5, y=0, width=570, height=320)
    # 文本框使用的字体颜色
    listbox.tag_config('red', foreground='red')
    listbox.tag_config('blue', foreground='blue')
    listbox.tag_config('green', foreground='green')
    listbox.tag_config('pink', foreground='pink')
    listbox.insert(tk.END, '欢迎加入聊天室(默认为群聊) ！', 'blue')

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
    entry = tk.Entry(root, width=120, textvariable=a)
    entry.place(x=5, y=350, width=570, height=40)

