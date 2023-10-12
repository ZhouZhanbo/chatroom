import tkinter as tk
import tkinter.messagebox

# 登录按钮
IP = ""
PORT = ""
user = ""
labelIP, entryIP, labelUser = [0, 0, 0]
loginRoot = 0
entryUser = 0
IP1 = 0
User = 0


def login(*args):
    global IP, PORT, user, entryUser
    IP, PORT = entryIP.get().split(':')  # 获取IP和端口号
    PORT = int(PORT)                     # 端口号需要为int类型
    user = entryUser.get()
    if not user:
        tkinter.messagebox.showerror('温馨提示', message='请输入任意的用户名！')
    else:
        loginRoot.destroy()                  # 关闭窗口


def create_login():
    global IP, PORT, user, labelIP, entryIP, labelUser, loginRoot, IP1, User, entryUser
    IP = ""
    PORT = ""
    user = "user1"
    # 登陆窗口
    loginRoot = tk.Tk()
    loginRoot.title("聊天室")
    loginRoot["height"] = 250
    loginRoot["width"] = 400
    loginRoot.resizable(0, 0)  # 限制窗口大小

    IP1 = tk.StringVar()
    IP1.set("127.0.0.1:8888")  # 默认显示的ip和端口
    User = tk.StringVar()
    User.set("")

    # 服务器标签
    labelIP = tk.Label(loginRoot, text='地址:端口', font=("宋体", 12))
    labelIP.place(x=60, y=70, width=100, height=30)

    entryIP = tk.Entry(loginRoot, width=80, textvariable=IP1, font=12)
    entryIP.place(x=160, y=70, width=130, height=30)

    # 用户名标签
    labelUser = tk.Label(loginRoot, text='昵称', font=("宋体", 12))
    labelUser.place(x=70, y=110, width=80, height=30)

    entryUser = tk.Entry(loginRoot, width=80, textvariable=User, font=15)
    entryUser.place(x=160, y=110, width=130, height=30)
    loginRoot.bind('<Return>', login)  # 回车绑定登录功能
    but = tk.Button(loginRoot, text='登录', command=login, font=15)
    but.place(x=165, y=160, width=70, height=30)
    tkinter.mainloop()



