
def main():
    variable_name = input("input a variable in camelCase : ")
    snake = convert(variable_name)
    return snake

def convert(n):
    nome1 = ""
    for i in n:
        if i.isupper():
            nome1 += '_' + i.lower()
        else:
            nome1 += i
    print(nome1)

if __name__ == '__main__':
    main()


