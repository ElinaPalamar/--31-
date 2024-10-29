a = int(input("Введіть додатне число а: "))

while (a <= 0):
    a = int(input("Введіть ДОДАТНЕ а: "))

b = int(input("Введіть додатне число b: "))

while (b <= 0):
    b = int(input("Введіть ДОДАТНЕ b: "))

if a > b:
    x = b * a + 1
elif a == b:
    x = -10
else:
    x = (a - 5) / b

print("Значення х: ", float(x))

