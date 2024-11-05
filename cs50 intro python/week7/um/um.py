import re
import sys

def main():
    text = input("text: ")
    return print(count(text))

def count(s):

    pattern = r"(^|\W)um(\W|[,])"
    match = re.findall(pattern, s, re.IGNORECASE)
    count = len(match)
    return count


if __name__ == '__main__':
    main()