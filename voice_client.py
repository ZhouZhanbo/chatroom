import sys
import socket
import pyaudio
from array import array
import threading

class AudioChatClient:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.BufferSize = 4096
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.audio = pyaudio.PyAudio()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stream = self.audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )

        self.running = True  # Flag to control thread execution

    def send_audio(self):
        while self.running:
            data = self.stream.read(self.CHUNK)
            self.client.sendall(data)

    def receive_audio(self):
        while self.running:
            data = self.recv_all(self.BufferSize)
            self.stream.write(data)

    def recv_all(self, size):
        data_bytes = b''
        while len(data_bytes) != size:
            to_read = size - len(data_bytes)
            if to_read > (4 * self.CHUNK):
                data_bytes += self.client.recv(4 * self.CHUNK)
            else:
                data_bytes += self.client.recv(to_read)
        return data_bytes

    def connect_to_server(self):
        try:
            self.client.connect((self.HOST, self.PORT))
        except ConnectionRefusedError:
            print("Connection to the server failed. Make sure the server is running.")
            sys.exit(1)

    def stop_threads(self):
        self.running = False

    def start_chat(self):
        receive_audio_thread = threading.Thread(target=self.receive_audio)
        send_audio_thread = threading.Thread(target=self.send_audio)

        receive_audio_thread.start()
        send_audio_thread.start()

        try:
            while self.running:
                pass
        except KeyboardInterrupt:
            print("Chat ended. Closing threads.")

        self.stop_threads()  # Signal threads to stop

        receive_audio_thread.join()
        send_audio_thread.join()

        self.client.close()
        self.audio.terminate()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        HOST = sys.argv[1]
        print(f"Connecting to host: {HOST}")
        PORT = 4000
        client = AudioChatClient(HOST, PORT)
        client.connect_to_server()
        client.start_chat()
    else:
        print("Please provide a host address as a command-line argument.")
