import random as rd

min_length = 3
max_length = 7
lst_word = ['cat', 'apple', 'animal', 'heart', 'swim',
            'batminton', 'football', 'camel', 'vegetable',
            'important', 'online', 'streamer', 'police',
            'strawberry', 'watermelon', 'english', 'poland',
            'red', 'ballon', 'language', 'lamp']

states = [
    """
    + - - - +
    |       |
    O       |
            |
            |
            |
            |
= = = = = = =            
    """,
    """
    + - - - +
    |       |
    O       |
    |       |
            |
            |
            |
= = = = = = =            
    """,
    """
    + - - - +
    |       |
    O       |
   /|       |
            |
            |
            |
= = = = = = =            
    """,
    """
    + - - - +
    |       |
    O       |
   /|\      |
            |
            |
            |
= = = = = = =            
    """,
    """
    + - - - +
    |       |
    O       |
   /|\      |
   /        |
            |
            |
= = = = = = =            
    """,
    """
    + - - - +
    |       |
    O       |
   /|\      |
   / \      |
            |
            |
= = = = = = =            
    """,
]

states.reverse()
key_word = rd.choice(lst_word)

generator_word = ['_' for _ in range(len(key_word))]
life = 6
end_of_games = False
print(" ".join(generator_word))
while not end_of_games:
    player_choice = input("Guest a letter: \n")
    for i in range(len(key_word)):
        if key_word[i] == player_choice:
            generator_word[i] = player_choice
    print(" ".join(generator_word))
    if player_choice not in key_word:
        print(states[life-1])
        life -= 1
    if '_' not in generator_word:
        end_of_games = True
        print("You win!")
    if life == 0:
        print("Game Over!")
        break
