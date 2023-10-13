import socket
import threading
import json
import queue
IP = '127.0.0.1'
PORT = 11451
users = []  # 列表储存用户信息，三元元组，(用户socket， 用户名， 用户地址)
lock = threading.Lock()
mesg_que = queue.Queue()  # 队列存放二元元组 (用户地址， 用户消息)
online_list = []  # 在线队列，用于客户端显示在线列表


class Server:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def connect_to_client(self, client_socket, client_address):
        user = client_socket.recv(1024).decode('utf-8')  # 接收字符消息
        recv_message = json.loads(user)  # recv_message为字典格式，格式为{"sender", "receiver", "message"}

        for i in range(len(users)):  # 检索是否有重名用户并重新取名
            repeat = 0
            if recv_message["user"] == users[i][1]:
                repeat = repeat + 1
                print('用户已存在！')
                recv_message["user"] = recv_message["user"] + str(repeat)

        users.append((client_socket, recv_message["user"], client_address))  # 将用户加入用户队列
        online_list.append(recv_message["user"])
        print('新的连接:', client_address, ':', recv_message["user"], end='')
        mesg_que.put(json.dumps({"type": "user_list", "user_list": online_list, "receiver": "all_user"}))
        try:  # 进入接收循环
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                print(json.loads(data))  # 调试时使用，查看接收消息是否正常
                lock.acquire()  # 申请开锁
                try:
                    mesg_que.put(data)  # 放入消息队列
                finally:
                    lock.release()  # 释放锁
        except:
            print(recv_message["user"] + '断开连接')
            # 断开连接后删除用户
            self.delete_user(client_socket, recv_message["user"])
            client_socket.close()

    def delete_user(self, client_socket, user_name):  # 删除用户

        tempa = 0  # 更新用户表
        for i in users:
            if i[0] == client_socket:
                users.pop(tempa)
                break
            tempa += 1

        tempb = 0  # 更新在线队列
        for j in online_list:
            if j == user_name:
                online_list.pop(tempb)
                break
            tempb += 1
        mesg_que.put(json.dumps({"type": "user_list", "user_list": users, "receiver": "all_user"}))

    def send_data(self):
        while True:
            if not mesg_que.empty():  # 消息队列非空时
                que = mesg_que.get()  # 取出队列中的消息
                message = json.loads(que)  # 解包为字典格式
                if message["receiver"] == "all_user":  # 若为群发消息
                    for j in range(len(users)):
                        try:
                            users[j][0].send(json.dumps(message).encode())
                        except:
                            self.delete_user(users[0], users[1])
                else:                            # 否则为私聊消息
                    for i in range(len(users)):  # 搜寻目标用户并转发
                        if users[i][1] == message["receiver"]:
                            users[i][0].send(json.dumps(message).encode())
                            break

    def run(self):  # 启动多线程，每个线程对应一个客户端的接收
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip, self.port))
        sock.listen(5)
        thread = threading.Thread(target=self.send_data)  # 启动转发消息线程
        thread.start()
        while True:
            # 等待客户端来连接（主线程）
            # 每检测到一个连接就会创建一个子线程
            print("等待新的链接中……")
            client_socket, client_address = sock.accept()
            # 创建客户端接收子线程
            t = threading.Thread(target=self.connect_to_client, args=(client_socket, client_address))
            t.start()
        sock.close()


if __name__ == '__main__':
    server = Server(PORT, IP)
    server.run()
