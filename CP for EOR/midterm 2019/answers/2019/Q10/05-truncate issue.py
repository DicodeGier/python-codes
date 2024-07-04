def TurnToTSV(txtfilename,csvfilename):    
    titleline = "game,date,host,guest,host score,guest score\n"
    lines=[]
    fh=open(txtfilename,"r")
    ramline = fh.readlines()
    for k in ramline:
        k=k.strip()
        lines.append(k.split())
    fh.close()
    wf = open(csvfilename,"w")
    wf.write(titleline)
    # print(lines)
    for j in range(0,7):
        wf.writelines(lines[0+4*j][1]+","+lines[1+4*j][0]+" "+lines[1+4*j][1]+","+lines[2+4*j][0]+","+lines[2+4*j][3]+","+lines[2+4*j][1]+","+lines[2+4*j][2]+"\n")
        wf.truncate(220)
    wf.close()

if __name__ == "__main__":
    import pandas as pd
    #0.2
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    TurnToTSV("Q10-main.txt","Q10studentcsv.txt")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==28)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==20)

    #0.4
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    try:
        TurnToTSV("Q10-short.txt","Q10studentcsv.txt")
    except:
        print("error")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==6)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==7)

    #0.4
    open("Q10studentcsv.txt","w").close() #remove the content of the output file if exists
    TurnToTSV("Q10-long.txt","Q10studentcsv.txt")
    print(pd.read_csv("Q10studentcsv.txt")["game"].sum()==45)
    print(pd.read_csv("Q10studentcsv.txt")["host score"].sum()==29)
