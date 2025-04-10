from pretty_midi import Instrument, Note

def add_metronome_track(midi_obj, bpm, beats_per_bar, num_bars):
  click_track = Instrument(program=115)  # Woodblock
  seconds_per_beat = 60 / bpm

  for bar in range(num_bars):
    for beat in range(beats_per_bar):
      start = (bar * beats_per_bar + beat) * seconds_per_beat
      end = start + 0.05  # very short click

      pitch = 76 if beat == 0 else 77  # Different pitch for downbeat
      note = Note(velocity=100, pitch=pitch, start=start, end=end)
      click_track.notes.append(note)

  midi_obj.instruments.append(click_track)
