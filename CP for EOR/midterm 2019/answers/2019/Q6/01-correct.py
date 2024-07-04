def returnCodes(country):
    country=country.lower()
    if country=="netherlands":
        return "NL","+31"   #do not change this line
    elif country=="canada":
        return "CA","+1"    #do not change this line
    elif country=="united states":
        return "US","+1"    #do not change this line
    else:
        return "No code","No code"    #do not change this line

cn,ph=returnCodes("netherlands")
print("the abbreviatin of netherlands is ",cn)    #do not change this line
print("the telephone code if netherlands is ",ph)    #do not change this line

#it should have four return, count(return) must be four.
#return "NL","+31"
#return "CA","+1"
#it should have for elif

