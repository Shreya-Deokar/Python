"""
Level 2
Initialize a 2D list of 3*3 matrix. E.g.-
1	2	3
4	5	6
7	8	9

Check if the matrix is symmetric or not.
"""
def Symmetric(a):
    for i in range(0,3):
        for j in range(0,3):
            if a[i][j] != a[j][i]:
                return False
    return True

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

if Symmetric(matrix):
    print ("Matrix is symmetric")
else:
    print ("Matrix is not a symmetric")