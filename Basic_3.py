# Conditional Operator, Logical Operator, Code Block, Scope
# Conditional Operator
age = int(input("How old are you?"))

if age >= 18:
    print("You can drive the car ")
else:
    print("You can't drive")

# Ex Odd or Even
number = int(input("Enter the number:  "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
# Elif conditional
score = int(input())

if score == 10:
    print("You is verry briliant")
elif score >= 8:
    print("You is good")
else:
    print("You is bad")

# Pizza Diliveries
size = input("Pizza size: ")
add_pepperoni = input("Add pepperoni? ")
extra_cheese = input("Extra Cheese? ")

bill = 0
if size == "S":
    bill += 5
elif size == "M":
    bill += 10
else:
    bill += 15

if add_pepperoni == "Y" and size == "S":
    bill += 2
else:
    bill += 3

if extra_cheese == "Y":
    bill += 5

print(f"The pizza bill is {bill}")
# True Love Score

name_1 = input("Name 1: ")
name_2 = input("Name 2: ")

name_concat = name_1 + name_2
name_lower = name_concat.lower()
t_score = name_lower.count("t")
r_score = name_lower.count("r")
u_score = name_lower.count("u")
e_score = name_lower.count("e")

first_digit = t_score + r_score + u_score + e_score

l_score = name_lower.count("l")
o_score = name_lower.count("o")
v_score = name_lower.count("v")

second_digit = l_score + r_score + v_score + e_score

print(f"Score True Love is {str(first_digit)+str(second_digit)}")
