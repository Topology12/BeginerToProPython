import random
letter = []
letter_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_lower = letter_upper.lower()
letter.extend(list(letter_upper))
letter.extend(list(letter_lower))
print(letter)
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+"]

print("Welcome to PyPassWord Generator!")

num_of_letter = int(input("How many letter would you like your password?\n"))
num_of_number = int(input("How many number would like?\n"))
num_of_symbol = int(input("How many symbol would you like?\n"))

letter_string = ""
for i in range(num_of_letter):
    letter_string += random.choice(letter)

number_string = ""
for i in range(num_of_number):
    number_string += random.choice(number)

symbol_string = ""
for i in range(num_of_symbol):
    symbol_string += random.choice(symbol)

your_password = letter_string + number_string + symbol_string

print(f"Your PassWord is : {your_password}")
