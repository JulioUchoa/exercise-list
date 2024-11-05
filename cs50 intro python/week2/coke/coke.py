
temp = 0

while True:
    coin = input("insert a coin: ").strip(" cents")

    if int(coin) in [5, 10, 25]:

        temp += int(coin)

        if temp < 50:
            print(f"Amount due: {50 - temp }")

        elif temp == 50:
            print("Change owed: 0")
            break

        elif temp > 50:
            print(f"Change owed: {temp - 50}")
            break
    else:
        print("Amount due: 50")
        continue

