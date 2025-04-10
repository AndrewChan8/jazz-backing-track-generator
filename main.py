from metronome import start_metronome
from chords.parser import parse_progression

def get_user_input():
  # key = input("Enter key (e.g. C, Bb, F#): ")
  bpm = int(input("Enter tempo (BPM): "))
  # progression = input("Enter chord progression (e.g. Cmaj7 | Dm7 | G7 | Cmaj7): ")
  # style = input("Enter style (swing, bossa, funk): ")
  # instruments = input("Enter instruments (comma-separated: bass, piano, drums): ").split(",")
  # return key, bpm, progression, style, [i.strip() for i in instruments]
  return bpm

# key, bpm, progression, style, instruments = get_user_input()
bpm = get_user_input()

bars = int(input("How many bars? "))
beats_per_bar = int(input("Beats per bar (e.g. 4 for 4/4, 3 for 3/4): "))
total_beats = bars * beats_per_bar

start_metronome(bpm=bpm, beats=total_beats, beats_per_bar=beats_per_bar)

# chords = parse_progression(progression)

# print(f"Key: {key}")
# print(f"BPM: {bpm}")
# print(f"Style: {style}")
# print(f"Instruments: {instruments}")
# print(f"Chords: {chords}")