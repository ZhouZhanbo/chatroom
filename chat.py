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


t = interact.Interact("user1", "user2")
for lines in t.messages:
    chatGUI.listbox.insert(tkinter.END, "\n" + lines[0] + ":" + lines[1], 'blue')
chatGUI.root.bind('<Return>', send)

tkinter.mainloop()
