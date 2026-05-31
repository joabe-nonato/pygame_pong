# Pygame Pong

Projeto didático de um jogo estilo **Pong** feito com **Pygame**.

**Autor:** Joabe Nonato

A ideia aqui é servir como base para estudo: o código está dividido em pequenas partes para facilitar o aprendizado de quem está começando com jogos em Python.

## O que este projeto ensina

- Criação de janela com Pygame
- Loop principal do jogo
- Desenho de objetos na tela
- Movimento de jogador, CPU e bola
- Detecção de colisão
- Sistema de pontuação
- Lógica simples de IA para o oponente

## Controles

- `Seta para cima` e `Seta para baixo`: mover a raquete do jogador
- `Enter`: iniciar uma partida ou reiniciar após vitória
- `Esc`: sair do jogo

## Requisitos

- Python 3
- `pygame`

Instalação:

```bash
pip install pygame
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

### `entities/base_ball.py`

Contém a classe `Ball`, responsável pela bola do jogo.

Responsabilidades:

- criar o retângulo da bola
- mover a bola na horizontal e vertical
- inverter a direção ao bater no topo ou no rodapé
- controlar a dificuldade/velocidade progressiva

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

## Como o jogo funciona

1. O programa inicia o Pygame e cria a janela.
2. O loop principal roda continuamente.
3. O jogador controla a raquete com o teclado.
4. A CPU tenta acompanhar a posição vertical da bola.
5. A bola se move e rebate nas bordas superior e inferior.
6. Quando a bola encosta numa raquete, a direção horizontal é invertida.
7. Se a bola atravessa uma lateral da tela, o placar é atualizado.
8. O jogo termina quando alguém atinge a pontuação máxima.

## Regras do jogo

- Ganha quem fizer primeiro `10 pontos`
- A bola fica mais rápida ao longo da partida
- Depois da vitória, `Enter` ou `Esc` reiniciam o jogo

## Para quem está aprendendo

Se você estiver estudando Pygame, este projeto é um bom exercício porque reúne os conceitos básicos de uma forma prática:

- `Rect` para representar objetos
- `draw` para desenhar formas geométricas
- `event.get()` para capturar teclas
- `colliderect()` para colisão
- `Clock` para controlar FPS

## Próximos passos sugeridos

- adicionar menu inicial
- criar efeitos sonoros
- melhorar a IA da CPU
- aumentar a dificuldade com o tempo
- adicionar tela de pausa
- registrar placares

## Licença

Use livremente para estudo e adaptação. Se publicar uma versão modificada, vale citar a origem do projeto.
