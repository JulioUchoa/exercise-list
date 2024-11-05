import re
import sys

def main():
    ip = input("IPv4 adress: ")

    return print(validate(ip))


def validate(ip):
    try:
        matches = re.match(r"^([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})\.([0-9]{0,3})$", ip)

        g1 = int(matches.group(1))
        g2 = int(matches.group(2))
        g3 = int(matches.group(3))
        g4 = int(matches.group(4))

        if g1 > 255 or g2 > 255 or g3 > 255 or g4 > 255:
            return False

        return True

    except:
        return False



if __name__ == '__main__':
    main()