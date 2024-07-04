import regex as re 
lst = []
dictionary = {'Rotterdam': {'4': {'best': {'model': 'ARIMA_func'}}}}
lst.append(re.split("_func",dictionary["Rotterdam"]["4"]["best"]["model"])[0])
print(lst)


