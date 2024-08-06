import os


def calculator(f_number, option, next_number):
    result_calc = eval(str(f_number) + option + str(next_number))
    return result_calc


def print_logo():
    print("""Final Project Day 10""")
    print(
        """
        _ _ _ _ _ _ _ _ _ _ _ _ _ _                        
    |  _ _ _ _ _ _ _ _ _ _ _ _  |   .---------------.   .------------------.   .------------------.   .---------------.
    | |                     0.| |  | .-------------. | | .----------------. | | .----------------. | | .-------------. |
    | |_ _ _ _ _ _ _ _ _ _ _ _| |  | |    _ _ _ _  | | | |      _  _      | | | |    _ _ _ _     | | | |    _ _ _ _  | |  
    |  _ _ _ _ _ _ _ _ _   _ _  |  | |  .' _ _   | | | | |     /    \     | | | |   |_     _|    | | | |  .' _ _   | | |
    | |  7  |  8  |  9  | | + | |  | | / .'    \_| | | | |    /  /\  \    | | | |     |   |      | | | | / .'    \_| | |
    | |_ _ _|_ _ _|_ _ _| |_ _| |  | | | |         | | | |   /  _  _  \   | | | |     |   |    _ | | | | | |         | |
    | |  4  |  5  |  6  | | - | |  | | \ '._ _ _'\ | | | | _/  /    \  \_ | | | |    _|   |_ _/ || | | | \ '._ _ _'\ | |
    | |_ _ _|_ _ _|_ _ _| |_ _| |  | |  `._ _ _ .' | | | ||_ _ _|  |_ _ _|| | | |   |_ _ _ _ _ _|| | | |  `. _ _ _ .'| |
    | |  1  |  2  |  3  | | * | |  | |             | | | |                | | | |                | | | |             | |
    | |_ _ _|_ _ _|_ _ _| |_ _| |  | '-------------' | | '----------------' | | '----------------' | | '-------------' |
    | |  .  |  0  |  =  | | / | |   '---------------'   '------------------'   '------------------'   '---------------'
    | |_ _ _|_ _ _|_ _ _| |_ _| |
    |_ _ _ _ _ _ _ _ _ _ _ _ _ _|
    """)


def program_running():
    print_logo()
    result = 0
    first_number = int(input("What is first number?:\n"))
    while True:
        print(
            """
        Option 1: +
        Option 2: -
        Option 3: *
        Option 4: /
        """)
        choose = input("What is your option?:\n")
        next_number = int(input("What is next number?:\n"))
        result = calculator(first_number, choose, next_number)
        print(f"{first_number} {choose} {next_number} = {result}")
        should_calc = input(
            f"Type 'y' to coutinue calculator {result}. Or type 'n' to start new calculator")
        os.system('cls')
        if should_calc == 'n':
            result = 0
            program_running()
            break
        else:
            first_number = result


program_running()
