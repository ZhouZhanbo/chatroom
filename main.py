import sys
import time
import argparse
from vchat import Video_Server, Video_Client
from achat import Audio_Server, Audio_Client
# 主函数的逻辑是控制服务端和客户端分别启动，判断是否断开，总共有两个服务端，分别控制视频流和音频流，具体的逻辑在achat.py(音频流)和vchat.py(视频流)中

# 创建命令行参数解析器
parser = argparse.ArgumentParser()

# 添加命令行参数选项
parser.add_argument('--host', type=str, default='127.0.0.1')
parser.add_argument('--port', type=int, default=10087)
parser.add_argument('--noself', type=bool, default=False)
parser.add_argument('--level', type=int, default=1)
parser.add_argument('-v', '--version', type=int, default=4)

# 解析命令行参数
args = parser.parse_args()

# 获取解析后的参数值
IP = args.host
PORT = args.port
VERSION = args.version
SHOWME = not args.noself
LEVEL = args.level

if __name__ == '__main__':
    # 创建视频客户端和服务器对象
    vclient = Video_Client(IP, PORT, SHOWME, LEVEL, VERSION)
    vserver = Video_Server(PORT, VERSION)

    # 创建音频客户端和服务器对象
    aclient = Audio_Client(IP, PORT+1, VERSION)
    aserver = Audio_Server(PORT+1, VERSION)

    # 启动视频客户端、视频服务器、音频客户端和音频服务器
    vclient.start()
    vserver.start()
    aclient.start()
    aserver.start()
    while True:
        time.sleep(1)

        # 如果视频服务器或客户端连接断开，打印错误消息并退出
        if not vserver.is_alive() or not vclient.is_alive():
            print("Video connection lost...")
            sys.exit(0)

        # 如果音频服务器或客户端连接断开，打印错误消息并退出
        if not aserver.is_alive() or not aclient.is_alive():
            print("Audio connection lost...")
            sys.exit(0)