import inflect

p = inflect.engine()
lista = []

while True:

    try:
        n = input("name: ")
        lista.append(n)

    except EOFError:
        print("")
        print("Adieu, adieu, to", p.join(lista, final_sep=""))
        break


