N = int(input("Введіть довжину масиву: "))

array = []
for i in range(N):
    element = int(input(f"Введіть елемент масиву #{i+1}: "))
    array.append(element)

sum_even_index = sum(array[i] for i in range(0, N, 2))

print("Сума елементів з парними індексами:", sum_even_index)
