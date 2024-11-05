
def main():
    entrada = input("digit something: ")
    saida = trans(entrada)
    print(saida)

def trans(n):
    output = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in n:
        if i not in vowels:
            output += i
    return output

if __name__ == '__main__':
    main()