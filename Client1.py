import socket
import threading
import json

IP = '127.0.0.1'
PORT = 11451
online_list = []  # 在线队列，用于客户端显示在线列表
chat = '【群聊】'
user = 'src2'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

init_message = {"sender": user,
                "receiver": "all_user",
                "message": "{}进入了聊天室".format(user)}
init_message = json.dumps(init_message)
init_message = init_message.encode('utf-8')
client_socket.send(init_message)


def send():  # 测试使用代码
    while True:
        data = input()
        message = {"sender": user,
                    "receiver": "src",
                    "message": data}
        message = json.dumps(message)
        message = message.encode('utf-8')
        client_socket.send(message)


def recv():  # 测试使用代码
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        data = json.loads(data)
        print(data["sender"], ":", data["message"])


if __name__ == '__main__':
    t = threading.Thread(target=send)
    t.start()
    recv()
