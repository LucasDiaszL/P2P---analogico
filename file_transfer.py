import socket
import json

BORDER_NODE_HOST = '10.62.215.207'
BORDER_NODE_PORT = 8000

def request_file(file_name):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((BORDER_NODE_HOST, BORDER_NODE_PORT))
            message = {"command": "query"}
            s.sendall(json.dumps(message).encode())

            response = s.recv(4096).decode()
            print(f"Resposta recebida do nó de borda: {response}")
            if not response:
                print("Erro: Resposta vazia recebida do nó de borda.")
                return
            file_list = json.loads(response)["files"]
            if file_name in file_list:
                node_id = file_list[file_name][0]
                node_host, node_port = node_id.split(':')
                node_port = int(node_port)
                download_file(node_host, node_port, file_name)
            else:
                print(f"Erro: arquivo '{file_name}' não encontrado na lista de arquivos")
    except Exception as e:
        print(f"Erro ao solicitar o arquivo: {e}")

def download_file(host, port, file_name):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            message = {"file_name": file_name}
            s.sendall(json.dumps(message).encode())

            with open(f"downloaded_{file_name}", 'wb') as f:
                while True:
                    data = s.recv(4096)
                    if not data:
                        break
                    f.write(data)
        print(f"Arquivo '{file_name}' baixado com sucesso.")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")

if __name__ == "__main__":
    file_name = "202101_BolsaFamilia_Pagamentos.csv"  # Substitua pelo nome do arquivo desejado
    print(f"Solicitando arquivo: {file_name}")
    request_file(file_name)
