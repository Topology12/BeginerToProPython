print("Wecome to the tip calculator")
total_bill = input("What is the total bill?")
tip = input("How much tip would you like to give?")
number_of_people = input("How many people to split the bill?")

each_person_pay = (float(total_bill) + float(tip)) / int(number_of_people)
print(f"Each person should pay: ${round(each_person_pay, 2)}")
