def countWords(str_input):
    return len(str_input.strip().split(" "))
    

print(countWords("Hello there"))

def main():
    test = "where the streets have no name and also no adresses"
    print('"'+ test + '"' + " has " + str(countWords(test)) + " words.")

main()