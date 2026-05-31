# Pygame Pong

Projeto didático de um jogo estilo **Pong** feito com **Pygame**.

**Autor:** Joabe Nonato

A ideia aqui é servir como base para estudo: o código está dividido em pequenas partes para facilitar o aprendizado de quem está começando com jogos em Python.  
Além da lógica do jogo, este projeto também inclui um sistema de áudio simples criado com `pygame.mixer` e `numpy`.

## O que este projeto ensina

- Criação de janela com Pygame
- Loop principal do jogo
- Desenho de objetos na tela
- Movimento de jogador, CPU e bola
- Detecção de colisão
- Sistema de pontuação
- Lógica simples de IA para o oponente
- Geração de áudio em tempo de execução
- Reproduzir efeitos sonoros e música de fundo

## Controles

- `Seta para cima` e `Seta para baixo`: mover a raquete do jogador
- `Enter`: iniciar uma partida ou reiniciar após vitória
- `Esc`: sair do jogo

## Requisitos

- Python 3
- `pygame`
- `numpy`

Instalação:

```bash
pip install pygame numpy
```

## Como executar

Na raiz do projeto, rode:

```bash
python main.py
```

## Estrutura do projeto

```text
pygame_pong/
├── README.md
├── main.py
├── audio/
│   ├── efeitos.py
│   ├── gerar_audio.py
│   ├── musicas.py
│   └── partituras.py
├── entities/
│   ├── base_ball.py
│   ├── base_CPU.py
│   ├── base_player.py
│   └── base_score.py
└── system/
    ├── helpers.py
    └── settings.py
```

## Visão geral dos arquivos

### `main.py`

É o ponto de entrada do jogo. Aqui ficam:

- inicialização do Pygame
- inicialização do mixer de áudio
- criação da janela
- loop principal
- tratamento de eventos
- atualização da lógica
- renderização dos elementos

Também define a classe `Game`, que organiza o ciclo do jogo em métodos:

- `events()`: lê teclado e eventos da janela
- `update()`: atualiza posições, colisões e pontuação
- `draw()`: desenha tudo na tela
- `run()`: executa o loop principal

Também é aqui que o jogo dispara os sons:

- música de menu ao abrir o jogo
- música de tema ao iniciar a partida
- efeito de batida quando a bola encosta na raquete
- efeito de pontuação quando alguém faz ponto
- efeito de vitória quando alguém vence

### `entities/base_ball.py`

Contém a classe `Ball`, responsável pela bola do jogo.

Responsabilidades:

- criar o retângulo da bola
- mover a bola na horizontal e vertical
- inverter a direção ao bater no topo ou no rodapé
- controlar a dificuldade/velocidade progressiva

Quando a bola ultrapassa uma lateral, o placar entra em ação e o jogo pode disparar o som de ponto.

### `entities/base_player.py`

Contém a classe `Player`, que representa a raquete controlada pelo jogador.

Responsabilidades:

- ler as teclas de seta
- mover a raquete para cima e para baixo
- impedir que a raquete saia da tela

### `entities/base_CPU.py`

Contém a classe `CPU`, que representa o adversário controlado pelo computador.

Responsabilidades:

- seguir o eixo vertical da bola
- manter a raquete dentro dos limites da tela

Essa IA é simples, mas ótima para estudo porque mostra como criar um oponente sem usar bibliotecas extras.

### `entities/base_score.py`

Contém a classe `Pontuacao`, que gerencia:

- pontos do jogador
- pontos da CPU
- condição de vitória

Quando a bola passa de um lado da tela, o ponto é atribuído ao lado oposto.

Esse arquivo também decide quando a vitória acontece, liberando o efeito sonoro de final de partida.

### `system/helpers.py`

Arquivo com funções auxiliares.

Hoje ele contém `escrever()`, usada para centralizar e desenhar textos na tela.

### `system/settings.py`

Arquivo de configurações do jogo.

Define valores como:

- largura e altura da janela
- FPS
- pontuação máxima
- cores

Centralizar essas constantes em um lugar facilita ajustes futuros.

### `audio/gerar_audio.py`

Arquivo responsável por gerar ondas sonoras com `numpy`.

Ele transforma frequência e duração em arrays de áudio que depois são convertidos em som pelo `pygame.mixer`.

### `audio/partituras.py`

Define as notas e a sequência usada pela música do jogo.

### `audio/musicas.py`

Cria objetos de música a partir da partitura, preparando o tema principal do jogo.

### `audio/efeitos.py`

Contém os efeitos sonoros curtos do jogo, como:

- batida da bola
- pontuação
- música de menu
- música de vitória
- outros sons preparados para expansão futura

## Como o jogo funciona

1. O programa inicia o Pygame e cria a janela.
2. O loop principal roda continuamente.
3. O jogador controla a raquete com o teclado.
4. A CPU tenta acompanhar a posição vertical da bola.
5. A bola se move e rebate nas bordas superior e inferior.
6. Quando a bola encosta numa raquete, a direção horizontal é invertida.
7. Se a bola atravessa uma lateral da tela, o placar é atualizado.
8. Sons diferentes são disparados conforme a situação do jogo.
9. O jogo termina quando alguém atinge a pontuação máxima.

## Regras do jogo

- Ganha quem fizer primeiro `10 pontos`
- A bola fica mais rápida ao longo da partida
- O som de fundo começa quando a partida é iniciada
- Depois da vitória, `Enter` ou `Esc` reiniciam o jogo

## Para quem está aprendendo

Se você estiver estudando Pygame, este projeto é um bom exercício porque reúne os conceitos básicos de uma forma prática:

- `Rect` para representar objetos
- `draw` para desenhar formas geométricas
- `event.get()` para capturar teclas
- `colliderect()` para colisão
- `Clock` para controlar FPS
- `mixer` para áudio e efeitos sonoros
- `numpy` para gerar ondas sonoras

## Sistema de áudio

O áudio deste projeto foi pensado para ser simples e didático, sem depender de arquivos `.wav` prontos para tudo.

### Como ele funciona

1. O jogo inicializa o `pg.mixer` com frequência de 44100 Hz.
2. As notas são definidas em `audio/partituras.py`.
3. `audio/gerar_audio.py` converte essas notas em ondas senoidais com `numpy`.
4. `audio/musicas.py` monta a música principal a partir da partitura.
5. `audio/efeitos.py` cria os efeitos curtos usados durante a partida.

### Onde os sons entram no jogo

- ao abrir o jogo, toca uma música de menu
- ao apertar `Enter`, a partida começa e a música principal entra em loop
- ao colidir com uma raquete, toca um som de batida
- ao marcar ponto, toca um som curto de pontuação
- ao vencer, toca uma música de vitória

## Próximos passos sugeridos

- adicionar menu inicial
- melhorar a IA da CPU
- aumentar a dificuldade com o tempo
- adicionar tela de pausa
- registrar placares
- separar melhor os assets de áudio
- adicionar arquivos de som externos para comparação com os sons gerados em código

## Licença

Use livremente para estudo e adaptação. Se publicar uma versão modificada, vale citar a origem do projeto.
