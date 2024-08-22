coffee_machine = {
    'water': 300,
    'milk': 250,
    'sugar': 150,
    'money': 0
}

coffee_category = {
    'espresso': {
        'water': 50,
        'milk': 10,
        'sugar': 10,
        'amount': 2.5
    },
    'latte': {
        'water': 75,
        'milk': 0,
        'sugar': 0,
        'amount': 1.5
    },
    'capuccino': {
        'water': 100,
        'milk': 20,
        'sugar': 0,
        'amount': 3.0
    }
}

coin_value = {
    'NiKen': 0.05
}


def print_menu():
    print("""
Menu: 
1 : Order Coffee
2 : Report
3 : Off machine
    """)


def off_machine():
    return


def check_order(water_need, milk_need, sugar_need):
    if water_need > coffee_machine['water']:
        return False
    if milk_need > coffee_machine['milk']:
        return False
    if sugar_need > coffee_machine['sugar']:
        return False
    return True


def check_money(type_1, type_2, type_3, type_4):
    pass


def order():
    coffee_type = input(f"What would you like? (Espresso, Latte, Cappuccino) ").lower()
    water_need = coffee_category[coffee_type]['water']
    milk_need = coffee_category[coffee_type]['milk']
    sugar_need = coffee_category[coffee_type]['sugar']
    if check_order(water_need, milk_need, sugar_need) and check_money(type_1, type_2, type_3, type_4):
        coffee_machine['water'] -= water_need
        coffee_machine['milk'] -= water_need
        coffee_machine['sugar'] -= sugar_need


def report():
    print(f"Water: {coffee_machine['water']}")
    print(f"Milk:  {coffee_machine['milk']}")
    print(f"Sugar: {coffee_machine['sugar']}")
    print(f"Money: {coffee_machine['money']}")


MENU = {
    "1": order,
    "2": report,
    "3": off_machine
}

while True:
    print_menu()
    select = input("What is your requirements?")
    while select not in MENU:
        print_menu()
        select = input(f"Please choice in menu")
    user_choice = MENU[select]
    user_choice()

