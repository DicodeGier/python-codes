import regex as re
def checkHTTP(input):
    result = re.search('http://', input)
    if result:
        return 'string found'
    else:
        return 'not found'

test = checkHTTP('This is the text to be searched for occurrences of the http:// pattern.')
print(test)
