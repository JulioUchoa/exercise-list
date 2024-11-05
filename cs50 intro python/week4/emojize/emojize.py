import emoji

inp = input("input: ")

def emo(n):
    try:
        re = emoji.emojize(n)
        print("Output:", re)
    except:
        if "_" in n:
            re = emoji.emojize(n, languase=alias)
            print("Output:", re)

emo(inp)