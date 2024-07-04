def TurnToTSV(txtfilename,csvfilename):
    fh = open(txtfilename, "r")
    m = "game,date,host,guest,host score,guest score\n"
    z = "1"
    while z != "":
        a = fh.readline()
        m += a[5] + ","
        b = fh.readline()
        m += b.strip() + ","
        c = fh.readline()
        d = c.split()
        m += d[0] + "," + d[3] + "," + d[1] + "," + d[2]
        z = fh.readline()
        m += "\n"
    fh.close()
    fh = open(csvfilename, "w")
    fh.write(m)
    fh.close()
