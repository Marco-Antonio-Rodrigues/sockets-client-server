from os import listdir,path
import os

def listar_arquivos():
    diretorio = os.path.abspath("nome_arquivo")
    return os.listdir(diretorio)

def enviar_arquivos(nome_arquivo):
    diretorio = os.path.abspath("nome_arquivo")
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    with open(caminho_arquivo, "rb") as arquivo:
        conteudo = arquivo.read()
        return conteudo

def finalizar_conexao(conexao):
    conexao.close()
    return "Conexão finalizada com sucesso."
