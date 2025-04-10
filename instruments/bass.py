# instruments/bass.py

from chords.theory import NOTE_MAP, get_chord_root
from pretty_midi import Instrument, Note

def generate_bass_track(chords, bpm, beats_per_bar):
  bass = Instrument(program=32)  # Acoustic Bass
  seconds_per_beat = 60 / bpm
  current_time = 0

  for chord in chords:
    root_note = get_chord_root(chord)
    midi_note = NOTE_MAP.get(root_note.capitalize(), 48)

    note = Note(
      velocity=90,
      pitch=midi_note,
      start=current_time,
      end=current_time + seconds_per_beat
    )
    bass.notes.append(note)

    current_time += beats_per_bar * seconds_per_beat

  return bass
