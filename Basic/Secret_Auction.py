import os
auction = {}
continue_aution = True


def add_aucter(new_name, bid_price):
    auction[new_name] = bid_price


while continue_aution:
    print('''           
                        _ _ _ _ _ _ _ _
                        \             /
                         )_ _ _ _ _ _(
                         |" " " " " "|_.-._,.---------.,_.-._ 
                         |           | | |               | | ''-.
                         |           |_| |_             _| |_..-'   
                         |_ _ _ _ _ _| '-' `'---------'` '-'
                         )" " " " " "(
                        /_ _ _ _ _ _ _\\
                       .---------------.
                      /_ _ _ _ _ _ _ _ _\\
    
    ''')
    print('Welcome to the secret auction program')
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n"))
    add_aucter(name, price)
    should_continue = input("Are there any order bidders? Type 'Yes' or 'No'")
    if should_continue == "No":
        continue_aution = False
    os.system('cls')

winner = ''
max_bid = 0
for name in auction:
    if auction[name] > max_bid:
        max_bid = auction[name]
        winner = name
print(winner)
