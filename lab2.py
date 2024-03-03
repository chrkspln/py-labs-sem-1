# завдання 1.28

import math

print("приклад 1.1")
# перший приклад
x1 = 2.1
while x1 <= 3.5:
    result1 = math.log10(math.log(x1) + math.log2(x1))
    print(x1)
    print(result1)
    x1 += 0.05

print("приклад 1.2")
# другий приклад
x2 = 2.5
while x2 <= 3.5:
    result2 = (math.cos(x2) ** 2 + math.cos(x2) / math.sin(x2)) ** 1 / 4
    print(x2)
    print(result2)
    x2 += 0.05

print("приклад 1.3")
# третій приклад
x3 = 3.35
while x3 <= 3.5:
    result3 = math.atan(1 / x3)
    print(x3)
    print(result3)
    x3 += 0.05

# завдання 2.28
print("приклад 2.2")


def function_tab(x_func):
    d = 0.001
    h = 0.1
    k = 1
    result_sum = 0

    while x_func < 3.6:
        while True:
            result_k = (-1 ** (k + 1) * math.cos(k * x_func)) / (x_func + 2 * k) ** 3
            result_sum += result_k
            prev_result_k = result_k
            k += 1
            if abs(result_k - prev_result_k) <= d:
                print("для x = ", round(x_func, 1), " безкінечна сума = ", result_sum)
                break
        x_func += h


x = 1.1
function_tab(x)
