def sparseMatixMult(mat1, mat2):
    
    sparse_mat1 = {}
    sparse_mat2 = {}
    
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if mat1[i][j] != 0:
                if i not in sparse_mat1:
                    sparse_mat1[i] = {}
                sparse_mat1[i][j] = mat1[i][j]
    
    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            if mat2[i][j] != 0:
                if i not in sparse_mat2:
                    sparse_mat2[i] = {}
                sparse_mat2[i][j] = mat2[i][j]
    
    res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    
    for i in sparse_mat1:
        for k in sparse_mat1[i]:
            if k in sparse_mat2:
                for j in sparse_mat2[k]:
                    res[i][j] += sparse_mat1[i][k] * sparse_mat2[k][j]
    
    return res


mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(sparseMatixMult(mat1, mat2))


# def sparseMatixMult(mat1, mat2):
    
#     res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

#     # Perform matrix multiplication
#     for i in range(len(mat1)):
#         for j in range(len(mat2[0])):
#             for k in range(len(mat1[0])):
#                 res[i][j] += mat1[i][k] * mat2[k][j]

#     return res

# mat1 = [[1,0,0],[-1,0,3]]
# mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# print(sparseMatixMult(mat1, mat2))

