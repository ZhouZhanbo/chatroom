import socket
import threading
import json

IP = '127.0.0.1'
PORT = 11451
online_list = []  # 在线队列，用于客户端显示在线列表
chat = '【群聊】'
user = 'src'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

init_message = {"sender": user,
                "receiver": "all_user",
                "message": "{}进入了聊天室".format(user)}
init_message = json.dumps(init_message)
init_message = init_message.encode()
client_socket.send(init_message)


def recv():
    while True:
        pass


if __name__ == '__main__':
    recv()