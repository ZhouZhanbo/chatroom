import sys
import socket
from threading import Thread
import signal

class VoiceChatServer:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.BufferSize = 4096
        self.addresses = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen(2)
        self.running = True  # Flag to control server and threads

    def accept_connections(self):
        while self.running:
            try:
                client, addr = self.server.accept()
                print("{} is connected!".format(addr))
                self.addresses[client] = addr
                Thread(target=self.handle_client_connection, args=(client,)).start()
            except Exception as e:
                print(f"Error accepting connection: {e}")

    def handle_client_connection(self, client):
        while self.running:
            try:
                data = client.recv(self.BufferSize)
                if not data:
                    break
                self.broadcast_sound(client, data)
            except Exception as e:
                print(f"Error handling client connection: {e}")
                break

    def broadcast_sound(self, client_socket, data_to_be_sent):
        for client in self.addresses:
            if client != client_socket:
                try:
                    client.sendall(data_to_be_sent)
                except Exception as e:
                    print(f"Error broadcasting sound to client: {e}")

    def stop_server(self):
        self.running = False  # Stop the server
        self.server.close()
        for client in self.addresses:
            client.close()

    def start_server(self):
        accept_thread = Thread(target=self.accept_connections)
        accept_thread.start()
        try:
            while self.running:
                pass
        except KeyboardInterrupt:
            print("Server stopped. Closing threads.")
            self.stop_server()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        HOST = sys.argv[1]
        print(f"Listening on host: {HOST}")
        PORT = 4000
        server = VoiceChatServer(HOST, PORT)

        def signal_handler(sig, frame):
            server.stop_server()

        signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
        server.start_server()
    else:
        print("Please provide a host address as a command-line argument.")
