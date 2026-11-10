import pygame  # Importa a biblioteca Pygame
# import '../cliente/teste.py'  # Importa o módulo teste.py do diretório cliente
# servidor = teste.conectar_servidor()  # Chama a função conectar_servidor() do módulo teste.py

# ── 1. Inicialização ────────────────────────────────────────────────────────
pygame.init()  # Inicializa todos os módulos do Pygame

# ── 2. Configuração da janela ───────────────────────────────────────────────
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))  # Cria a janela
pygame.display.set_caption("Cara a Cara")  # Define o título

# Define a cor de fundo (formato RGB: Vermelho, Verde, Azul — valores de 0 a 255)
COR_FUNDO = (30, 30, 30)  # Cinza escuro

# ── 3. Laço principal ───────────────────────────────────────────────────────
rodando = True

while rodando:
    # Preenche a tela com a cor de fundo a cada frame
    tela.fill(COR_FUNDO)

    # Processa todos os eventos pendentes
    for evento in pygame.event.get():

        # Clique no botão X da janela
        if evento.type == pygame.QUIT:
            rodando = False


    # Atualiza o conteúdo exibido na janela
    pygame.display.flip()

# ── 4. Encerramento ─────────────────────────────────────────────────────────
pygame.quit()
print("Programa encerrado.")