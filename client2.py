import socket
import chat
import chatGUI
import loginGUI
import json
import threading
import tkinter as tk


# 接收消息
def recv():
    while True:
        try:
            data = s.recv(1024)
            data = data.decode()
            data = json.loads(data)
            if data["type"] == "user_list":  # 接收的消息是用户列表，则重新加载用户
                chat.show_users(data["user_list"])
            elif data["type"] == "message":  # 接收的消息是文本消息
                chat.revc(data["receiver"], data["sender"], data["message"])
                for i in range(-1,chatGUI.listbox1.size()):  # 来消息时提醒：发送方背景变红
                    if chatGUI.listbox1.get(i) == data["sender"] \
                            and chatGUI.listbox1.curselection()[0] != i:  # 当已经选中该发方则不变红
                        chatGUI.listbox1.itemconfigure((i,), bg="red")
        except:
            print("已经断开链接")
            break


# 发送消息
def send(*args):
    data = {"type": "message", "sender": chat.user, "receiver": chat.chat, "message": chat.chatGUI.a.get()}
    chat.send()
    data = json.dumps(data)
    s.send(data.encode())


chat.user = loginGUI.user
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((loginGUI.IP, loginGUI.PORT))   # 网络链接
if chat.user:
    s.send(json.dumps({"type": "user", "user": chat.user}).encode())  # 发送用户名
else:
    s.send("no".encode())
chat.create_chat()   # 创建聊天界面
chat.chatGUI.entry.bind("<Return>", send)
# 回车绑定发送功能
but = tk.Button(chat.chatGUI.entry, text='发送', command=send, font=15)
but.place(x=500, y=10, width=50, height=30)
r = threading.Thread(target=recv)  # 启动接受消息线程
r.start()
chat.tkinter.mainloop()
# 关闭链接，把缓存的消息放进文件
s.close()
chat.t.close()
