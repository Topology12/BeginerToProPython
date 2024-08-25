# Global Variable and Local Variable
enemies = 1


def increase_enemies():
    enemies = 2
    print(f'enemies inside function {enemies}')


increase_enemies()
print(f'enemies outside function {enemies}')

# Constant

PI = 3.131452

# Python no block code
if True:
    result = True
print(result)
