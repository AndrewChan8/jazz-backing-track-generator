# engine/renderer.py

import pretty_midi
import fluidsynth
import soundfile as sf

def render_to_wav(midi_path, sf2_path, output_path, sample_rate=44100):
  """
  Renders a MIDI file to a WAV file using a SoundFont (.sf2).
  """
  try:
    # Start FluidSynth
    fs = fluidsynth.Synth()
    fs.start(driver="alsa")

    # Load the SoundFont
    sfid = fs.sfload(sf2_path)
    fs.program_select(0, sfid, 0, 0)

    # Load MIDI data
    midi_data = pretty_midi.PrettyMIDI(midi_path)

    # Synthesize audio (fs=sample_rate is the correct usage here)
    audio = midi_data.fluidsynth(fs=sample_rate)
    fs.delete()

    # Save as WAV
    sf.write(output_path, audio, sample_rate)
    print(f"✅ Exported audio to {output_path}")
  except Exception as e:
    print(f"❌ Error rendering to WAV: {e}")
