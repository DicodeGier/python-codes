def TurnToTSV(txtfilename, csvfilename):
    fh = open(txtfilename, "r")
    scores = fh.readlines()
    fh.close()
    scores2 = []
    for i in scores:
        new = (i.strip()).split()
        scores2.append(new)
    fh = open(csvfilename, "w")
    fh.write("game,date,host,guest,host score,guest score\n")
    # fixed numbers
    for i in range(0,7):
        fh.write(str(scores2[i*4][1])+","+str(scores2[1+i*4][0])+" "+str(scores2[1+i*4][1])+","+str(scores2[2+i*4][0])+","+str(scores2[2+i*4][3])+","+str(scores2[2+i*4][1])+","+str(scores2[2+i*4][2])+"\n")
    fh.close()

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
    try:
        TurnToTSV("Q10-short.txt","Q10studentcsv.txt")
    except:
        print("error")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==6)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==7)
