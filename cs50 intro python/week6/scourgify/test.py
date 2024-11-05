import sys

def main():
    try:
        print(f'0={sys.argv[0]}')
        print(f'1={sys.argv[1][-4:]}')
        print(f'2={sys.argv[2]}')
    except:
        print("error de indexação")


main()