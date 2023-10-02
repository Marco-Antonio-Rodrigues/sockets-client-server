from os import listdir,path
import datetime
import os

diretorio = "./DB"

def listar_arquivos(arg):
    return listdir(diretorio)
    
def enviar_arquivo(nome_arquivo):
    arquivo = os.path.join(diretorio,nome_arquivo)
    with open(arquivo, "rb") as file:
        return nome_arquivo,file
       
def finalizar_conexao(arg):
    return finalizar_conexao.close()


def hora_atual(arg):
    hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
    return hora_atual

def dados(arg):
    response = "Servidor online 24 horas"
    return response

