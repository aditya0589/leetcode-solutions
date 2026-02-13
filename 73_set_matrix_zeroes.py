matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

indexes = []

# Step 1: Store positions of zeros
for i in range(len(matrix)):
    for j in range(len(matrix[0])):  # view the size of a typical row in the matrix
        if matrix[i][j] == 0:
            indexes.append((i, j))

# Step 2: Set rows and columns to zero
for i, j in indexes:
    # Make entire row zero
    for col in range(len(matrix[0])):
        matrix[i][col] = 0

    # Make entire column zero
    for row in range(len(matrix)):
        matrix[row][j] = 0

print(matrix)
