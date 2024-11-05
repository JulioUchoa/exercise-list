# define list of months
list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# 1- loop for prompting valid answers
# 2- check for data cleaning and transform it
# 3- handle execptions
while True:
    date = input("Date: ")
    if "-" in date:
        date = date.split("-")
    elif "/" in date:
        date = date.split("/")
    else:
        date = date.split(" ")
        date[1] = date[1].strip(",")

    dia = int(date[1])
    ano = int(date[2])
    if not dia > 31 or not int(dia):
        try:
            mes = int(date[0])
            if not mes > 12:
                print(f"{ano}-{mes:02d}-{dia:02d}")
                break

        except ValueError:
            mes = date[0].capitalize()
            mes = int(list.index(mes)+1)
            if not mes > 12:
                print(f"{ano}-{mes:02d}-{dia:02d}")
                break
    else:
        continue

