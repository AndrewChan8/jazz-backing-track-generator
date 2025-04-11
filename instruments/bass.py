# instruments/bass.py

from chords.theory import NOTE_MAP, get_chord_root
from pretty_midi import Instrument, Note

def normalize_bass_pitch(pitch, low=28, high=50):
  """
  Wraps or transposes a pitch into a realistic bass range.
  """
  while pitch > high:
    pitch -= 12
  while pitch < low:
    pitch += 12
  return pitch


def generate_walking_bass_track(chords, bpm, beats_per_bar):
  bass = Instrument(program=32)  # Acoustic Bass
  seconds_per_beat = 60 / bpm
  current_time = 0

  for i, chord in enumerate(chords):
    root_note = get_chord_root(chord)
    root_pitch = NOTE_MAP.get(root_note.capitalize(), 48)

    # Determine next chord root (or loop back to first)
    next_chord = chords[i + 1] if i + 1 < len(chords) else chords[0]
    next_root = get_chord_root(next_chord)
    next_pitch = NOTE_MAP.get(next_root.capitalize(), 48)

    # Construct a simple 4-note walk
    notes = []

    # Beat 1: root
    notes.append(root_pitch)

    # Beat 2: third (major/minor detection)
    if "min" in chord.lower():
      notes.append(root_pitch + 3)  # minor 3rd
    else:
      notes.append(root_pitch + 4)  # major 3rd

    # Beat 3: fifth
    notes.append(root_pitch + 7)

    # Beat 4: chromatic approach to next root
    if next_pitch > root_pitch:
      approach = next_pitch - 1
    else:
      approach = next_pitch + 1
    notes.append(approach)

    # Add to track
    for pitch in notes:
      bass.notes.append(Note(
        velocity=90,
        pitch=normalize_bass_pitch(pitch),
        start=current_time,
        end=current_time + seconds_per_beat
      ))
      current_time += seconds_per_beat

  return bass


def generate_bass_track(chords, bpm, beats_per_bar):
  bass = Instrument(program=32)  # Acoustic Bass
  seconds_per_beat = 60 / bpm
  current_time = 0

  for chord in chords:
    root_note = get_chord_root(chord)
    midi_note = NOTE_MAP.get(root_note.capitalize(), 48)

    note = Note(
      velocity=90,
      pitch=normalize_bass_pitch(midi_note),
      start=current_time,
      end=current_time + seconds_per_beat
    )
    bass.notes.append(note)

    current_time += beats_per_bar * seconds_per_beat

  return bass
