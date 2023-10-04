from os import listdir,path
import datetime
import os

diretorio = "DB"

def listar_arquivos(arg=None):
    # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Junta o diretório atual com o nome do arquivo
    path = os.path.join(diretorio_atual,diretorio)
    return listdir(path)

def enviar_arquivo(nome_arquivo):
    # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Junta o diretório atual com o nome do arquivo
    path = os.path.join(diretorio_atual,diretorio,nome_arquivo)
    if os.path.exists(path):
        with open(path, "rb") as file:
            dados = file.read()
            return nome_arquivo, dados
    return "Arquivo não encontrado!"
           
def finalizar_conexao(arg=None):
    return finalizar_conexao.close()

def hora_atual(arg=None):
    hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
    return hora_atual

def dados(arg=None):
    response = "Servidor online 24 horas"
    return response