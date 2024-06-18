import socket
import threading
import json

BORDER_NODE_HOST = '0.0.0.0'  # Permitir conexões de qualquer IP
BORDER_NODE_PORT = 8000

class BorderNode:
    def __init__(self):
        self.files = {}

    def handle_client(self, client_socket):
        try:
            message = client_socket.recv(1024).decode()
            if message:
                message = json.loads(message)
                if message["command"] == "query":
                    self.send_file_list(client_socket)
                elif message["command"] == "register":
                    self.register_files(message["node_id"], message["files"])
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")
        finally:
            client_socket.close()

    def send_file_list(self, client):
        response = {"files": self.files}
        response_json = json.dumps(response)
        client.sendall(response_json.encode())

    def register_files(self, node_id, files):
        for file_name in files:
            if file_name not in self.files:
                self.files[file_name] = []
            self.files[file_name].append(node_id)
        print(f"Arquivos registrados: {self.files}")

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((BORDER_NODE_HOST, BORDER_NODE_PORT))
        server.listen(5)
        print(f"Nó de borda rodando em {BORDER_NODE_HOST}:{BORDER_NODE_PORT}")

        while True:
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    border_node = BorderNode()
    border_node.run()
