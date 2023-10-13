import socket
import chat
import loginGUI
import json
import threading


def recv():
    while True:
        try:
            data = s.recv(1024)
            data = data.decode()
            data = json.loads(data)
            if data["type"] == "user_list":
                chat.show_users(data["user_list"])
            elif data["type"] == "message":
                chat.revc(data["sender"], data["message"])
        except:
            print("已经断开链接")
            break


def send(*args):
    data = {"type": "message", "sender": chat.user, "receiver": chat.chat, "message": chat.chatGUI.a.get()}
    chat.send()
    data = json.dumps(data)
    s.send(data.encode())


chat.user = loginGUI.user
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((loginGUI.IP, loginGUI.PORT))
if chat.user:
    s.send(json.dumps({"type": "user", "user": chat.user}).encode())
else:
    s.send("no".encode())
chat.create_chat()
chat.chatGUI.entry.bind("<Return>", send)
r = threading.Thread(target=recv)
r.start()
chat.tkinter.mainloop()
s.close()
