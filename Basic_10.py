# Function whit output

# def return_function():
#     result = 1 + 1
#     return result


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# formated_name = format_name('NGUYEN', 'duong')
# print(formated_name)

# Ex

def is_leap(year):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False


def days_of_month(year, month):
    day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 0 and month > 12:
        return "Month not valid"
    if is_leap(year) and month == 2:
        return day_of_month[month-1] + 1
    return day_of_month[month-1]


year = int(input("\n"))
month = int(input("\n"))
days = days_of_month(year, month)
print(days)
