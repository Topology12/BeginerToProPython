import math
# Function with input

# def love(name: str, date: str) -> None:
#     print('I love ' + name)
#     print('In ' + date)


# love('Quynh', '13/1/2024')

# height = int(input('Height?\n'))
# width = int(input('Width?\n'))
# coverage = 5


# def paint_calc(height, width, coverage):
#     num_of_can = (height*width) / coverage
#     round_can = math.ceil(num_of_can)
#     print(f"Number of can {round_can}")


# paint_calc(height=height, coverage=coverage, width=width)

def prime_checked(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime = False
    return is_prime


number = int(input("Number?\n"))
print(prime_checked(number=number))
