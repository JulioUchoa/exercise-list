# import RE and Sys libraries
import re
import sys

# define main function
def main():
    # asks for an hour for user. force it to be uppercase
    hours = input("hours: ").upper()
    # returns print the convert function on users input
    return print(convert(hours))

# define convert function
def convert(s):
    # defin pattern to be searched for # 1:00 PM AM ///  12:00 PM AM
    pattern  = r"(\d\d?)\:?(\d\d)?\s(AM|PM)?\s..\s(\d\d?)\:?(\d\d)?\s(AM|PM)?"
    match = re.search(pattern, s)
    if match:
        h1 = int(match[1])
        m1 = match[2]
        o1 = match[3]
        h2 = int(match[4])
        m2 = match[5]
        o2 = match[6]
        # check and adjust time format
        if h1 < 12 and 'PM' in o1:
            h1 +=12
        elif h2 < 12 and 'PM' in o2:
            h2 +=12
        # check if h1 or h2 are higher then 24
        if (h1 or h2) > 24:
            return ValueError
        # check if m1 is higher then 60
        if m1 and int(m1) > 60:
            return ValueError
        # check if m2 is higher then 60
        if m2 and int(m2) > 60:
            return ValueError

        if not m1 and m2:
            m2 = int(m2)
            return f"{h1:02} to {h2:02}:{m2}"

        if not m2 and m1:
            m1 = int(m1)
            return f"{h1:02}:{m1} to {h2:02}"

        if not (m1 and m2):
            return f"{h1:02} to {h2:02}"

        else:
            return f"{h1:02}:{m1} to {h2:02}:{m2}"

    return None

if __name__ == '__main__':
    main()