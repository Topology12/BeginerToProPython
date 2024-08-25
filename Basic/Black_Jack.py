import random
import os


def logo():
    print(
        """
        .------.          _      _               _     _                _
        |A_  _ |.        | |    | |             | |   (_)              | |
        |( \/ ).-----.   | |_ _ | | _ _ _  _ _ _| | _ _ _  _ _ _  _ _ _| | _ _
        | \  /|K /\  |   | '_  \| |/  _` |/  _ _| |/  /  |/  _` |/  _ _| |/  /
        |  \/ | /  \ |   | |_)  | |  (_| |  (_ _|    <|  |  (_| |  (_ _|    < 
        `-----| \  / |   |_._ _/|_|\_ _,_|\_ _ _|_|\_ \  |\_ _,_|\_ _ _|_|\_ \ 
              |  \/ K|                               _/  |  
              `------'                              |_ _/
        """)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


def cal_score(list_card: list):
    if sum(list_card) == 21 and len(list_card) == 2:
        return 0
    if 11 in list_card and sum(list_card) > 21:
        list_card.remove(11)
        list_card.append(1)
    return sum(list_card)


def compare(your_cards, computer_cards):
    if cal_score(your_cards) == cal_score(computer_cards) and cal_score(your_cards) <= 21:
        print('Draw!')
    elif cal_score(computer_cards) == 0:
        print("You lose!")
    elif cal_score(your_cards) == 0:
        print('You win!')
    elif cal_score(your_cards) > 21:
        print('You lose!')
    elif cal_score(computer_cards) > 21:
        print("You win!")
    elif cal_score(your_cards) < cal_score(computer_cards):
        print('You lose!')
    else:
        print('You win!')


def black_jack_game():
    playing_game = input(
        "Do you want plat to the game of Black Jack? Type 'y' or 'no' ")
    if playing_game == 'y':
        logo()
        game_over = False
        your_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]
        your_score = cal_score(your_cards)
        computer_score = cal_score(computer_cards)

        while not game_over:
            print(
                f'Your card: {your_cards}. Current score is {cal_score(your_cards)}')
            print(f"First card of computer is: [{computer_cards[0]}]")
            if your_score == 0 or computer_score == 0 or your_score >= 21:
                game_over = True
            else:
                get_card = input(
                    "Type 'y' to get another card, type 'n' to pass \n")
                if get_card == 'y':
                    new_card = deal_card()
                    your_cards.append(new_card)
                    your_score = cal_score(your_cards)
                else:
                    game_over = True

        while computer_score < 17 and computer_score != 0:
            new_card = deal_card()
            computer_cards.append(new_card)
            computer_score = cal_score(computer_cards)
        print(
            f"Your final hand: {your_cards}. Final your score is {your_score}")
        print(
            f'Computer final hand: {computer_cards}. Final computer score is {computer_score}')
        compare(your_cards, computer_cards)
        restart_game = input("Type 'y' to restart game. Type 'n' to stop")
        if restart_game == 'y':
            os.system('cls')
            black_jack_game()
    else:
        print("Bye. See you again!")
        os.system('cls')
        black_jack_game()


black_jack_game()
