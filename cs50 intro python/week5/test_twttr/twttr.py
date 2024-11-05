
def main():

    user_ipt = str(input("give me a word: ")).lower()
    return print(shorten(user_ipt))


def shorten(word):
    sep = ' '
    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i not in vowels:
            sep += i
    return sep.strip(" ")


if __name__ == '__main__':
    main()