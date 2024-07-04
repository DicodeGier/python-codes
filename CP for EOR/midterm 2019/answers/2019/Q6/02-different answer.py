def returnCodes(country):
    country_1=country.lower()
    if country_1=="netherlands":
        return "NL","+31"   #do not change this line
    elif country_1=="canada":
        return "CA","+1"    #do not change this line
    elif country_1=="united states":
        return "US","+1"    #do not change this line
    else:
        return "No code","No code"    #do not change this line

cn=returnCodes("netherlands")[0]
ph=returnCodes("netherlands")[1]
print("the abbreviatin of netherlands is ",cn)    #do not change this line
print("the telephone code of netherlands is ",ph)    #do not change this line
