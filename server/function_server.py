from os import listdir,path
import os


def listar_arquivos():
    diretorio = os.path.abspath()
    arquivo = os.path.join(diretorio, "nome_arquivo")

    return listdir(arquivo)
    
def enviar_arquivos():
    diretorio = os.path.abspath()
    arquivo = os.path.join(diretorio, "nome_arquivo", nome_arquivo)

    with open(arquivo, "rb") as files:
        for data in files.readline():
           return(data)
        return ("arquivo enviado!")
       
def finalizar_conexao():
    return finalizar_conexao.close()
