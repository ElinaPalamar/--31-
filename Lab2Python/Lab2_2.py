import math
from moduleFunc import sum_of_digits

def calc_expression(x):
    return math.exp(x) + math.sqrt(x)

try:
    x = float(input("Введіть число х: "))
    z = calc_expression(x)
    print("В результаті z =", z)

    n = int(input("Введіть ціле число n: "))
    sum_result = sum_of_digits(n)
    print("Сума цифр числа n дорівнює:", sum_result)
except ValueError:
    print("Введене значення має бути числовим!")