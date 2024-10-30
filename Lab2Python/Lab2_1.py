import math

def calc_expression(x):
    return math.exp(x) + math.sqrt(x)

def sum_of_digits(n):
    sum_digits = 0

    for digit in str(abs(n)):
        sum_digits += int(digit)
    return sum_digits

try:
    x = float(input("Введіть число х: "))
    z = calc_expression(x)
    print("В результаті z =", z)

    n = int(input("Введіть ціле число n: "))
    sum_result = sum_of_digits(n)
    print("Сума цифр числа n дорівнює:", sum_result)
except ValueError:
    print("Введене значення має бути числовим!")
