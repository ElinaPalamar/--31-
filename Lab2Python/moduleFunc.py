def sum_of_digits(n):
    sum_digits = 0

    for digit in str(abs(n)):
        sum_digits += int(digit)
    return sum_digits