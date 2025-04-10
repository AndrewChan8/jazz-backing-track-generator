import wave
import struct
import math
import os

def generate_click(filename, duration=0.05, freq=1000, volume=0.5, rate=44100):
  samples = int(duration * rate)
  wav_file = wave.open(filename, 'w')
  wav_file.setnchannels(1)
  wav_file.setsampwidth(2)
  wav_file.setframerate(rate)

  for i in range(samples):
    value = int(volume * 32767.0 * math.sin(2 * math.pi * freq * i / rate))
    wav_file.writeframes(struct.pack('<h', value))

  wav_file.close()
  print(f"✅ {filename} generated")

os.makedirs("data", exist_ok=True)
generate_click("data/click_low.wav", freq=1000, volume=0.4)
generate_click("data/click_high.wav", freq=1600, volume=0.7)
