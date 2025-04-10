import tkinter as tk
from tkinter import messagebox
import pygame
import os

from chords.parser import parse_progression
from engine.generator import generate_midi
from engine.midi_writer import save_midi
from engine.renderer import render_to_wav

SF2_PATH = "/usr/share/sounds/sf2/FluidR3_GM.sf2"

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_WAV = os.path.join(OUTPUT_DIR, "track.wav")
OUTPUT_MIDI = os.path.join(OUTPUT_DIR, "track.mid")

class JazzGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Jazz Backing Track Generator")

    # Input fields
    tk.Label(root, text="Tempo (BPM):").grid(row=0, column=0, sticky="w")
    self.bpm_entry = tk.Entry(root)
    self.bpm_entry.insert(0, "140")
    self.bpm_entry.grid(row=0, column=1)

    tk.Label(root, text="Bars:").grid(row=1, column=0, sticky="w")
    self.bars_entry = tk.Entry(root)
    self.bars_entry.insert(0, "4")
    self.bars_entry.grid(row=1, column=1)

    tk.Label(root, text="Beats per Bar:").grid(row=2, column=0, sticky="w")
    self.beats_entry = tk.Entry(root)
    self.beats_entry.insert(0, "4")
    self.beats_entry.grid(row=2, column=1)

    tk.Label(root, text="Repeat Count:").grid(row=3, column=0, sticky="w")
    self.repeat_entry = tk.Entry(root)
    self.repeat_entry.insert(0, "1")
    self.repeat_entry.grid(row=3, column=1)

    tk.Label(root, text="Chord Progression:").grid(row=4, column=0, sticky="nw")
    self.progression_entry = tk.Text(root, height=4, width=40)
    self.progression_entry.insert("1.0", "Cmaj7 | Dm7 | G7 | Cmaj7")
    self.progression_entry.grid(row=4, column=1, pady=5)

    # Generate and play buttons
    self.generate_button = tk.Button(root, text="Generate Track", command=self.generate_track)
    self.generate_button.grid(row=5, column=0, columnspan=2, pady=5)

    self.play_button = tk.Button(root, text="▶️ Play Track", command=self.play_audio, state=tk.DISABLED)
    self.play_button.grid(row=6, column=0, columnspan=2)

    self.stop_button = tk.Button(root, text="⏹️ Stop", command=self.stop_audio, state=tk.NORMAL)
    self.stop_button.grid(row=7, column=0, columnspan=2, pady=5)

    # Loop toggle
    self.loop_var = tk.BooleanVar(value=False)
    self.loop_check = tk.Checkbutton(root, text="🔁 Loop Track", variable=self.loop_var)
    self.loop_check.grid(row=8, column=0, columnspan=2)

    # Initialize pygame mixer
    pygame.mixer.init()

  def generate_track(self):
    try:
      bpm = int(self.bpm_entry.get())
      bars = int(self.bars_entry.get())
      beats_per_bar = int(self.beats_entry.get())
      repeat = int(self.repeat_entry.get())
      progression = self.progression_entry.get("1.0", tk.END).strip()

      # Repeat the progression N times
      progression = " | ".join([progression] * repeat)

      chords = parse_progression(progression)
      midi = generate_midi(chords, bpm, beats_per_bar)
      save_midi(midi, OUTPUT_MIDI)
      render_to_wav(OUTPUT_MIDI, SF2_PATH, OUTPUT_WAV)

      self.play_button.config(state=tk.NORMAL)
      messagebox.showinfo("Success", "✅ Track generated successfully!")

    except Exception as e:
      messagebox.showerror("Error", f"Something went wrong:\n{e}")

  def play_audio(self):
    try:
      if os.path.exists(OUTPUT_WAV):
        pygame.mixer.music.load(OUTPUT_WAV)
        loops = -1 if self.loop_var.get() else 0
        pygame.mixer.music.play(loops=loops)
      else:
        messagebox.showerror("Error", "Audio file not found.")
    except Exception as e:
      messagebox.showerror("Playback Error", f"Could not play audio:\n{e}")

  def stop_audio(self):
    try:
      pygame.mixer.music.stop()
    except Exception as e:
      messagebox.showerror("Stop Error", f"Could not stop audio:\n{e}")

if __name__ == "__main__":
  root = tk.Tk()
  app = JazzGUI(root)
  root.mainloop()
