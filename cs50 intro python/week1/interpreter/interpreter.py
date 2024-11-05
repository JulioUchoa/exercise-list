soma = input("digit the formula: ").split(' ')

def inter(n):

    soma[0] = int(soma[0])
    soma[2] = int(soma[2])

    if soma[1] == '+':
        res = soma[0] + soma[2]
    elif soma[1] == '-':
        res = soma[0] - soma[2]
    elif soma[1] == '*':
        res = soma[0] * soma[2]
    elif soma[1] == '/':
        res = soma[0] / soma[2]
    else:
        print("please, present the formula with the following strutucture: x + x ")

    return float(res)

print(inter(soma))