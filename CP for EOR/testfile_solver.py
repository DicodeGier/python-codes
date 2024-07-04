fh = open("test_all_words.txt",'r')
words = fh.read().strip().split('\n')
fh.close()

fh = open("test_all_words.txt",'w')
for word in words:
    if len(word) != 5:
        new_text = words.replace(word, '')
        fh.write(new_text)
fh.close()