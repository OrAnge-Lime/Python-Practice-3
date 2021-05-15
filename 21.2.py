def transpose(matrix):
    for i in range(matrix.__len__()):
        for j in range(matrix[i].__len__()):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
