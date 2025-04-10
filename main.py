import os
from metronome import start_metronome
from chords.parser import parse_progression
from engine.generator import generate_midi
from engine.renderer import render_to_wav
from engine.midi_writer import save_midi

SF2_PATH = "/usr/share/sounds/sf2/FluidR3_GM.sf2"

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_MIDI = os.path.join(OUTPUT_DIR, "track.mid")
OUTPUT_WAV = os.path.join(OUTPUT_DIR, "track.wav")

USE_PRESET = True

def get_user_input():
  if USE_PRESET:
    bpm = 140
    progression = " EbMaj7 | EbMaj7 | Dmin7 | G7 | Cmin7 | Cmin7 | Bbmin7 | Eb7 "
    bars = 8
    beats_per_bar = 4
  else:
    bpm = int(input("Enter tempo (BPM): "))
    progression = input("Enter chord progression: ")
    bars = int(input("How many bars? "))
    beats_per_bar = int(input("Beats per bar: "))
  return bpm, progression, bars, beats_per_bar

bpm, progression, bars, beats_per_bar = get_user_input()
total_beats = bars * beats_per_bar

# start_metronome(bpm=bpm, beats=total_beats, beats_per_bar=beats_per_bar)

chords = parse_progression(progression)
midi = generate_midi(chords, bpm, beats_per_bar)

save_midi(midi, OUTPUT_MIDI)
render_to_wav(OUTPUT_MIDI, SF2_PATH, OUTPUT_WAV)
