def get(note,octave):
    Notes=[["C",100],["D",200],["E",300],["F",400]]
    if octave<1 or octave>4:
        return -1
    if note=="C":
        freq=Notes[0][1]
    elif note=="D":
        freq=Notes[1][1]
    elif note=="E":
        freq=Notes[2][1]
    elif note=="F":
        freq=Notes[3][1]
    else:
        return -1
    
    freq= freq + 2**octave
    return freq

if __name__ == "__main__":
    print(get("C",4)==116) #add 0.25
    print(get("F",2)==404) #add 0.25
    print(get("F",5)==-1) #add 0.25
    print(get("A",2)==-1) #add 0.25
