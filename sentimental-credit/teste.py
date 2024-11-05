
from cs50 import get_string

card = get_string("Digit card number:  ")


lista_total = []
lesta_outros = []
losta_parcial = []
lasta_final = []

for i in card:
    lista_total.append(int(i))

lista_total = lista_total[::-1]


for i in range(1, len(lista_total), 2):
    losta_parcial.append(lista_total[i]*2)


for i in range(0, len(lista_total), 2):
    lesta_outros.append(lista_total[i])

sim=0

for i in losta_parcial:
    for j in str(i):
        lasta_final.append(int(j))

for i in lasta_final:
    sim+=i

final = sum(lesta_outros)+sim


if card[0] == '3' and str(final)[-1::] == '0':
    print("AMEX\n")

if card[0] == '5' and str(final)[-1::] == '0':
    print("MasterCard\n")

if card[0] == '4' and str(final)[-1::] == '0':
    print("VISA\n")
else:
    print("INVALID\n")

