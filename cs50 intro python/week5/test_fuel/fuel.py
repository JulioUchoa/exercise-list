def main():
    n = input("fraction: ")
    per = convert(n)
    print(gauge(per))


def convert(n):
    while True:
        x, y = n.split("/")
        try:
            x = int(x)
            y = int(y)
            fraction = x / y
            if x > y:
                n = input("fraction: ")
                continue
            else:
                percentage = int(fraction * 100)
                return percentage

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == '__main__':
    main()