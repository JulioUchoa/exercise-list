fruit = input("type a fruit if you want to know its calories: ").title()

list = {
    'Apple':130,
    'Avocado':50,
    'Banana':110,
    'Cantaloupe':50,
    'Grapefruid':60,
    'Grapes':90,
    'Honeydew Melon':50,
    'Kiwifruit':90,
    'Lemon':15,
    'Lime':20,
    'Nectarine':60,
    'Orange':80,
    'Peach':60,
    'Pear':100,
    'Pineapple':50,
    'Plums':70,
    'Strawbarries':50,
    'Sweet Cherries':100,
    'Tagenrine':50,
    'Watermelon':80
}

if fruit in list:
    print(list[fruit])

else:
    pass