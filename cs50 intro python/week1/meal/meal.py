def main():

    time = input("What time is it ? ")

    time = convert(time)

    if  7 <= time < 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time < 19:
        print("dinner time")
    else:
        return

def convert(time):

    hora, min = time.split(":")

    hora, min = int(hora), int(min)

    min *= 100 / 60 / 100

    return hora + min


if __name__ == '__main__':
    main()