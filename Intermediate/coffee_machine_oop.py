"""Object-oriented programing basic"""


class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }


class Menu:
    def __init__(self):
        self.menu = [MenuItem("Espresso", 2.5, 50, 0, 25),
                     MenuItem('Latte', 2.0, 50, 25, 0),
                     MenuItem("Capuccino", 3.5, 75, 25, 15)]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += item.name + "/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


class CoffeeMaker:
    ''' Class Coffee Maker '''
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 250,
            'coffee': 350,
        }

    def report(self):
        print(f"Water: {self.resources['water']}")
        print(f"Milk:  {self.resources['milk']}")
        print(f"Coffee: {self.resources['coffee']}")

    def is_resources_sufficient(self, drink: MenuItem) -> bool:
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is order {order.name}")


class MoneyMachine:
    CURRENCY = '$'

    COIN_VALUES = {
        'quarter': 0.25,
        'dimes': 0.1,
        'nickles': 0.05,
        'pennies': 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print('Please insert coins.')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change")
            self.profit += cost
            return True
        else:
            print("Not enough money")
            self.money_received = 0
            return False


money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

while True:
    choice = input(f"What would you like? ({menu.get_items()})")
    coffee_type = menu.find_drink(choice)
    if coffee_type:
        if coffee_maker.is_resources_sufficient(coffee_type):
            if money_machine.make_payment(coffee_type.cost):
                coffee_maker.make_coffee(coffee_type)
        else:
            print('Sorry, machine not enough ingredients')
    else:
        if choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            break
