an = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")

an = an.lower().strip(' ')
if an == '42' or an == 'forty-two' or an == 'forty two':
    print("Yes")
else:
    print("No")