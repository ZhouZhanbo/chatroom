import chatGUI
import tkinter
import interact


def send(*args):
    global t
    if not chatGUI.a.get():
        print("error")
        return
    t.add_information("user1", chatGUI.a.get())
    chatGUI.a.set("")
    chatGUI.listbox.insert(tkinter.END, "\n" + t.messages[-1][0] + ":" + t.messages[-1][1], 'blue')
    t.show()


def create_private_chat():
    global user, chat, t
    if t.u1 == user:
        t.close()
    t = interact.Interact(user, chat)
    chatGUI.listbox.delete(1.0, "end")
    for lines in t.messages:
        chatGUI.listbox.insert(tkinter.END, lines[0] + ":" + lines[1] + "\n", 'blue')


chat = "user2"
user = "user1"
t = interact.Interact(user, chat)
if __name__ == '__main__':
    create_private_chat()
    chatGUI.root.bind('<Return>', send)
    chatGUI.listbox.delete(1.0, "end")
    tkinter.mainloop()
    t.close()
