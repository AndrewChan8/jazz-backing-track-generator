from pretty_midi import PrettyMIDI
from instruments.bass import generate_walking_bass_track
from instruments.piano import generate_piano_track
from instruments.drums import generate_drum_track
from instruments.metronome_track import add_metronome_track

def generate_midi(chords, bpm, beats_per_bar, include_metronome=False, style="swing"):
  midi = PrettyMIDI()

  # Add tracks
  bass = generate_walking_bass_track(chords, bpm, beats_per_bar)
  midi.instruments.append(bass)

  piano = generate_piano_track(chords, bpm, beats_per_bar)
  midi.instruments.append(piano)

  drums = generate_drum_track(bpm, beats_per_bar, len(chords), style=style)
  midi.instruments.append(drums)
  
  if include_metronome:
    add_metronome_track(midi, bpm, beats_per_bar, len(chords))

  return midi
