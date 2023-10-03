import socket
import pickle

HOST = "127.0.0.1"  # O nome de host ou endereço IP do servidor
PORT = 65432  # A porta usada pelo servidor

def send_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))#espera conexão
        print(f"CONECTADO!")
        while True:
            request = None
            print("Escolha um comando:")
            print("1. CONSULTA")
            print("2. HORA")
            print("3. ARQUIVO <nome>")
            print("4. LISTAR")
            print("5. SAIR")
            escolha = input("Digite o número do comando ou 'SAIR' para encerrar: ")

            if escolha == '1':
                request = ["CONSULTA", None]

            elif escolha == '2':
                request = ["HORA", None]

            elif escolha.startswith('3'):
                nome_arquivo = escolha.split(' ', 2)[1]
                request = ["ARQUIVO", nome_arquivo]
                request_bytes = pickle.dumps(request)
                s.sendall(request_bytes)
                data_bytes = s.recv(1024)
                data = pickle.loads(data_bytes)
                with open(data[0],"wb") as file:
                    file.write(data[1])
                continue

            elif escolha == '4':
                request = ["LISTAR", None]

            elif escolha == '5' or escolha.upper() == 'SAIR':
                s.shutdown(socket.SHUT_WR)
                data_bytes = s.recv(1024)
                data = pickle.loads(data_bytes)
                s.close()
                print("Encerrando a conexão com o servidor.")
                break
            else:
                print("Comando inválido. Tente novamente.")

            if request:
                request_bytes = pickle.dumps(request)
                s.sendall(request_bytes)
                data_bytes = s.recv(1024)
                data = pickle.loads(data_bytes)
                print(f"Received: {data!r}")
send_server()