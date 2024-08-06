# Dictionary

# friend = {
#     'Vu': 'Ha Tinh',
#     'Nam': 'Da Nang',
#     'Tuan': 'Quang Tri',
#     'Duc': 'Quang Tri'
# }

# print(friend['Duc'])
# for key in friend:
#     print(key, end='-')
#     print(friend[key])

# Ex
# student_scores = {
#     'Harry': 81,
#     'Ron': 78,
#     'Herminose': 99,
#     'Draco': 74,
#     'Neville': 62,
# }

# student_grades = {}

# for student in student_scores:
#     grade = ''
#     if student_scores[student] > 90:
#         grade = "Outstanding"
#     elif student_scores[student] > 80:
#         grade = 'Exceeds Expectations'
#     elif student_scores[student] > 70:
#         grade = 'Acceptable'
#     else:
#         grade = 'Fail'
#     student_grades[student] = grade

# print(student_grades)
# Ex

country = input()
visits = int(input())
list_of_cities = eval(input())

visit_log = [
    {
        "country": "France",
        "visits": 1,
        "cities": ['Paris', "Lille", "Dijon"]
    },
    {
        'country': 'England',
        'visits': 1,
        'cities': ['Liverpool', 'Manchester', 'London']
    }
]


def add_new_country(country, visits, list_of_cities):
    country_visit = {}
    country_visit['country'] = country
    country_visit['visits'] = visits
    country_visit['list_of_cities'] = list_of_cities
    visit_log.append(country_visit)


add_new_country(country, visits, list_of_cities)
print(visit_log)
