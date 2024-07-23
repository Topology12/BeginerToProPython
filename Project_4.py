import random
print("Welcome go to the Rock Paper Scissors Game")
rock = """
      _ _ _ _ _
_ _ _'    _ _ _)
        (_ _ _ _ _)
        (_ _ _ _ _)
_ _ _   (_ _ _ _)
     '_ (_ _ _)
"""
paper = """
        _ _ _ 
_ _ _ '  _ _ _ )_ 
            _ _ _ )_
            _ _ _ _ _)
_ _ _     _ _ _ _ _)
      '_ _ _ _)
"""
scrissor = """
        _ _ _ _
_ _ _ '     _ _)_ _ _
            _ _ _ _ _ )_
              _ _ _ _ _ )
_ _ _     (_ _ _ _)       
     '_ _(_ _ _)               

"""
list_option = [rock, paper, scrissor]
user_choice = int(
    input("What do you choice? Type 0 is Rock, 1 is Paper and 2 is Scissors"))

if user_choice <= 2 and user_choice >= 0:
    print("You choice", list_option[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer choice", list_option[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    else:
        print("Draw!")
else:
    print("You choice not valid!, You lose!")
