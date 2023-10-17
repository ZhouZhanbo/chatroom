import chat
import interact
import tkinter
import loginGUI

chat.t = interact.Interact(loginGUI.user, chat.chat)
chat.user = loginGUI.user
chat.create_chat()
chat.create_private_chat("user2")
tkinter.mainloop()
chat.t.close()
