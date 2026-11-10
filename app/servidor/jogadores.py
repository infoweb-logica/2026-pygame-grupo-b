import threading

class Jogador:
  def __init__(self, socket, ip):
    self.socket = socket
    self.ip = ip

class Lista:

  def __init__(self):
    self._lista = []
    self._lock = threading.Lock()

  def adicionar(self, jogador):
    with self._lock:
      self._lista.append(jogador)

  def remover(self, jogador):
    with self._lock:
      if jogador in self._lista:
        self._lista.remove(jogador)

  def obter(self, index):
    with self._lock:
      return self._lista[index]

  def enviar_mensagem_para_todos(self, mensagem):
    print(f"Enviando mensagem para todos os jogadores: {mensagem}")
    for jogador in self._lista:
      jogador.socket.send(mensagem.encode('utf-8'))

  def tamanho(self):
    with self._lock:
      return len(self._lista)
