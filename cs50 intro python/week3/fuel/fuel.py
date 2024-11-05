def main():
    while True:
        fuel = input("Fraction: ")
        um, dois = fuel.split("/")
        try:
            um, dois = int(um), int(dois)
            da = int((um / dois)* 100)
            if da >= 99:
                print("F")
                break
            elif da <= 1:
                print("E")
                break
            else:
                print(f"{da}%")
                break

        except (ValueError, ZeroDivisionError):
            pass
main()


