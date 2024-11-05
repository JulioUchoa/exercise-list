# import libraries
import sys
import os
import csv

def main():
    # tests if sys.argv lenght is smaller than three. if so, execute sys.exit
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # tests if sys.argv lenght is bigger than thress. if so, execute sys.exit
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # if neither of the above options where false take the next step>
    else:
        # tests if sys.argv[1] ends in '.csv' to asure its in the correct format
        if sys.argv[1][-4:] != '.csv':
            sys.exit(f"could not read {sys.argv[1]}")
        # do the same as above for the second comman-line argument
        elif sys.argv[2][-4:] != '.csv':
            sys.exit(f"could not read {sys.argv[2]}")

        # after both files checked, we open the first one as follows:
        with open(sys.argv[1], 'r') as file:
            fil = csv.DictReader(file)
            # define counter to write the files header ahead
            co = 0
            # iterate over the 'fil' variable that recivied the return of csv.DictReader function on file
            for i in fil:
                # split the 'name' variable into 2 different variables
                a, b = i['name'].split(",") # return ex:. a = Abbott b = Hannah
                # stores 'house' value on c temporarily so we can write it on the new file 'after.csv'
                c = i['house']
                # opens the second command-line argument and write on it the above mentioned variables
                with open(sys.argv[2], 'a') as arq:
                    writer = csv.writer(arq)
                    if co == 0:
                        writer.writerow(["first", "last", "house"])
                        co+=1
                    else:
                        writer.writerow([a.strip(" "), b.strip(" "), c.strip(" ")])







if __name__ == '__main__':
    main()