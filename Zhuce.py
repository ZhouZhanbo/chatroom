import tkinter as tk
import tkinter.messagebox
import store


def create_zhuceroot():
    # 注册窗口
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
        Password1 = entrypassword.get()
        againPassword = entryagainpassword.get()
        if user1 and Password1 and againPassword:
            result = store.user_zhuce(user1,Password1,againPassword)
            if result == 1:
                tkinter.messagebox.showerror('温馨提示', message='用户名已被使用！')
                User.set("")
            elif result == 2:
                tkinter.messagebox.showerror('温馨提示', message='密码和确认密码不一致！')
                password.set("")
                againpassword.set("")
            else:
                tkinter.messagebox.showinfo('提示', message='注册成功！')
                zhuceRoot.destroy()

        else:
            tkinter.messagebox.showerror('温馨提示', message='用户名或密码或确认密码为空！')


    button = tk.Button(zhuceRoot, text='注册', command=zhuce, font=10)
    button.place(x=170, y=220, width=70, height=50)

    zhuceRoot.mainloop()




