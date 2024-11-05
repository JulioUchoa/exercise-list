
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    n = []
    for i in s:
        try:
            n.append(int(i))
        except:
            ValueError

    # maior que 1 e menor que 7 digitos
    if 1 < len(s) < 7:

    # duas letras na frente
        if s[0].isalpha() and s[1].isalpha():

    # primeiro numero nao é 0
            if n:
                if not n[0] == 0:

        # não pode ser numero do meio e letra no fim.
                    if s[-1].isdigit():

                        for i in s:
                            if i not in [".", " ", ","]:
                                continue
                            else:
                                return False
                                break
                    else:
                        return False
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False

    return True




if __name__ == "__main__":
    main()