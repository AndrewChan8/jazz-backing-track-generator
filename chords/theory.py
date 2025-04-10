# chords/theory.py

NOTE_MAP = {
    'C': 48, 'C#': 49, 'Db': 49,
    'D': 50, 'D#': 51, 'Eb': 51,
    'E': 52, 'F': 53, 'F#': 54, 'Gb': 54,
    'G': 55, 'G#': 56, 'Ab': 56,
    'A': 57, 'A#': 58, 'Bb': 58,
    'B': 59
}

def get_chord_root(chord_str):
    if len(chord_str) > 1 and chord_str[1] in ['#', 'b']:
        return chord_str[:2]
    else:
        return chord_str[0]
