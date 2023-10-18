import tkinter as tk
import tkinter.messagebox
import store

def create_changepwroot():
    # 修改密码窗口
    changepwRoot = tk.Tk()
    changepwRoot.title("修改密码")
    changepwRoot["height"] = 300
    changepwRoot["width"] = 400
    changepwRoot.resizable(0, 0)  # 限制窗口大小

    # 用户名，旧密码，新密码，确认新密码
    User = tk.StringVar()
    User.set("")
    oldpassword = tk.StringVar()
    oldpassword.set("")
    newpassword = tk.StringVar()
    newpassword.set("")
    againnewpassword = tk.StringVar()
    againnewpassword.set("")

    # 用户名标签
    labelUser = tk.Label(changepwRoot, text='用户名', font=("宋体", 12))
    labelUser.place(x=60, y=50, width=100, height=30)

    entryUser = tk.Entry(changepwRoot, width=80, textvariable=User, font=12)
    entryUser.place(x=160, y=50, width=130, height=30)

    # 旧密码标签
    labeloldpassword = tk.Label(changepwRoot, text='旧密码', font=("宋体", 12))
    labeloldpassword.place(x=70, y=100, width=80, height=30)

    entryoldpassword = tk.Entry(changepwRoot, width=80, textvariable=oldpassword, font=15)
    entryoldpassword.place(x=160, y=100, width=130, height=30)

    # 新密码标签
    labelnewpassword = tk.Label(changepwRoot, text='新密码', font=("宋体", 12))
    labelnewpassword.place(x=70, y=150, width=80, height=30)

    entrynewpassword = tk.Entry(changepwRoot, width=80, textvariable=newpassword, font=15)
    entrynewpassword.place(x=160, y=150, width=130, height=30)

    # 确认新密码标签
    labelagainnewpassword = tk.Label(changepwRoot, text='确认新密码', font=("宋体", 12))
    labelagainnewpassword.place(x=70, y=200, width=80, height=30)

    entryagainnewpassword = tk.Entry(changepwRoot, width=80, textvariable=againnewpassword, font=15)
    entryagainnewpassword.place(x=160, y=200, width=130, height=30)
    def change(*args):
        print("hello")
        user = entryUser.get()
        Oldpassword = entryoldpassword.get()
        Newpassword = entrynewpassword.get()
        againnewPassword = entryagainnewpassword.get()
        if user and Oldpassword and Newpassword and againnewPassword:
            result = store.user_change(user, Oldpassword, Newpassword,againnewPassword)
            if result == 1:#用户不存在
                tkinter.messagebox.showerror('温馨提示', message='用户名不存在，请注册！')
            elif result == 2:#旧密码错误
                tkinter.messagebox.showerror('温馨提示', message='旧密码错误！')
            elif result == 3:#新密码和确认密码不一致
                tkinter.messagebox.showerror('温馨提示', message='新密码和确认密码不一致！')
            else:
                tkinter.messagebox.showinfo('提示', message='修改密码成功！')
                changepwRoot.destroy()


        else:
            tkinter.messagebox.showerror('温馨提示', message='用户名或旧密码或新密码或确认密码为空！')

    button = tk.Button(changepwRoot, text='修改', command=change, font=10)
    button.place(x=170, y=250, width=70, height=40)

    changepwRoot.mainloop()

