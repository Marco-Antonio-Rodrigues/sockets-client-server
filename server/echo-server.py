import socket
import pickle
from function_server import dados,listar_arquivos,enviar_arquivo,finalizar_conexao,hora_atual

HOST = "127.0.0.1"  # Endereço de host padrão (localhost)
PORT = 65432  # Porta para escutar (portas não privilegiadas são > 1023)


dicionario = {
    b'CONSULTA': dados,
    b'HORA': hora_atual,
    b'ARQUIVO': enviar_arquivo,
    b'LISTAR': listar_arquivos,
    b'SAIR': finalizar_conexao,
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Aguardando conexões em {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data_bytes = conn.recv(1024)
            if not data_bytes:
                continue
            data = pickle.loads(data_bytes)
            comando = data[0].encode()
            argumento = data[1]
            print(comando)
            print(argumento)
            if comando in dicionario:
                resultado = dicionario[comando](argumento)
                resultado_bytes = pickle.dumps(resultado)
                conn.sendall(resultado_bytes)
            else:
                conn.sendall(pickle.dumps("Comando desconhecido."))
