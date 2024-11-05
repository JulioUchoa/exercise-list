
dict = {}
sorted_dict = {}
while True:

    try:
        item = input("").upper()
        if item in dict:
            dict[item] += 1
        else:
            dict.update({item:1})
    except EOFError:
        print("\n")
        for key in sorted(dict.keys()):
            sorted_dict[key] = dict[key]
            print(sorted_dict[key], key)
        break

