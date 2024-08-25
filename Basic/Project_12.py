import random


def logo():
    print("""
        
     __                 _                   ___                     _                 ___                     
  /\ \ \_   _ _ __ ___ | |__   ___ _ __    / _ \_   _  ___  ___ ___(_)_ __   __ _    / _ \__ _ _ __ ___   ___ 
 /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|  / /_\/ | | |/ _ \/ __/ __| | '_ \ / _` |  / /_\/ _` | '_ ` _ \ / _ \ 
/ /\  /| |_| | | | | | | |_) |  __/ |    / /_\\| |_| |  __/\__ \__ \ | | | | (_| | / /_\\ (_| | | | | | |  __/
\_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    \____/ \__,_|\___||___/___/_|_| |_|\__, | \____/\__,_|_| |_| |_|\___|
                                                                            |___/                             
                   
""")


def compare(number, target):
    if number == target:
        return True
    else:
        if number > target:
            print("Too high")
        else:
            print("Too low")
        print("Guess again")
        return False


def game():
    logo()
    number = [_ for _ in range(0, 101)]
    target = random.choice(number)
    print('Welcome to the Number Guessing Game!')
    print('I am thinking of a number between 1 and 100')
    level = input("Choose a difficulty. 'Easy' or 'Hard'\n")
    if level == 'Easy':
        attempts = 10
    else:
        attempts = 5
    print(f'You have {attempts} remaining to guess the number.')
    should_continue = True
    while should_continue:
        user_guess = int(input('Make a guess: '))
        result = compare(user_guess, target)
        if result == True:
            print(f"You got it. The answer was {target}")
        else:
            attempts -= 1
        if attempts == 0:
            should_continue = False
            print("You lose! Guess miss a number")
game()
