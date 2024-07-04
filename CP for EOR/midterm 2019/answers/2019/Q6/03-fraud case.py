def returnCodes(country):
    country = country.upper()
    if country == "Netherlands":
        return "NL", "+31"
    if country == "Canada": 
        return "CA", "+1"
    if country == "United States":
        return "US", "+1"
    else:
        return "No Code", "No Code"

cn = returnCodes("Netherlands")
ph = returnCodes("Netherlands")
print("The abbreviation of The Netherlands is", "NL" )   #????
print("The The telephone code of Netherlands is", "+31") #????
