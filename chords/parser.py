def parse_progression(prog_str):
  chords = [ch.strip() for ch in prog_str.split('|')]
  return chords
