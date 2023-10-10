import socket
import threading
import json
import queue
IP = '127.0.0.1'
PORT = 114514
users = []  # 列表储存用户信息，三元元组，(用户socket， 用户名， 用户地址)
lock = threading.Lock()
mesg_que = queue.Queue()  # 队列存放二元元组 (用户地址， 用户消息)


class Server:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def connect_to_client(self, client_socket, client_address):
        user = client_socket.recv(1024)
        user = user.decode('utf-8')

        for i in range(len(users)):  # 检索是否有重名用户并重新取名
            repeat = 0
            if user == users[i][1]:
                repeat = repeat + 1
                print('用户已存在！')
                user = '' + user + str(repeat)

        users.append((client_socket, user, client_address))  # 将用户加入用户队列
        print('新的连接:', client_address, ':', user, end='')
        try:  # 进入接收循环
            while True:
                data = client_socket.recv(1024)
                data = data.decode()
                lock.acquire()  # 申请开锁
                try:
                    mesg_que.put((client_address,data))  # 放入消息队列
                finally:
                    lock.release()  # 释放锁
        except:
            print(user + '断开连接')
            # 断开连接后删除用户
            self.delete_user(client_socket)
            client_socket.close()

    def delete_user(self, client_socket):  # 删除用户
        tempa = 0
        for i in users:
            if i[0] == client_socket:
                users.pop(tempa)
                break
            tempa += 1

    def send_data(self):
        while True:
            if not mesg_que.empty():
                data = ''
                reply_text = ''
                message = mesg_que.get()
                if isinstance(message[1], str):
                    for i in range(len(users)):
                        for j in range(len(users)):
                            if message[0] == users[j][2]:
                                print('消息来自user[{}]'.format(j))  # 调试用
                                data = ' ' + users[j][1] + ':' + message[1]
                                break
                        users[i][0].send(data.encode())

    def run(self):  # 启动多线程，每个线程对应一个客户端的接收
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(5)
        while True:
            # 等待客户端来连接（主线程）
            # 每检测到一个连接就会创建一个子线程
            client_socket, client_address = sock.accept()
            # 创建子线程
            t = threading.Thread(target=self.connect_to_client, args=(client_socket, client_address ))
            t.start()
        sock.close()






if __name__ == '__main__':
    server = Server(PORT, IP)
