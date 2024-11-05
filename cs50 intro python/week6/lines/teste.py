import sys

def main():
    try:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != '.py':
            print("Not a python file")
    except FileNotFoundError:
        sys.exit
    with open(sys.argv[1], 'r') as file:
        fil = file.readlines()
        cntr = 0
        for i in fil:
            if i[0] != '#' and i != '\n':
                cntr +=1
        return print(cntr)

if __name__ == '__main__':
    main()



#