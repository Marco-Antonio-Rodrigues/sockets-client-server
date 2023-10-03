from os import listdir,path
import datetime
import os

diretorio = "./DB"

def listar_arquivos(arg=None):
    return listdir(diretorio)

def enviar_arquivo(nome_arquivo):
    path = diretorio+"/"+nome_arquivo
    with open(path, "rb") as file:
        dados = file.read()
        return nome_arquivo,dados
       
def finalizar_conexao(arg=None):
    return finalizar_conexao.close()


def hora_atual(arg=None):
    hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
    return hora_atual

def dados(arg=None):
    response = "Servidor online 24 horas"
    return response

# nome,dados = enviar_arquivo("file1.txt")
# print(nome,dados)
# with open(nome,"wb") as file:
#     file.write(dados)