
inp = input("Choose between: Hello :), Goodbye :( or Hello :) Goodbye (:\n")

def convert(inp):
    if inp == 'Hello :)':
        return 'Hello 🙂'
    elif inp == 'Goodbye :(':
        return 'Goodbye 🙁'
    elif inp == 'Hello :) Goodbye :(':
        return 'Hello 🙂 Goodbye 🙁'
print(convert(inp))