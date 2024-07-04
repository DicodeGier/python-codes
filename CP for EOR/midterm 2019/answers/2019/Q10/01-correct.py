def TurnToTSV(txtfilename,csvfilename):
    with open(txtfilename) as fh:
        lines=fh.readlines()
    
    fw=open(csvfilename,"w")
    fw.write("game,date,host,guest,host score,guest score\n")

    for i in range(0,len(lines),4):
        gid=lines[i].split()[1]
        date=lines[i+1].strip()
        k=lines[i+2].split()
        host=k[0]
        hscore=k[1]
        gscore=k[2]
        guest=k[3]
        fw.write(gid+","+date+","+host+","+guest+","+hscore+","+gscore+"\n")

    fw.close()

def TurnToTSV2(txtfilename,csvfilename):
    allgames=[]
    with open(txtfilename) as fh:
        while True:
            line=fh.readline()
            if line=="":
                break
            elif line.startswith("Game"):
                gid=int(line.split()[1])
                date=fh.readline().strip()
                s=fh.readline()
                k=s.split()
                host=k[0]
                hscore=int(k[1])
                gscore=int(k[2])
                guest=k[3]
                allgames.append([str(gid),date,host,guest,str(hscore),str(gscore)])
    with open(csvfilename,"w") as fh:
        fh.write("game,date,host,guest,host score,guest score\n")
        for g in allgames:
            for i in range(len(g)-1): 
                fh.write(g[i]+",")
            fh.write(g[len(g)-1]+"\n")

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


