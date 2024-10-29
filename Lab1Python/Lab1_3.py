N = int(input("Введіть ціле число N (1 < N < 9): "))

if 1 < N < 9:
    for i in range(N, 0, -1):
        print(str(N) * i)

    for i in range(1, N + 1):
        print(str(N) * i)
else:
    print("Число N має бути в межах від 2 до 8.")
