import tkinter as tk
import tkinter.messagebox
import socket
import json

user = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 11451))  # 网络链接

def create_zhuceroot():
    # 注册窗口
    global s
    zhuceRoot = tk.Tk()
    zhuceRoot.title("注册")
    zhuceRoot["height"] = 300
    zhuceRoot["width"] = 400
    zhuceRoot.resizable(0, 0)  # 限制窗口大小

    User = tk.StringVar()
    User.set("")
    password = tk.StringVar()
    password.set("")
    againpassword = tk.StringVar()
    againpassword.set("")

    # 用户名标签
    labelUser = tk.Label(zhuceRoot, text='用户名', font=("宋体", 12))
    labelUser.place(x=60, y=50, width=100, height=30)

    entryUser = tk.Entry(zhuceRoot, width=80, textvariable=User, font=12)
    entryUser.place(x=160, y=50, width=130, height=30)

    # 密码标签
    labelpassword = tk.Label(zhuceRoot, text='密  码', font=("宋体", 12))
    labelpassword.place(x=70, y=110, width=80, height=30)

    entrypassword = tk.Entry(zhuceRoot, width=80, textvariable=password, font=15)
    entrypassword.place(x=160, y=110, width=130, height=30)

    # 确认密码标签
    labelagainpassword = tk.Label(zhuceRoot, text='确认密码', font=("宋体", 12))
    labelagainpassword.place(x=70, y=170, width=80, height=30)

    entryagainpassword = tk.Entry(zhuceRoot, width=80, textvariable=againpassword, font=15)
    entryagainpassword.place(x=160, y=170, width=130, height=30)

    def zhuce(*args):
        print("hello")
        user1 = entryUser.get()
        Password = entrypassword.get()
        againPassword = entryagainpassword.get()
        if user1 == "" or Password == "" or againPassword == "":
            tkinter.messagebox.showerror('提示', message='用户名或密码为空')
            return
        data = {"type": "register", "user": user1, "password": Password, "again_Password": againPassword}  # 发给服务器
        s.send(json.dumps(data).encode('utf-8'))
        recv_data = s.recv(1024).decode('utf-8')  # 接收返回信息
        print(recv_data)
        recv_data = json.loads(recv_data)
        if recv_data["type"] == "register":
            if recv_data["message"] == "OK":
                zhuceRoot.destroy()
            elif recv_data["message"] == "Error_user_exists":
                tkinter.messagebox.showerror('提示', message='注册失败，用户名已被使用！')
            elif recv_data["message"] == "Error_password_diff":
                tkinter.messagebox.showerror('提示', message='密码不一致！')

    button = tk.Button(zhuceRoot, text='注册', command=zhuce, font=10)
    button.place(x=170, y=220, width=70, height=50)

    zhuceRoot.mainloop()


def zhuce(*args):
    print("注册")
    loginRoot.destroy()
    create_zhuceroot()
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
        user1 = entryUser.get()
        Password = entrypassword.get()
        if user1 == "" or Password == "":
            tkinter.messagebox.showerror('温馨提示', message='用户名或密码为空！')
            return
        data = {"type": "login", "user": user1, "password": Password}  # 发给服务器
        s.send(json.dumps(data).encode('utf-8'))

        recv_data = s.recv(1024).decode('utf-8')  # 接收返回信息
        recv_data = json.loads(recv_data)
        if recv_data["type"] == "login":  # 登录消息
            if recv_data["message"] == "OK":
                user = user1
                loginRoot.destroy()
            elif recv_data["message"] == "Error_user_online":
                tkinter.messagebox.showerror('提示', message='用户已经登录！')
            elif recv_data["message"] == "Error_register":
                tkinter.messagebox.showerror('提示', message='用户未注册！')
            elif recv_data["message"] == "Error_password":
                tkinter.messagebox.showerror('提示', message='密码错误！')

            # if len(Password) > 16:
            # tkinter.messagebox.showerror('温馨提示', message='密码不能超过16位！')
            # password.set("")
            # else:

    loginRoot.bind('<Return>', login)  # 回车绑定登录功能
    but = tk.Button(loginRoot, text='登录', command=login, font=15)
    but.place(x=100, y=160, width=70, height=30)
    but2 = tk.Button(loginRoot, text='注册', command=zhuce, font=15)
    but2.place(x=230, y=160, width=70, height=30)
    loginRoot.mainloop()

create_loginroot()



