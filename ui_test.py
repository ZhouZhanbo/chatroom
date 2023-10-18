import pyaudio
import tkinter as tk
import subprocess
import os
import signal

server_process = None
client_process = None

def start_voice_chat():
    global server_process, client_process
    HOST = host_entry.get()  # 获取输入的主机号

    # Start the server script
    server_process = subprocess.Popen(['python', 'groupserver_audio.py', HOST], shell=True)

    # Start the client script
    client_process = subprocess.Popen(['python', 'groupclient_audio.py', HOST], shell=True)

def stop_voice_chat():
    global server_process, client_process
    if server_process:
        server_process.send_signal(signal.CTRL_BREAK_EVENT)  # Send Ctrl+Break signal to terminate the server
        server_process.wait()  # Wait for the server to terminate

    if client_process:
        client_process.send_signal(signal.CTRL_BREAK_EVENT)  # Send Ctrl+Break signal to terminate the client
        client_process.wait()  # Wait for the client to terminate

# 创建主窗口
root = tk.Tk()
root.title("语音聊天")

# 创建文本输入框
host_label = tk.Label(root, text="主机号:")
host_label.pack()

host_entry = tk.Entry(root)
host_entry.pack()

# 创建一个按钮来启动语音聊天
start_button = tk.Button(root, text="开始语音聊天", command=start_voice_chat)
start_button.pack()

# 创建一个按钮来停止语音聊天
stop_button = tk.Button(root, text="停止语音聊天", command=stop_voice_chat)
stop_button.pack()

# 启动GUI主循环
root.mainloop()
