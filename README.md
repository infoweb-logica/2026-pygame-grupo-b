# 2026-pygame-grupo-b
Repositório do jogo do grupo do 5 e 6 horários

---
## Tarefa
1. Abrir o vs code
2. Clonar o repositório do github e aceitar abrir o projeto na janela atual
   - Pressionar `CTRL+P`
   - Digitar `git: clone` e pressionar `ENTER`
   - Copiar a URL `https://github.com/infoweb-logica/2026-pygame-grupo-a.git` e pressionar `ENTER`
3. Abrir o terminal e configurar nome e email github
   - Pressionar `CTRL+SHIFT+'`
   - Digitar `git config user.name "NOME"` e pressionar `ENTER`
   - Digitar `git config user.email "EMAIL"` e pressionar `ENTER`
4. Definir qual tarefa irá fazer
5. Atualizar o README.md com nome e tarefa
6. Programar a tarefa
7. Guardar alterações no git locamente
8. **Professor** publicar no github
9. Apagar pasta com o código

---
## FIXME [título do jogo]

### Resumo do jogo

Cara a cara é um jogo que consiste em perguntas de sim ou não, em turnos alternados, em que o principal objetivo é adivinhar o personagem escolhido pelo seu adversário, antes que ele adivinhe o seu, isto é, vão sendo eliminados os personagens não correspondentes às características perguntadas. Este jogo possui várias personalidades, ou seja, cada exemplar possui seres/objetos diferentes.


### Descrevendo o tipo do jogo e suas metáforas
O Cara a Cara é essencialmente um jogo de dedução lógica e eliminação por meio de questionamentos eliminatórios, operando como uma mecânica de busca e filtragem de informações. Por trás de sua dinâmica recreativa, o tabuleiro funciona como uma metáfora perfeita para os processos de tomada de decisão e resolução de problemas, onde cada pergunta feita atua como um filtro que reduz as possibilidades para encontrar o dado correto.
### Como um jogador ganha
No jogo Cara a Cara, a vitória e a derrota são decididas pela precisão do seu palpite final sobre a identidade do personagem secreto do adversário. Um jogador ganha a partida quando, na sua vez de jogar, consegue adivinhar corretamente o nome do personagem do oponente, um feito que geralmente acontece após eliminar os suspeitos incorretos por meio de perguntas estratégicas de sim ou não. Por outro lado, existem duas formas de perder: a primeira é quando o adversário é mais rápido e descobre o seu personagem secreto antes; a segunda é através de um erro autoinfligido, já que arriscar um palpite definitivo e errar o nome do suspeito resulta em derrota imediata, independentemente de quantas molduras ainda estejam de pé no tabuleiro. 

### Referências de outros jogos
Como referência para o nosso jogo, pegamos o clássico jogo de tabuleiro de adivinhação para dois jogadores: Cara a Cara.

---
## Design do jogo

FIXME [Link para o figma] ou [Rascunhos das telas em papel]

FIXME [Elementos áudio visuais do jogo (sprites, fundos, etc) são autorais ou de terceiros? construídos ou baixados de qual lugar?]

### Descreva a jogabilidade

A jogabilidade do Cara a Cara consiste em uma disputa entre dois jogadores, na qual cada participante deve descobrir o personagem secreto escolhido pelo adversário por meio de perguntas sobre suas características. Os jogadores alternam seus turnos, fazendo perguntas que podem ser respondidas apenas com "sim" ou "não". Com base nas respostas, cada jogador elimina os personagens que não correspondem às características descobertas, até conseguir identificar o personagem secreto do oponente.

#### Sequência de tarefas

1. **Iniciar o jogo:** os jogadores acessam o jogo e iniciam uma nova partida.
2. **Escolher o personagem secreto:** cada jogador escolhe um personagem que deverá ser descoberto pelo adversário. Essa escolha deve permanecer secreta durante a partida.
3. **Visualizar os personagens:** os jogadores observam os personagens disponíveis no tabuleiro e suas respectivas características.
4. **Realizar uma pergunta:** o primeiro jogador faz uma pergunta sobre alguma característica do personagem secreto do adversário. A pergunta deve permitir uma resposta de "sim" ou "não".
5. **Responder à pergunta:** o adversário responde de acordo com as características do personagem que escolheu.
6. **Analisar a resposta:** o jogador utiliza a informação recebida para identificar quais personagens podem ser descartados.
7. **Eliminar personagens:** o jogador elimina ou abaixa os personagens que não correspondem à resposta recebida, reduzindo as possibilidades.
8. **Alternar os turnos:** após cada pergunta e resposta, a vez passa para o outro jogador, que realiza o mesmo procedimento.
9. **Tentar adivinhar:** quando acreditar que descobriu o personagem secreto do adversário, o jogador pode realizar um palpite definitivo.
10. **Finalizar a partida:** se o palpite estiver correto, o jogador vence. Caso erre, perde a partida. O jogo apresenta o resultado final, indicando o vencedor.

#### Uso de teclas

Os controles de teclado permitem que os jogadores interajam com os elementos do jogo, movimentando a seleção pelo tabuleiro e confirmando suas ações.

| Tecla | Função |
|---|---|
| `W` ou `↑` | Movimentar a seleção para cima. |
| `S` ou `↓` | Movimentar a seleção para baixo. |
| `A` ou `←` | Movimentar a seleção para a esquerda. |
| `D` ou `→` | Movimentar a seleção para a direita. |
| `ENTER` | Confirmar uma seleção ou ação. |
| `ESPAÇO` | Selecionar ou eliminar um personagem. |
| `ESC` | Voltar ao menu ou cancelar uma ação. |



FIXME [Qual a engine ([pygame](https://www.pygame.org/), [pygame zero](https://pygame-zero.readthedocs.io/), [godot](https://godotengine.org/), [unreal](https://www.unrealengine.com/), [unity](https://unity.com/), [GameMaker](https://gamemaker.io/), [construct](https://www.construct.net/), [love2d](https://love2d.org/), [cry engine](https://www.cryengine.com/), [gideros](https://www.gideros.rocks/))? Por que escolheram a engine?]

### Demo do jogo

FIXME [Vídeo do jogo]

FIXME [Como fazer para jogar?]

---
## Equipe

- [Allan Guilherme](https://github.com/allanguilhermec)
- [Allaphy Ricardo](https://github.com/allaphyricardo)
- [Ana cecília](https://github.com/anaribeiro2-r)
- [Ana Júlia](https://github.com/anaregis08)
- [Andrey Valentin](https://github.com/AndreyValentin)
- [Anne Beatriz](https://github.com/oliveiraanne-netizen)
- [Arthur Galvão](https://github.com/arthur74593)
- [Augusto Borges](https://github.com/GUT-R)
- [D S Ferreira](https://github.com/danisferreiraa)
- [Daniel R](https://github.com/Daniel-rodrigues-coder)
- [Davi Fonseca](https://github.com/ddavifonseca)
- [David Armando](https://github.com/davidarmando00)
- [Douglas F. Silva](https://github.com/douglasbsilva1)
- [Enzo Vasconcelos](https://github.com/vasconcelos14)
- [Eulla Paula](https://github.com/EullaOliveira)
- [Felipe raniery](https://github.com/Feliperaniery-commits)
- [Gabriel Bezerra](https://github.com/gabrielbezerra09)
- [Gabriel Ravazzolo](https://github.com/Ravazzolo)
- [Giovanna Tavares](https://github.com/giovannaprograma)
- [Jenyffer Danily](https://github.com/jenypr)
- [L A Minora](https://github.com/leonardo-minora)
