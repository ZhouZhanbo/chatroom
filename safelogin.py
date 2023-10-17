import tkinter as tk
import tkinter.messagebox
import store
import Zhuce
import socket
import json

user = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 11451))  # 网络链接

def zhuce(*args):
    print("注册")
    loginRoot.destroy()
    Zhuce.create_zhuceroot()
    create_loginroot()

def create_loginroot():
    # 登陆窗口
    global loginRoot
    loginRoot = tk.Tk()
    loginRoot.title("登录")
    loginRoot["height"] = 250
    loginRoot["width"] = 400
    loginRoot.resizable(0, 0)  # 限制窗口大小

    User = tk.StringVar()
    User.set("")
    password = tk.StringVar()
    password.set("")

    # 用户名标签
    labelUser = tk.Label(loginRoot, text='用户名', font=("宋体", 12))
    labelUser.place(x=60, y=70, width=100, height=30)

    entryUser = tk.Entry(loginRoot, width=80, textvariable=User, font=12)
    entryUser.place(x=160, y=70, width=130, height=30)

    # 密码标签
    labelpassword = tk.Label(loginRoot, text='密  码', font=("宋体", 12))
    labelpassword.place(x=70, y=110, width=80, height=30)

    entrypassword = tk.Entry(loginRoot, width=80, textvariable=password, font=15)
    entrypassword.place(x=160, y=110, width=130, height=30)

    # 登录按钮
    def login(*args):
        global user, Password
        user = entryUser.get()
        Password = entrypassword.get()

        data = {"type": "login", "user": user, "password": Password}  # 发给服务器
        data = json.dumps(data)
        data = data.encode('utf-8')
        s.send(data)

        recv_data = s.recv(1024).decode('utf-8')  # 接收返回信息
        recv_data = json.loads(recv_data)
        if recv_data["type"] == "login":  # 登录消息
            if recv_data["message"] == "OK":
                pass  # 登录成功操作
            elif recv_data["message"] == "ERROR":
                pass  # 错误操作
        if recv_data["type"] == "register":
            if recv_data["message"] == "OK":
                pass  # 注册成功操作
            elif recv_data["message"] == "ERROR":
                pass  # 错误操作

        if user and Password:
            # if len(Password) > 16:
            # tkinter.messagebox.showerror('温馨提示', message='密码不能超过16位！')
            # password.set("")
            # else:
            result = store.check_user(user, Password)
            if result == 1:
                tkinter.messagebox.showerror('提示', message='您还未注册！')
            elif result == 2:
                tkinter.messagebox.showinfo('提示', message='登录成功！')
                loginRoot.destroy()
            else:
                tkinter.messagebox.showerror('提示', message='密码错误！')
                password.set("")

        else:
            tkinter.messagebox.showerror('温馨提示', message='用户名或密码为空！')

    loginRoot.bind('<Return>', login)  # 回车绑定登录功能
    but = tk.Button(loginRoot, text='登录', command=login, font=15)
    but.place(x=100, y=160, width=70, height=30)
    but2 = tk.Button(loginRoot, text='注册', command=zhuce, font=15)
    but2.place(x=230, y=160, width=70, height=30)
    loginRoot.mainloop()

create_loginroot()



