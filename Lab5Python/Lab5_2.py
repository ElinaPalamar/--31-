N = 7

matrix = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (i + j) % 2 == 0:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

for row in matrix:
    print(" ".join(map(str, row)))