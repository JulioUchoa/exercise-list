import re
import sys

def main():
    s = input("HTML: ")

    print(parse(s))

def parse(s):
    p = r'.*src="(https?://(www\.)?youtube\.com/embed/.*?)".*?'
    r = re.search(p, s)
    if r:
        first_link = r.group(1)
        if 'www' in first_link:
            last_link = first_link.replace("www.youtube.com/embed", "youtu.be")
        else:
            last_link = first_link.replace("youtube.com/embed", "youtu.be")

        return last_link
    else:
        return None

if __name__ == '__main__':
    main()