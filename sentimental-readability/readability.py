# PROGRAM TO CHECK THE GRADE LVL OF A GIVEN TEXT

# IMPORT LIBRARY FROM CS50
from cs50 import get_string


# FUNCTIONS:

def count_letters(string):
    n = 0
    for i in texto:
        if i.isalpha():
            n += 1
    return n


def count_words(string):
    m = 1
    for i in texto:
        if i == " ":
            m += 1
    return m


def count_sentences(string):
    h = 0
    for i in texto:
        if i == "." or i == "!" or i == "?":
            h += 1
    return h


# GET USERS INPUT
texto = get_string("Digit a Text: \n")

# ADDRESSING COUNTING LETTERS FUNCTIONS RETURN TO 'LETTTERS' VARIABLE
letters = count_letters(texto)

# ADDRESSING COUNTING WORDS FUNCTIONS RETURN TO 'WORDS' VARIABLE
words = count_words(texto)

# ADDRESSING COUNTING SENTENCES FUNCTIONS RETURN TO 'SENTENCES' VARIABLE
sentences = count_sentences(texto)

# GET AVARAGE N OF LETTERS PER 100 WORDS
L = letters / words * 100

# GET AVARAGE N OF SENTENCES PER 100 WORDS
S = sentences / words * 100

# CALCULATE COLEMAN-LIAU INDEX
index = 0.0588 * L - 0.296 * S - 15.8

# SET CONDITION TO PRINT THE GRADE IN ACORDANCE WITH INDEX VALUE
if index < 1:
    print("Before Grade 1\n")

elif index > 16:
    print("Grade 16+\n")

else:
    print(f"Grade {round(index)}")

