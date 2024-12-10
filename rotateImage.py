def rotate_with_space(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    return rotated

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print("Original:")
# for row in matrix:
#     print(row)

# rotated = rotate_with_space(matrix)
# print("\nRotated:")
# for row in rotated:
#     print(row)



def rotate_transpose_reverse(mat):
    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(i, c):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(r):
        mat[i] = mat[i][::-1]
        
    return mat


rotated = rotate_transpose_reverse(matrix)
print("\nRotated:")
for row in rotated:
    print(row)