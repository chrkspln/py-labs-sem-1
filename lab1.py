# ЧАСТИНА 1
import requests
url = "https://www.wikipedia.org/"
response = requests.get(url)
print(response.text)

# ЧАСТИНА 2
# завдання 1.28
game = "sims 4"
print(game)

is_student = False
is_teacher = True
result = is_student or is_teacher
print("student or teacher result: ", result)
result = is_student and is_teacher
print("student and teacher result: ", result)
result_s = not is_student
result_t = not is_teacher
print("logical 'not' for student and teacher result: ", result_s, " ", result_t)

is_raining = False
is_snowing = False
print("logical 'not' result: ", not is_raining, " ", not is_snowing)


# завдання 2.28
def formula_function(x, y):
    formula_result = (x * y) ** 1 / 3 + 13 * (x * y) ** 4 - x / y
    print(formula_result)


a = 1.22
b = 3.21
formula_function(a, b)
