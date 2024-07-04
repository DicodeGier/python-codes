def check_out(p1, np1, b1):
    bipResult = []
    totalResult = 0
    for n in b1:
        if n.lower() in p1:
            if n.lower() in np1:
                bipResult.append("{:.2f}".format(p1[n.lower()]*1.09))
                totalResult += p1[n.lower()]*1.09
            else:
                bipResult.append("{:.2f}".format(p1[n.lower()]*1.21))
                totalResult += p1[n.lower()]*1.21
        else:
            bipResult.append("0.00")
    return bipResult, "{:.2f}".format(totalResult)


def check_out_with_file(filename,b1):
    fh = open("C:/Users/dicod/Documents/python codes/CP for EOR/mock_midterm_codes/"+str(filename), 'r')
    L = fh.readlines()
    fh.close()
    prices = {}
    bipResult = []
    for n in L:
        L1 = n.strip().split(',')
        item = L1[0]
        price = L1[1]
        prices[item]=int(price)   
        tax=L1[2].strip('%')
        if (tax=='9'):
            bipResult.append(item)
    return check_out(prices, bipResult, b1)

b1 = ["apple","apple","dvd","jacket","chicken","chicken"]
bipResult1,totalResult1=check_out_with_file("Q5.txt",b1)
print(bipResult1==['1.09','1.09','18.15','24.20','3.27','3.27']and totalResult1=="51.07")#ifTrue,1point

