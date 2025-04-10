# engine/midi_writer.py

def save_midi(midi_obj, filename="output.mid"):
  """
  Saves the PrettyMIDI object to disk.
  """
  try:
    midi_obj.write(filename)
    print(f"✅ MIDI file saved as {filename}")
  except Exception as e:
    print(f"❌ Error saving MIDI file: {e}")
