import tkinter as tk
from tkinter import scrolledtext

# 聊天窗口
# 创建图形界面
user = "user"
root = []
listbox = []
listbox1 = []
a = []
entry = []
ii = 0


def showUsers():
    global listbox1, ii
    if ii == 1:
        listbox1.place(x=445, y=0, width=130, height=320)
        ii = 0
    else:
        listbox1.place_forget()  # 隐藏控件
        ii = 1
# 查看在线用户按钮


# 全局变量
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
    listbox.insert(tk.END, '欢迎加入聊天室 ！', 'blue')

    # 创建多行文本框, 显示在线用户
    listbox1 = tk.Listbox(root)
    listbox1.place(x=445, y=0, width=130, height=320)

    # 创建输入文本框和关联变量
    a = tk.StringVar()
    a.set('')
    entry = tk.Entry(root, width=120, textvariable=a)
    entry.place(x=5, y=350, width=570, height=40)
