

import csv
import sys


def main():


    # check for correct user input
    if len(sys.argv) != 3:
        print("Error! you should input: python file.py file.csv text.txt")
        return
    # opens csv.file, extract its content in string format
    with open(sys.argv[1]) as cfile:
        reader = csv.reader(cfile)
        all_seq = next(reader)[1:]

    # opens txt.file
        with open(sys.argv[2]) as tfile:
            s = tfile.read()
    # find longest STRS in txt files
        lt = [longest_match(s, seq) for seq in all_seq]

    #print matched infos
        printm(reader, lt)
# define a functions to check the results
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