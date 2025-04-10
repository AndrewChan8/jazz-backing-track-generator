from metronome import start_metronome
from chords.parser import parse_progression
from engine.generator import generate_midi
from engine.renderer import render_to_wav
from engine.midi_writer import save_midi

USE_PRESET = True  # Change to False if you want to use manual input

def get_user_input():
  if USE_PRESET:
    bpm = 140
    # progression = " EbMaj7 | EbMaj7 | Dmin7 | G7 | Cmin7 | Cmin7 | Bbmin7 | Eb7 "
    progression = " FMaj7 | Fmaj7 | BbMaj7 | C7 | FMaj7 | Fmaj7 | BbMaj7 | C7"
    bars = 8
    beats_per_bar = 4
  else:
    bpm = int(input("Enter tempo (BPM): "))
    progression = input("Enter chord progression (e.g. Cmaj7 | Dm7 | G7 | Cmaj7): ")
    bars = int(input("How many bars? "))
    beats_per_bar = int(input("Beats per bar (e.g. 4 for 4/4, 3 for 3/4): "))
  return bpm, progression, bars, beats_per_bar

# Get all user input
bpm, progression, bars, beats_per_bar = get_user_input()
total_beats = bars * beats_per_bar

# Start metronome
# start_metronome(bpm=bpm, beats=total_beats, beats_per_bar=beats_per_bar)

# Generate MIDI
chords = parse_progression(progression)
midi = generate_midi(chords, bpm, beats_per_bar)
save_midi(midi)

# Render to audio
sf2_path = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
render_to_wav("output.mid", sf2_path, "output.wav")
