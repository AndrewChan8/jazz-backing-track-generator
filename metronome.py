import pygame
import time

def start_metronome(bpm=120, beats=16, click_high="data/click_high.wav", click_low="data/click_low.wav", beats_per_bar=4):
  pygame.mixer.init()
  high = pygame.mixer.Sound(click_high)
  low = pygame.mixer.Sound(click_low)

  interval = 60.0 / bpm
  print(f"Metronome: {bpm} BPM, {beats} beats")

  pulse = []  # store visual beat indicators

  for i in range(beats):
    is_downbeat = (i % beats_per_bar == 0)

    if is_downbeat and i != 0:
      print("|", end=" ", flush=True)

    symbol = "*" if is_downbeat else "."
    print(symbol, end=" ", flush=True)

    (high if is_downbeat else low).play()
    time.sleep(interval)


  print("Metronome finished.")