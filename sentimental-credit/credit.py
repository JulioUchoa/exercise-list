# PROGRAM TO CHECK IF ANY GIVEN NUMBER IS A VALID CREDIT CARD NUMBER

# IMPORT LIBRARY FROM CS50
from cs50 import get_string

# ASK USER FOR INPUT
card = get_string("Digit card number:  ")

# CREATING LISTS TO MANAGE DATA
lista_total = []
lesta_outros = []
losta_parcial = []
lasta_final = []

# READ INPUT IN TO MEMORY
for i in card:
    lista_total.append(int(i))

# REVERSE THE LIST
lista_total = lista_total[::-1]

# SAVE EVERY OTHER DIGIT  STARTING BY POSITION 1 AND MULTIPLYING IT BY 2
for i in range(1, len(lista_total), 2):
    losta_parcial.append(lista_total[i]*2)

# SAVE DIGITS THAT DIDNT GET MULTIPLIED
for i in range(0, len(lista_total), 2):
    lesta_outros.append(lista_total[i])

# SET VARIABLE TO STORE SUM OF GIVEN NUMBERRS
sim = 0

# SET LOOP TO CREATE LIST WITH EVERY DIGIT NUMBER IN LIST NUMBERS
for i in losta_parcial:
    for j in str(i):
        lasta_final.append(int(j))

# SET LOOP TO SUM EVERY DIGIT NUMBER ABOVE SAVEDF
for i in lasta_final:
    sim += i

# SET VARIABLE TO SAVE THE SUM OF THE 2 LISTS NUMBERS
final = sum(lesta_outros)+sim


# SET CONDITIONS TO CHECK IF ITS VISA, MATER, AMEX CARDS OR INVALID.

if card[0] == '3' and str(final)[-1::] == '0':
    print("AMEX\n")

if card[0] == '5' and str(final)[-1::] == '0':
    print("MASTERCARD\n")

if card[0] == '4' and str(final)[-1::] == '0':
    print("VISA\n")
else:
    print("INVALID\n")

