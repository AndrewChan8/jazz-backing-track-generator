# instruments/piano.py

from pretty_midi import Instrument, Note
from chords.theory import get_chord_root, NOTE_MAP

def generate_piano_track(chords, bpm, beats_per_bar):
  piano = Instrument(program=0)  # Acoustic Grand Piano
  seconds_per_beat = 60 / bpm

  current_time = 0

  for chord_str in chords:
    root_note = get_chord_root(chord_str)
    root_pitch = NOTE_MAP.get(root_note.capitalize(), 48)

    # Basic triad voicing: root, +4, +7 (major), or tweak later
    if "min" in chord_str.lower():
      # Minor triad: root, m3, P5
      notes = [root_pitch, root_pitch + 3, root_pitch + 7]
    elif "7" in chord_str and "maj" not in chord_str.lower():
      # Dominant 7: root, M3, m7
      notes = [root_pitch, root_pitch + 4, root_pitch + 10]
    else:
      # Major triad: root, M3, P5
      notes = [root_pitch, root_pitch + 4, root_pitch + 7]

    for pitch in notes:
      note = Note(
        velocity=70,
        pitch=pitch,
        start=current_time,
        end=current_time + (beats_per_bar * seconds_per_beat)
      )
      piano.notes.append(note)

    current_time += beats_per_bar * seconds_per_beat

  return piano
