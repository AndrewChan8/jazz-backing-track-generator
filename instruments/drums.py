# instruments/drums.py

from pretty_midi import Instrument, Note

# MIDI drum notes (channel 9)
KICK = 36
SNARE = 38
HIHAT = 42

def generate_drum_track(bpm, beats_per_bar, num_bars):
  drum = Instrument(program=0, is_drum=True)
  seconds_per_beat = 60 / bpm

  for bar in range(num_bars):
    for beat in range(beats_per_bar):
      start = (bar * beats_per_bar + beat) * seconds_per_beat
      end = start + 0.05  # short hits

      # Hi-hat on every beat
      drum.notes.append(Note(velocity=80, pitch=HIHAT, start=start, end=end))

      # Kick on 1 and 3
      if beat % beats_per_bar in [0, 2]:
        drum.notes.append(Note(velocity=100, pitch=KICK, start=start, end=end))

      # Snare on 2 and 4
      if beat % beats_per_bar in [1, 3]:
        drum.notes.append(Note(velocity=110, pitch=SNARE, start=start, end=end))

  return drum
