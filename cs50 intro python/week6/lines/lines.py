import sys
import os

def main():
    # verifies if user gives more than 2 command-line arguments
    if len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit()
    # verifies if user gives less than 2 command-line arguments
    elif len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit()

    # Verifies if file ends with '.py'
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        print("Not a python file")

    # Verifies if file exists
    if not os.path.exists(filename):
        print("the file doesnt exit")
        sys.exit()

    # count lines of coding excluding coments and blank lines
    count = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            # Ignora linhas vazias ou que começam com #
            if line and not line.startswith("#"):
                count += 1

    # print rsult
    print(count)

if __name__ == '__main__':
    main()