# instruments/drums.py

from pretty_midi import Instrument, Note
import random

# MIDI drum notes (channel 9)
KICK = 36
SNARE = 38
HIHAT_CLOSED = 42
HIHAT_PEDAL = 44
RIDE = 51

def generate_fill(start_time, seconds_per_beat, beats_per_bar, style="swing"):
  fill = []
  velocity = 100
  note_len = 0.1

  # Time grid: 8 16th-note positions in a bar
  grid = [start_time + i * (seconds_per_beat / 2) for i in range(beats_per_bar * 2)]

  # === Swing-style fills (lighter, snare-focused) ===
  SWING_FILLS = [
    [(SNARE, 4), (SNARE, 5), (SNARE, 6), (SNARE, 7)],
    [(SNARE, 2), (SNARE, 4), (RIDE, 6), (SNARE, 7)],
    [(SNARE, 3), (SNARE, 5)],
  ]

  # === Straight/funk-style fills (toms, kick, heavier) ===
  STRAIGHT_FILLS = [
    [(SNARE, 0), (KICK, 1), (SNARE, 2), (KICK, 3), (SNARE, 5), (KICK, 6)],
    [(47, 0), (45, 1), (43, 2), (SNARE, 4), (KICK, 6)],
    [(SNARE, 2), (KICK, 4), (SNARE, 6)],
  ]

  # Pick the fill bank by style
  if style == "swing":
    fill_bank = SWING_FILLS
  else:
    fill_bank = STRAIGHT_FILLS

  pattern = random.choice(fill_bank)

  for pitch, idx in pattern:
    if idx < len(grid):
      fill.append(Note(
        velocity=velocity,
        pitch=pitch,
        start=grid[idx],
        end=grid[idx] + note_len
      ))

  return fill


def generate_drum_track(bpm, beats_per_bar, num_bars, style="straight"):
  drum = Instrument(program=0, is_drum=True)
  seconds_per_beat = 60 / bpm

  for bar in range(num_bars):
    for beat in range(beats_per_bar):
      start = (bar * beats_per_bar + beat) * seconds_per_beat

      # Insert fill at the **last bar** or every 4th bar
      if (bar + 1) % 4 == 0 and beat == 0:
        fill_notes = generate_fill(start, seconds_per_beat, beats_per_bar, style=style)
        drum.notes.extend(fill_notes)
        continue  # Skip rest of groove in this bar

      # Swing: offset every 2nd eighth note by a bit
      if style == "swing":
        swing_and_offset = (2 / 3) * seconds_per_beat

        # Ride cymbal on all downbeats
        drum.notes.append(Note(velocity=70, pitch=RIDE, start=start, end=start + 0.05))

        # Swung “&” ride after beats 2 and 4
        if beat % beats_per_bar in [1, 3]:  # 2 and 4
          swung_and = start + swing_and_offset
          drum.notes.append(Note(velocity=60, pitch=RIDE, start=swung_and, end=swung_and + 0.05))

        # Hi-hat pedal "chick" on 2 and 4
        if beat % beats_per_bar in [1, 3]:
          drum.notes.append(Note(velocity=80, pitch=HIHAT_PEDAL, start=start, end=start + 0.05))

        # (Optional) Kick on 1 and 3
        # if beat % beats_per_bar in [0, 2]:
        #   drum.notes.append(Note(velocity=100, pitch=KICK, start=start, end=start + 0.05))

      else:  # straight feel
        beat_time = start

        # Hi-hat 8th notes: beat and upbeat
        hh1 = beat_time
        hh2 = beat_time + (seconds_per_beat / 2)

        drum.notes.append(Note(velocity=75, pitch=HIHAT_CLOSED, start=hh1, end=hh1 + 0.05))
        drum.notes.append(Note(velocity=65, pitch=HIHAT_CLOSED, start=hh2, end=hh2 + 0.05))

        # Kick on 1 and 3
        if beat % beats_per_bar in [0, 2]:
          drum.notes.append(Note(velocity=100, pitch=KICK, start=beat_time, end=beat_time + 0.05))

        # Snare on 2 and 4
        if beat % beats_per_bar in [1, 3]:
          drum.notes.append(Note(velocity=110, pitch=SNARE, start=beat_time, end=beat_time + 0.05))

  return drum