"""Class in object-oriented programing"""

class User:
    def __init__(self, id_number, name: str):
        self.id = id_number
        self.username = name

    def check_valid_username(self):
        if self.username[0].isupper():
            return True
        else:
            return False


user_1 = User(1, "Duong")
user_2 = User(2, "Quynh")
if user_1.check_valid_username:
    print(user_1.username)










