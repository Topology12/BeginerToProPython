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
    "Quarters": 0.25,
    'Dimes': 0.10,
    'Nickles': 0.05,
    'Pennies': 0.01
}


def print_menu() -> None:
    """Print the menu"""
    print("""
Menu: 
1 : Order Coffee
2 : Report
3 : Off machine
    """)


def check_order(water_need, milk_need, sugar_need):
    """Check ingredients of machine and return False if one of them not available """
    if water_need > coffee_machine['water']:
        return False
    if milk_need > coffee_machine['milk']:
        return False
    if sugar_need > coffee_machine['sugar']:
        return False
    return True


def check_money(amount):
    """Check amount of coffee with money of customers"""
    print('Please insert coin')
    total = int(input("How many quarters ?")) * 0.25
    total += int(input("How many dimes ?")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    if total >= amount:
        return True
    return False


def order():
    """Process order"""
    coffee_type = input("What would you like? (Espresso, Latte, Cappuccino) ").lower()
    water_need = coffee_category[coffee_type]['water']
    milk_need = coffee_category[coffee_type]['milk']
    sugar_need = coffee_category[coffee_type]['sugar']
    money_need = coffee_category[coffee_type]['amount']
    if check_order(water_need, milk_need, sugar_need):
        if check_money(money_need):
            coffee_machine['water'] -= water_need
            coffee_machine['milk'] -= water_need
            coffee_machine['sugar'] -= sugar_need
            coffee_machine['money'] += money_need
        else:
            print("Sorry. You enough money")
    else:
        print("Sorry. Machine not enough ingredient")


def report():
    """Report the state of the machine"""
    print(f"Water: {coffee_machine['water']}")
    print(f"Milk:  {coffee_machine['milk']}")
    print(f"Sugar: {coffee_machine['sugar']}")
    print(f"Money: {coffee_machine['money']}")


ON_MACHINE = True


def on_coffee_machine():
    """Machine working"""
    menu = {
        "1": order,
        "2": report,
        "3": None
    }
    while ON_MACHINE:
        print_menu()
        select = input("What is your requirements?")
        while select not in menu:
            print_menu()
            select = input("Please choice in menu")
        if select == "3":
            break
        user_choice = menu[select]
        user_choice()


# Start machine
on_coffee_machine()
