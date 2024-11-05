import random

def main():
    l = get_level()
    generate_integer(l)

def get_level():
    l = input("level: ")
    if l not in ['1', '2', '3']:
        l = 0
        get_level()
    return l

def generate_integer(level):
    level = int(level)
    if level == 1:
        level = range(10)
    elif level == 2:
        level = range(10, 100)
    elif level == 3:
        level = range(100, 1000)
    score = 0
    loses = 0
    count = 0
    while count < 10:
        try:
            a = random.choice(level)
            b = random.choice(level)
            c = a + b
            cc = int(input(f"{a} + {b} = "))
            if c == cc:
                score += 1
            else:
                print("EEE")
                loses =+ 1
            count+=1
        except ValueError:
            print("EEE")
            loses +=1
            count+=1
        if loses >= 3:
            print(f"{a} + {b} = {c}")
            print(f"score={score}")
            break

if __name__ == '__main__':
    main()