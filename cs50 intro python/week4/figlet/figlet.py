import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fontes = figlet.getFonts()

forma = ["-f", "--font"]

if len(sys.argv) == 1:
    texto = input("input: ")
    fonte = random.choice(fontes)
    figlet.setFont(font=fonte)
    print(f"Output: {figlet.renderText(texto)}")

elif len(sys.argv) == 3:
    if sys.argv[1] not in forma:
        print(sys.argv[2])
        sys.exit("incorrect key, try again")

    elif sys.argv[2] not in fontes:
        sys.exit("font not found!")

    else:
        texto = input("input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output: {figlet.renderText(texto)}")

else:
    sys.exit("error!")