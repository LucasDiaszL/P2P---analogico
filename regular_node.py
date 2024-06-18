import socket
import threading
import json
import os

BORDER_NODE_HOST = '10.62.215.207'
BORDER_NODE_PORT = 8000

class RegularNode:
    def __init__(self, host='127.0.0.1', port=0):
        self.host = host
        self.port = port
        self.files = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.host, self.port = self.server.getsockname()
        self.load_files()

    def load_files(self):
        for file_name in os.listdir('.'):
            if os.path.isfile(file_name):
                self.files[file_name] = self.calculate_checksum(file_name)
        print(f"Files loaded: {self.files}")

    def calculate_checksum(self, file_name):
        return file_name  # Simplificação para teste

    def register_with_border_node(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((BORDER_NODE_HOST, BORDER_NODE_PORT))
            message = {
                "command": "register",
                "node_id": f"{self.host}:{self.port}",
                "address": (self.host, self.port),
                "files": list(self.files.keys())
            }
            print(f"Registering with border node: {message}")
            s.sendall(json.dumps(message).encode())

    def handle_client(self, client_socket):
        try:
            message = client_socket.recv(1024).decode()
            message = json.loads(message)
            file_name = message.get("file_name")
            if file_name in self.files:
                with open(file_name, 'rb') as f:
                    client_socket.sendall(f.read())
        finally:
            client_socket.close()

    def run(self):
        self.server.listen(5)
        print(f"Regular node running on {self.host}:{self.port}")
        self.register_with_border_node()

        while True:
            client_socket, addr = self.server.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    regular_node = RegularNode()
    regular_node.run()
