n = int(input("Введіть чотиризначне натуральне число: "))

if 1000 <= n <= 9999:
    max_digit = max(int(digit) for digit in str(n))
    print("Найбільша цифра в числі:", max_digit)
else:
    print("Введене число не є чотиризначним!")
