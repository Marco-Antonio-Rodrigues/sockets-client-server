# sockets-client-server

## Introdução

Projeto desenvolvido na disciplina de Redes de Computadores. Este documento descreve a implementação do projeto, incluindo detalhes sobre a arquitetura, desafios enfrentados durante o desenvolvimento e soluções adotadas para superar esses desafios. Além disso, são fornecidas instruções detalhadas sobre como executar o projeto.

## Arquitetura do Projeto

O projeto  é construído usando Python e algumas Bibliotecas(socket, pickle, threading, os, datetime), seguindo uma arquitetura cliente-servidor.
O servidor e o cliente utilizam a biblioteca socket para processar solicitações e fornecer respostas aos clientes e interagir com o servidor via protocolo TCP.

## Executando

Para executar o servidor do projeto, siga as etapas abaixo:

Pré-requisitos:

 Python 3.10^ instalado na máquina.
 ter o gerenciador de pacotes PIP


Passos Para Execução(Via terminal):

 Clone o repositório do projeto: 
git clone https://github.com/Marco-Antonio-Rodrigues/sockets-client-server.git

Navegue até o diretório do servidor: 
cd sockets-client-server

Execute:

 Cliente:
   -Navegue para o diretório cliente:
    cd client
   -Execute:
     python echo-client.py

 Servidor:
   -Navegue para o diretório servidor:
    cd server
   -Execute:
     python echo-server.py

Ou execute ambos:
python run.py

Caso queira ter multiconexões rode o cliente outras vezes em diferentes terminais.

Funções do algoritmo

## Comandos Disponíveis: 

listar_arquivos: Esta função retorna uma lista de nomes de arquivos no diretório ./DB.

enviar_arquivo: Esta função recebe o nome de um arquivo como entrada e tenta abrir e ler esse arquivo no diretório especificado. Se o arquivo existir, ele retorna o nome do arquivo e seus dados binários.

finalizar_conexao: Esta função finaliza a conexão pelo cliente.

hora_atual: Esta função retorna a hora atual no formato "HH:MM:SS".

dados: Esta função retorna uma string que diz "Servidor online 24 horas".

Conection: Esta classe representa uma conexão com um cliente. Ela mantém uma instância de soquete (conn) e o endereço do cliente (addr). A função running é responsável por lidar com as comunicações com o cliente dentro desta conexão.

Conection.__init__(self, conn, addr): O construtor da classe Conection inicializa uma instância da classe com um soquete de conexão (conn) e o endereço do cliente (addr).

Conection.running(self): Esta função é executada em uma thread para lidar com as comunicações com o cliente. Ela recebe comandos do cliente, verifica o comando e os argumentos, executa a função correspondente a partir do dicionário, envia a resposta de volta ao cliente e continua esperando por mais comandos até que a conexão seja encerrada.

start_server(): Esta função principal é responsável por iniciar o servidor e aguardar conexões de clientes. Ela cria um soquete, faz o bind a um endereço e porta específicos e, em seguida, aguarda por conexões de clientes. Para cada cliente que se conecta, cria uma instância de Conection e inicia uma thread para lidar com essa conexão.

send_server(): Esta função é responsável por criar uma conexão de cliente com o servidor em um endereço e porta específicos. Ela permite que o usuário envie comandos para o servidor e receba respostas correspondentes. A função apresenta um menu interativo de comandos para o usuário escolher, envia os comandos para o servidor e exibe as respostas recebidas.

