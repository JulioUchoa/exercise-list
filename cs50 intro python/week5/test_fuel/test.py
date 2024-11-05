def main():
    fraction = input("fraction:")
    try:
        a = convert(fraction)
        b = gauge(a)
        return print(b)
    except (ValueError, ZeroDivisionError):
        print("value error")

def convert(f):
    x, y = f.split("/")
    x, y = int(x), int(y)
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError

    c = int((x / y) * 100)
    return c

def gauge(n):
    n = int(n)
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    else:
        return f'{n}%'

if __name__ == '__main__':
    main()