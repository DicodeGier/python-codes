##a (had met 1 if statement gemoeten)
def leap(year):
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return 'Yes'
            return 'No'
        return 'Yes'
    else:
        return 'No'

##zijn antwoord
def leap2(year):
    if (year % 4 != 0 or year % 100 == 0 and year > 1582 and year % 400 != 0):
        return 'yes'
    else:
        return 'no'

what_year = input("give the year ")
print(leap(what_year))
    
##b
def letter_checker(letter):
    if len(letter) != 1 or letter.isalpha() == False:
        return "error message: not a (single) letter"
    elif letter.lower() in ('a','e','i','o','u','y'):
        if letter.islower():
            return 'Vowel in lowercase'
        else:
            return 'Vowel in uppercase'
    else:
        if letter.islower():
            return 'Consonant in lowercase'
        else:
            return 'Consonant in uppercase'

letter_of_choice = input("give a letter ")
print(letter_checker(letter_of_choice))