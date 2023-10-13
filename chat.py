import tkinter
import interact
import chatGUI


# 发送消息，缺一行发送给服务器消息
def send(*args):
    global t, user
    if not chatGUI.a.get():
        print("error")
        return
    t.add_information(user, chatGUI.a.get())
    chatGUI.a.set("")
    chatGUI.listbox.insert(tkinter.END, "\n" + t.messages[-1][0] + ":" + t.messages[-1][1], 'blue')
    if __name__ == '__main__':
        t.show()


# 接受消息，仅接受消息添加到对应的文件里
def revc(sender, message):
    tt = interact.Interact(user, sender)
    tt.add_information(sender, message)
    tt.close()


# 创建chat界面
def create_chat():
    global t
    chatGUI.user = user
    chatGUI.create_chatGUI()
    t = interact.Interact(user, "all_user")


# 在主界面显示对应的聊天记录，在点击对应私聊用户后需要调用
def create_private_chat():
    global user, t, chat
    if t.u1 == user:
        t.close()   # 关闭上一个私聊
    t = interact.Interact(user, chat)
    chatGUI.listbox.delete(1.0, "end")
    for lines in t.messages:
        chatGUI.listbox.insert(tkinter.END, lines[0] + ":" + lines[1] + "\n", 'blue')


def show_users(users):
    chatGUI.listbox1.delete(0, "end")
    for use in users:
        chatGUI.listbox1.insert("end", use)


user = "user"
chat = "user2"
t = 0
