# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# 解题思路：
# 查看新位置i,j怎么变为原始的x,y
# 可创建同规模矩阵，
# 或者直接在原矩阵上进行操作，4个移动的位置交换值，n//2,n+1//2,表示矩阵的四分之一，而中心是button，中心不需要移动，且均为n+1//2会重复移动导致错误
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return matrix
        for i in range(n//2):
            for j in range((n+1)//2):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] \
                =  matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j] 
