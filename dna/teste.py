import csv
import sys

def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error! you should input: python file.py file.csv text.txt")
        return

    # TODO: Read database file.csv into a variable
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        sub = []
        sub1 = []
        for i in reader:
            sub.append(i)              # sub=[['name', 'AGATC', 'AATG', 'TATC'], ['Alice', '2', '8', '3'], ['Bob', '4', '1', '5'], ['Charlie', '3', '2', '5']]
        for i in range(1, len(sub[0])):
            sub1.append(sub[0][i])     # sub1 = ['AGATC', 'AATG', 'TATC'...]

    # TODO: Read DNA sequence file.txt into a variable
    with open(sys.argv[2], "r") as ftexto:
        reader1 = csv.reader(ftexto)
        seq = []
        for i in reader1:
            seq.append(i)
    seque = seq[0][0]                  # seque = ATACGAAGATCATGACTAGCATAGACAGATTAAGCGAT...

    # TODO: Find longest match of each STR in DNA sequence
    lt = []
    for i in sub1:
        a = longest_match(seque, i)
        lt.append(a)
    print(f"longes_match result = {lt}")         # lt = [4, 1, 5] longest_matchs of STR

    # TODO: Check database for matching profiles
"""
    td = []

    for i in sub:

        if i != sub[0]:
            print(f"For i in sub = {i}")

            for j in i:

                if j != i[0]:

                    td.append(int(j))

                    if td == lt:
                        print('testte print final', sub[1][0])


            print(f"td={td}")
            td = []
                #antiga posição de print(f"td={td}")
"""
def printm(seque, lt):
    for line




def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run



main()

>>>>>>>>>>>>>>>>>>



import csv
import sys


def main():
    with open(sys.argv[1]) as cfile:
        reader = csv.reader(cfile)
        all_seq = next(reader)[1:]

        with open(sys.argv[2]) as tfile:
            s = tfile.read()

        lt = [longest_match(s, seq) for seq in all_seq]

        printm(reader, lt)

def printm(reader, lt):
    for line in reader:
        person = line[0]
        value = [int(val) for val in line[1:]]
        if value == lt:
            print(person)
            return
    print('No match')




def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()