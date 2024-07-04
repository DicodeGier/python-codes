def get(note, octave):    
    if any(note in i for i in notes) and (octave in [1,2,3,4]):
        for i in range(0, i):
            starting_frequency = i[1]
            return starting_frequency + 2**octave
    else:
        return -1

notes = [["C", 100], ["D", 200], ["E", 300], ["F", 400]]

if __name__ == "__main__":
    print(get("C",4)==116) #add 0.25
    print(get("F",2)==404) #add 0.25
    print(get("F",5)==-1) #add 0.25
    print(get("A",2)==-1) #add 0.25