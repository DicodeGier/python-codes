import regex as re 
lst = []
dictionary = {'Rotterdam': {'4': {'best': {'model': 'ARIMA_func'}}}}
lst.append(re.split("_func",dictionary["Rotterdam"]["4"]["best"]["model"])[0])
print(lst)

#create an empty list 
lst = []

#append to the list
for i in range(5):
    for j in range(5):
        lst.append((i,j))

print(lst)

