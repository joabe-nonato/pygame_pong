# gerar_audio.py
import numpy as np
import wave

SAMPLE_RATE = 44100

NOTAS = {
    "C4": 261,
    "D4": 293,
    "E4": 329,
    "F4": 349,
    "G4": 392,
    "A4": 440,
    "B4": 493,

    "C5": 523,
    "D5": 587,
    "E5": 659,
    "F5": 698,
    "G5": 784,
}

# def gerar_tom(freq, duracao, volume=0.5):

#     t = np.linspace(
#         0,
#         duracao,
#         int(SAMPLE_RATE * duracao),
#         False
#     )

#     onda = np.sin(freq * 2 * np.pi * t)

#     fade_in_size = int(len(onda) * 0.1)
#     fade_out_size = int(len(onda) * 0.2)

#     envelope = np.ones(len(onda))

#     envelope[:fade_in_size] = np.linspace(0, 1, fade_in_size)

#     envelope[-fade_out_size:] = np.linspace(
#         1,
#         0,
#         fade_out_size
#     )

#     audio = onda * envelope * volume

#     return (audio * 32767).astype(np.int16)

def gerar_tom(freq, duracao, volume=0.5):
    t = np.linspace(0, duracao, int(SAMPLE_RATE * duracao), False)
    onda = np.sin(freq * 2 * np.pi * t)
    audio = onda * volume
    # return (audio * 32767).astype(np.int16)
    audio = (audio * 32767).astype(np.int16)
    audio = np.column_stack((audio, audio))
    return audio

def gerar_musica(partitura):
    faixas = []
    for nota, duracao in partitura:
        freq = NOTAS[nota]
        som = gerar_tom(
            freq,
            duracao,
            volume=0.15
        )
        faixas.append(som)
    return np.concatenate(faixas)
