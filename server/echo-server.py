import socket
import pickle
import threading

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
class Conection():
    def __init__(self,conn,addr):
        self.conn = conn
        self.addr = addr
        self.thread = None
    
    def running(self):
        with self.conn:
            print(f"Conectado por {self.addr}")
            while True:
                data_bytes = self.conn.recv(1024)
                if not data_bytes:
                    self.conn.sendall(pickle.dumps("Adeus!"))
                    print(f"encerrada conexão em {HOST}:{PORT}")
                    break
                data = pickle.loads(data_bytes)
                comando = data[0].encode()
                argumento = data[1]
                if comando in dicionario:
                    resultado = dicionario[comando](argumento)
                    resultado_bytes = pickle.dumps(resultado)
                    self.conn.sendall(resultado_bytes)
                else:
                    self.conn.sendall(pickle.dumps("Comando desconhecido."))

def start_server():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print(f"Aguardando conexões em {HOST}:{PORT}")
            conn, addr = s.accept()
            conection_client = Conection(conn,addr)
            thread = threading.Thread(target=conection_client.running)
            thread.start()
            
start_server()