import textdistance

def distance(word_1, word_2):
    absolute_distance = textdistance.hamming.distance(word_1, word_2)
    normalized_distance = textdistance.hamming.normalized_distance(word_1, word_2)
    return absolute_distance, normalized_distance


data  =  ["kitten",  "katten",  "saturday", 
"sunday", "rosettacode", "raisethysword", "kitten", "", "kitten", "KITTEN", 
"kitten","kitten","","kitten"]

while data != []:
    print(distance(data[0],data[1]))
    data.pop(0)
    data.pop(0)