from validator_collection import validators, checkers

def main():
    email = input("email: ")
    return print(validate(email))


def validate(s):

    valid_email = checkers.is_email(s)
    if valid_email == True:
        return "Valid"
    else:
        return "Invalid"



if __name__ == '__main__':
    main()