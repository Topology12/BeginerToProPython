import random
import os


def logo():
    print('''
        _       _
  /\  /(_) __ _| |__   ___ _ __
 / /_/ / |/ _` | '_ \ / _ \ '__|
/ __  /| | (_| | | | |  __/ |
\/ /_/ |_|\__, |_| |_|\___|_|
    __    |___/
   / /  _____      _____ _ __
  / /  / _ \ \ /\ / / _ \ '__|
 / /__| (_) \ V  V /  __/ |
 \____/\___/ \_/\_/ \___|_|

    ''')


def compare(value_1, value_2, choice):
    if value_1 > value_2:
        return choice == "A"
    else:
        return choice == "B"


def game():
    data = [
        {
            "name": "Neymar",
            "follower_count": 315,
            "description": "Social media platform",
            "country": "United States"
        },
        {
            "name": "Lionel Messi",
            "follower_count": 740,
            "description": "Footballer",
            "country": "Agentina"
        },
        {
            'name': "Dakota Jonhson",
            'follower_count': 150,
            'description': "Actress",
            'country': 'United States'
        },
        {
            'name': 'Cristiano Ronaldo',
            'follower_count': 1000,
            'description': "Footballer",
            'country': "Portugal"
        },
        {
            'name': 'Selena Gomez',
            'follower_count': 504,
            'description': "Musician and actress",
            'country': 'United States'
        },
        {
            'name': 'Kylie Jenner',
            'follower_count': 398,
            'description': "Media personality",
            'country': 'United States'
        },
        {
            'name': 'Dwayne Johnson',
            'follower_count': 396,
            'description': "Actor",
            'country': 'United States'
        },
        {
            'name': "Ariana Grande",
            'follower_count': 377,
            'description': "Musician and actress",
            'country': "United States"
        },
        {
            'name': "Kim Kardashian",
            'follower_count': 361,
            'description': "Media personality",
            'country': "United States",
        },
        {
            'name': "Beyoncé",
            'follower_count': 317,
            'description': "Musician and actress",
            'country': "United States"
        }
    ]
    logo()
    compare_A = random.choice(data)
    game_over = False
    score = 0
    while not game_over:
        compare_B = random.choice(data)
        while compare_A == compare_B:
            compare_B = random.choice(data)
        print(
            f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
        print(""" 
    /\   /\___ 
    \ \ / / __|
     \ V /\__ \ 
      \_/ |___/
    """)
        print(
            f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
        user_choice = input("Who has more followers? Typbe 'A' or 'B'")
        os.system('cls')
        logo()
        if compare(compare_A['follower_count'], compare_B['follower_count'], user_choice):
            compare_A = compare_B
            score += 1
            print(f"You are right. Current score is {score}")
        else:
            print("Game over!")
            game_over = True
            print(f"Worry!. Final score is {score}")
            continue_playing = input(
                "Do you want restart game? Type 'y' or 'n'.")
            if continue_playing == 'y':
                os.system('cls')
                game()


game()
