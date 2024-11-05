import random

def jogo():
    try:
        level = int(input("Level: "))
        ran_int = random.choice(range(1, (level+1)))
        print(f"ran_int={ran_int}")
        while True:
            if level <= 1 or not int(level):
                print("not int works")
                continue
            guess = int(input("Guess: "))
            if ran_int < guess:
                print("Too large!")
                continue
            elif ran_int > guess:
                print("Too small!")
                continue
            else:
                    print("Just right!")
                    return

    except ValueError:
         jogo()
jogo()