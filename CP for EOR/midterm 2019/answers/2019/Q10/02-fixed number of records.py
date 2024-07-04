def TurnToTSV(txtfilename, csvfilename):

    with open(txtfilename, "r") as fh:
        lines = fh.readlines()
    File = []
    for element in lines:
        if element == "":  #I guess (s)he meant \n
            lines.remove(element)
    #issue is using a fixed number 20; it only reads 20 lines, 7 games.
    # if three are only 3 games, it returns an error of "out of range
    # if there are more than 10 games, it returns only the first 7 games
    for i in range(0, 20, 3):

        File.append([lines[i].split(), lines[i+1].split(), lines[i+2].split()])



    with open(csvfilename, "w+") as f:

        f.write("")

    L = []



    for match in File:

        game = match[0][1]

        date = match[1][0]+" "+match[1][1]

        guest = match[2][0]

        host = match[2][3]

        hostscore = match[2][1]

        guestscore = match[2][2]

    

        with open(csvfilename, "a") as f:

            f.write(game +",")

            f.write(date +",")

            f.write(guest +",")

            f.write(host +",")

            f.write(hostscore +",")

            f.write(guestscore +"")

            f.write("\n")



if __name__ == "__main__":
    import pandas as pd
    #0.2
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    TurnToTSV("Q10-main.txt","Q10studentcsv.txt")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==37)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==27)

    #0.4
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    TurnToTSV("Q10-long.txt","Q10studentcsv.txt")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==45)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==29)

    #0.4
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    TurnToTSV("Q10-short.txt","Q10studentcsv.txt")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==6)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==7)
