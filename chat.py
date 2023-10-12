import tkinter
import interact
import chatGUI


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


def revc(sender, message):
    tt = interact.Interact(user, sender)
    tt.add_information(sender, message)
    tt.close()


def create_chat():
    chatGUI.user = user
    chatGUI.create_chatGUI()
    chatGUI.entry.bind("<Return>", send)


def create_private_chat():
    global user, chat, t
    if t.u1 == user:
        t.close()   # 关闭上一个私聊
    t = interact.Interact(user, chat)
    chatGUI.listbox.delete(1.0, "end")
    for lines in t.messages:
        chatGUI.listbox.insert(tkinter.END, lines[0] + ":" + lines[1] + "\n", 'blue')


chat = "user2"
user = "user"
t = 0
