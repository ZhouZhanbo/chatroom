import tkinter as tk
import tkinter.messagebox


# 登陆窗口
loginRoot = tk.Tk()
loginRoot.title("登录")
loginRoot["height"] = 250
loginRoot["width"] = 400
loginRoot.resizable(0, 0)  # 限制窗口大小

User = tk.StringVar()
User.set("")
password = tk.StringVar()
password.set("")

# 服务器标签
labelUser = tk.Label(loginRoot, text='用户名', font=("宋体", 12))
labelUser.place(x=60, y=70, width=100, height=30)

entryUser = tk.Entry(loginRoot, width=80, textvariable=User, font=12)
entryUser.place(x=160, y=70, width=130, height=30)

# 用户名标签
labelpassword = tk.Label(loginRoot, text='密码', font=("宋体", 12))
labelpassword.place(x=70, y=110, width=80, height=30)

entrypassword = tk.Entry(loginRoot, width=80, textvariable=password, font=15)
entrypassword.place(x=160, y=110, width=130, height=30)


# 登录按钮
def login(*args):
    global user, Password
    user = entryUser.get()
    Password = entrypassword.get()
    if user and Password:
        if len(Password) > 16:
            tkinter.messagebox.showerror('温馨提示', message='密码不能超过16位！')
            password.set("")
        else:
            loginRoot.destroy()  # 关闭窗口
    else:
        tkinter.messagebox.showerror('温馨提示', message='用户名或密码为空！')





loginRoot.bind('<Return>', login)            # 回车绑定登录功能
but = tk.Button(loginRoot, text='登录', command=login, font=15)
but.place(x=165, y=160, width=70, height=30)
tkinter.mainloop()


