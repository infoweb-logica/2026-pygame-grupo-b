import socket

servidor = None

def conectar_servidor():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_ip = '10.25.2.225'
    porta = 1234
    cliente_socket.connect((servidor_ip, porta))
    return cliente_socket

def teste_servidor():
    servidor = conectar_servidor()
    print("Conectado ao servidor.")
    servidor.send("Olá, servidor!".encode('utf-8'))
    dados = 1
    while dados:
        dados = servidor.recv(1024)
        print(f"Recebido do servidor: {dados.decode('utf-8')}")
    

if __name__ == "__main__":
    teste_servidor()