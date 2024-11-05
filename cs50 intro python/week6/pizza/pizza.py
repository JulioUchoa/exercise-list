import sys
import os
import csv
from tabulate import tabulate

def main():
    # verifies if user inputs more than
    # one command line argument
    if len(sys.argv) != 2:
        sys.exit("Program just accepts 1 command-line argument.")
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file.")
    elif not os.path.exists(filename):
        sys.exit("file dosnt exit.")
    else:
        text = sys.argv[1]
        with open(text, "r") as file:
            fil = csv.reader(file)
            l = []
            for i in fil:
                l.append(i)
            print(tabulate(l, tablefmt="grid"))

if __name__ == '__main__':
    main()