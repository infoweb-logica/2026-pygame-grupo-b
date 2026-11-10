import socket
import threading
import jogadores

lista = jogadores.Lista()

def escutar_jogador(jogador):
    global lista
    loop = True
    while loop:
        try:
            dados = jogador.socket.recv(1024).decode('utf-8')
            if dados:
                lista.enviar_mensagem_para_todos(dados)
                print(f"Recebido do {jogador.ip}: {dados}")
                # resposta = f"Mensagem recebida: {dados}"
                # jogador.socket.send(resposta.encode('utf-8'))
            loop = False
        except ConnectionResetError:
            print(f"Conexão com {jogador.ip} foi encerrada.")
            loop = False
    print(f"Encerrando conexão com {jogador.ip}.")
    jogador.socket.close()
    lista.remover(jogador)

def ligar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_servidor = '10.25.2.225'
    porta = 1234
    server_socket.bind((ip_servidor, porta))
    server_socket.listen(15)
    print(f"Servidor ligado {ip_servidor} e ouvindo na porta {porta}...")

    while True:
        cliente_socket, cliente_ip = server_socket.accept()
        print(f"Cliente conectado: {cliente_ip}")
        jogador_novo = jogadores.Jogador(cliente_socket, cliente_ip)
        lista.adicionar(jogador_novo)
        thread = threading.Thread(target=escutar_jogador, args=(jogador_novo,))
        thread.start()

if __name__ == "__main__":
    ligar_servidor()