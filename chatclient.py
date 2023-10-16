import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText

IP = ''
PORT = ''
user = ''
listbox1 = ''  # 用于显示在线用户的列表框


#登陆窗口

root0 = tkinter.Tk()
root0.geometry("300x150")
root0.title('用户登陆窗口')
root0.resizable(0,0)
one = tkinter.Label(root0,width=300,height=150,bg="LightBlue")
one.pack()

IP0 = tkinter.StringVar()       #存储和跟踪用户输入
IP0.set('127.0.0.1:11451')
USER = tkinter.StringVar()
USER.set('Fan')

labelIP = tkinter.Label(root0,text='IP地址',bg="LightBlue")
labelIP.place(x=20,y=20,width=100,height=40)
entryIP = tkinter.Entry(root0, width=60, textvariable=IP0)
entryIP.place(x=120,y=25,width=100,height=30)

labelUSER = tkinter.Label(root0,text='用户名',bg="LightBlue")
labelUSER.place(x=20,y=70,width=100,height=40)
entryUSER = tkinter.Entry(root0, width=60, textvariable=USER)
entryUSER.place(x=120,y=75,width=100,height=30)

def Login(*args):
	global IP, PORT, user
	IP, PORT = entryIP.get().split(':')     #获取输入，将其分割成IP和PORT，然后分别赋值给全局变量IP和PORT
	user = entryUSER.get()          #获取用户输入，并赋值给user
	if not user:
		tkinter.messagebox.showwarning('warning', message='用户名为空!')
	else:
		root0.destroy()

loginButton = tkinter.Button(root0, text ="登录", command = Login,bg="Yellow")
loginButton.place(x=135,y=110,width=40,height=25)
root0.bind('<Return>', Login)

root0.mainloop()

# 建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))

init_message = {"sender": user,
                "receiver": "all_user",
                "message": "{}进入了聊天室".format(user)}
init_message = json.dumps(init_message)
init_message = init_message.encode()
s.send(init_message)

# 聊天窗口
root1 = tkinter.Tk()
root1.geometry("640x480")
root1.title('群聊')
root1.resizable(0,0)

# 消息界面
listbox = ScrolledText(root1)
listbox.place(x=5, y=0, width=640, height=320)
listbox.tag_config('tag1', foreground='red',backgroun="yellow")
listbox.insert(tkinter.END, '欢迎进入群聊，大家开始聊天吧!', 'tag1')

INPUT = tkinter.StringVar()
INPUT.set('')
entryIuput = tkinter.Entry(root1, width=120, textvariable=INPUT)
entryIuput.place(x=5,y=320,width=580,height=170)

# 在线用户列表
listbox1 = tkinter.Listbox(root1)
listbox1.place(x=510, y=0, width=130, height=320)

def send(*args):
    message =  {"sender": user,
                "receiver": "all_user",
                "message": entryIuput.get() }
    message = json.dumps(message)
    s.send(message.encode())
    INPUT.set('')

sendButton = tkinter.Button(root1, text ="\n发\n\n\n送",anchor = 'n',command = send,font=('Helvetica', 18),bg = 'white')
sendButton.place(x=585,y=320,width=55,height=300)
root1.bind('<Return>', send)


def receive():
	while True:
		data = s.recv(1024)
		data = data.decode()
		recv_message = json.loads(data)
		if isinstance(recv_message,list) :		#收到的消息是在线用户列表，更新其显示

			listbox1.delete(0, tkinter.END)
			listbox1.insert(tkinter.END, "当前在线用户")
			listbox1.insert(tkinter.END, "------Group chat-------")
			for x in range(len(recv_message)):
				listbox1.insert(tkinter.END, recv_message[x])
		else:
			message = recv_message["sender"] + ':'+ recv_message["message"]
			userName = recv_message["sender"]
			chatwith = recv_message["receiver"]
			message = '\n' + message
			if chatwith == "all_user":   # 群聊
				if userName == user:
					listbox.insert(tkinter.END, message)
				else:
					listbox.insert(tkinter.END, message)
			#此处写私聊
			#
			#



r = threading.Thread(target=receive)
r.start()  # 开始线程接收信息

root1.mainloop()
s.close()

