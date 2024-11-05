greet = input("Greet the banker:\n").lower()

if 'hello' in greet:
    print("$0")
elif greet[0] == 'h':
    print("$20")
else:
    print("$100")
