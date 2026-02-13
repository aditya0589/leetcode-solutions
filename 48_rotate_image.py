# we find that the solution is the reverse of the determinant of the matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")
    print(" ")
    
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  #determinant of the matrix

for i in matrix:
    i.reverse()  # reverse it 
print(" ")
    
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end = " ")
    print(" ")
        
