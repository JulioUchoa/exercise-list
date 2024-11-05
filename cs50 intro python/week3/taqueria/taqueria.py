try:

    total = 0
    while True:
        menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

        item = input("Select a item from menu: ").title()
        if item in menu:
            total += menu[item]
            print(f"${total:.2f}")
        else:
            pass
except EOFError:
    pass