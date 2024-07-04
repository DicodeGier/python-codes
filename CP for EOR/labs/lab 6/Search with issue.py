# this function finds only 6 "fortunato" in file "text.txt", while there
# are 14 "fortunato" in the file (Open text.txt using Notepad and search 
# for fortunato)
# Figure out what the problem is by debugging the code

from typing import Counter
 
def display_contents_file4(file_name,search_term):
    fh=open("C:/Users/dicod/Documents/python codes/CP for EOR/labs/lab 6/"+str(file_name), 'r')
    lines = fh.readlines()
    fh.close()
    search_term=search_term.lower()
    
    counter = 0
    for line in lines:
        if search_term in line.strip(",.?!-").lower():
            counter +=  1
    return counter
    
 
print(display_contents_file4("text-lab6.txt","fortunato")==14)