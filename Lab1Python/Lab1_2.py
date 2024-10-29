sum_even = 0
mult_odd = 1

for i in range(21):
    if i % 2 == 0:
        sum_even += i
    else:
        mult_odd *= i

print("Сума парних чисел від 0 до 20:", sum_even)
print("Добуток непарних чисел від 0 до 20:", mult_odd)
