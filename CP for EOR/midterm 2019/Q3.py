def get(note, octave):
    if note == 'C' and octave in (1,4):
        return 100 + 2**octave
    elif note == 'D' and octave in (1,4):
        return 200 + 2**octave
    elif note == 'E' and octave in (1,4):
        return 300 + 2**octave
    elif note == 'F' and octave in (1,4):
        return 400 + 2**octave
    else:
        return -1