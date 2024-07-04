def TurnToTSV(txtfilename, csvfilename):
    fh1 = open(txtfilename, "r")
    fh2 = open(csvfilename, "w+")
    fh2.write("game,date,host,guest,host score,guest score \n 1,Dec 11,Barca,Real,3,4 \n 2,Dec 12,Juve,Inter,0,0 \n 3,Jan 13,Barca,Milan,4,1 \n 4,Jan 15,Inter,Juve,5,4 \n 5,Jan 16,Inter,Real,4,4 \n 6,Feb 1,PSV,Ajax,2,2 \n 7,Feb 19,Ajax,Feyenoord,2,1")
        

