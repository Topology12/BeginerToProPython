# Ramdom module
import random

# Random Integer

random_int = random.randint(1, 5)
print(random_int)

# Random Float

random_float = random.random()
print(random_float)

# Random decimal 0 - 5
decimal = random.random()*random.randint(0, 5)
print(decimal)
# List data structure

province_of_Vietnam = ["Hue", "HoChiMinh",
                       "HaNoi", "DaNang", "CanTho", "HaiPhong"]
province_of_Vietnam.append("HoaBinh")
province_of_Vietnam.extend(["NgheAn"])
print(province_of_Vietnam)

# Nessted List
car = ["BMW", "RollRoy", "Lambogini"]
motobike = ["Suzuki", "Honda", "Yamaha"]
mean_of_transport = [car, motobike]
print(mean_of_transport)
