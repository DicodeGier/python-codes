
def check_out(prices,ninePercenter,basket):
    basket_item_price = []
    total = 0.0
    for item in basket:
        item=item.lower()
        if item in prices:
            if item in ninePercenter:
                bip=prices[item] * 1.09
            else:
                bip=prices[item] * 1.21
        else:
            bip=0.0
        
        total += bip
        basket_item_price.append("{:.2f}".format(bip))
    return basket_item_price, "{:.2f}".format(total)

#section 5-1
p1 = {"chicken": 2, "apple": 3, "dvd": 6, "jacket": 20, "book": 9}
np1 = ["chicken", "dvd", "book"]
b1 = ["apple","apple","dvd","jacket","book","chicken"]
bipResult1, totalResult1 = check_out(p1, np1, b1)
print(totalResult1=='49.99') #if True, 0.25
print(bipResult1==['3.63', '3.63', '6.54', '24.20', '9.81', '2.18'])

p1 = {"chicken": 2, "apple": 3, "dvd": 6, "jacket": 20, "book": 9}
np1 = ["chicken", "dvd", "book"]
b1 = ["APPLE","apple","DVd","jacket","book","chicken"]
bipResult1, totalResult1 = check_out(p1, np1, b1)
print(totalResult1=='49.99') #if True, 0.25
print(bipResult1==['3.63', '3.63', '6.54', '24.20', '9.81', '2.18'])

p1 = {"chicken": 2, "apple": 3, "dvd": 6, "jacket": 20, "book": 9}
np1 = ["chicken", "dvd", "book"]
b1 = ["AP","apple","DV","jaket","book","chick"]
bipResult1, totalResult1 = check_out(p1, np1, b1)
print(totalResult1=='13.44') #if True, 0.25
print(bipResult1==['0.00', '3.63', '0.00', '0.00', '9.81', '0.00'])


# Check 1 - Calculating correct taxes for a simple list

# p1 = {"chicken": 3, "apple": 1, "dvd": 15, "jacket": 20, "book": 10}
# np1 = ["chicken", "apple", "book"]
# b1 = ["apple","apple","dvd","jacket","chicken","chicken"]
# bipResult1, totalResult1 = check_out(p1, np1, b1)
# print(totalResult1== "51.07") #if True, 0.25
# print(bipResult1==['1.09', '1.09', '18.15', '24.20', '3.27', '3.27']) #if True, 0.25


# Check 2 - Handles different capitalization
# p1 = {"chicken": 3, "apple": 1, "dvd": 15, "jacket": 20, "book": 10}
# np1 = ["chicken", "apple", "book"]
# b2 = ["aPPle","Apple","dvd","jaCKet","ChickeN","chicken"]
# bipResult2, totalResult2 = check_out(p1, np1, b2)
# print(bipResult2  == ['1.09', '1.09', '18.15', '24.20', '3.27', '3.27'] and totalResult2== "51.07") #if True, 0.25

# Check 3 - Puts 0 price for items not on the list
# p1 = {"chicken": 3, "apple": 1, "dvd": 15, "jacket": 20, "book": 10}
# np1 = ["chicken", "apple", "book"]
# b3 = ["apple", "xyz", "apple"]
# bipResult3, totalResult3 = check_out(p1, np1, b3)
# print(bipResult3==['1.09', '0.00', '1.09'] and totalResult3=='2.18' ) #if True, 0.25

#section 5-2

def check_out_with_file(filename,basket):
    lines=open(filename).readlines()
    prices={}
    ninePercenter=[]
    for line in lines:
        items=line.strip().split(',')
        item_name=items[0]
        item_price=items[1]
        prices[item_name]=int(item_price)  #you can also use float
        tax=items[2].strip('%')
        if (tax=='9'):
            ninePercenter.append(item_name)
    # print(ninePercenter)
    # print(prices)
    return check_out(prices,ninePercenter,basket)

#test code
b1 = ["apple","dvd","dvd","jacket","chicken"]
bipResult1, totalResult1 = check_out_with_file("Q5.txt",b1)
print(bipResult1==['3.27', '13.31', '13.31', '24.20', '4.36'] and totalResult1=='58.45') #if True, 1 point

#test code exam
# b1 = ["apple","apple","dvd","jacket","chicken","chicken"]
# bipResult1, totalResult1 = check_out_with_file("Q5.txt",b1)
# print(bipResult1==['1.09', '1.09', '18.15', '24.20', '3.27', '3.27'] and totalResult1== "51.07") #if True, 1 point