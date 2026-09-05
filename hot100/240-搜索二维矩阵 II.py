# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true

# 失败方法：复杂度过高，这里使用deque进行广度优先搜索，复杂度为O(m*n)，空间复杂度为O(m*n)
# 队列方法：
# deque = collections.deque()
# deque.append() or deque.popleft()
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        dq = deque([[matrix[x][y], x, y]])
        visited = [[False]*n for _ in range(m)]
        while x<m and y<n and dq:
            val, x, y = dq.popleft()
            visited[x][y]=True
            if val == target:
                return True
            elif val < target:
                tempx = x+1
                tempy = y+1
                if tempx<m:
                    if visited[tempx][y] == False:
                        dq.append([matrix[tempx][y], tempx, y])
                if tempy<n:
                    if visited[x][tempy] == False:
                        dq.append([matrix[x][tempy], x, tempy])
                if tempx<m and tempy<n:
                    if visited[tempx][tempy] == False:
                        dq.append([matrix[tempx][tempy], tempx, tempy])
        return False

# 法二：使用双指针，从右往左，从上到下。因为右上角是行中最小、列中最大的；左上角是行列均最小的，移动步数会多。
# 右上角开始，只需比较target和当前值的大小，若target大，则向下移动，若target小，则向左移动。复杂度为O(m+n)，空间复杂度为O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        m = len(matrix)
        n = len(matrix[0])
        row, column = 0, n-1
        while row<m and column>=0:
            cur = matrix[row][column]
            if cur == target:
                return True
            elif cur > target:
                column -= 1
            else:
                row += 1
        return False

        # m = len(matrix)
        # n = len(matrix[0])
        # x = 0
        # y = 0
        # dq = deque([[matrix[x][y], x, y]])
        # visited = [[False]*n for _ in range(m)]
        # while x<m and y<n and dq:
        #     val, x, y = dq.popleft()
        #     visited[x][y]=True
        #     if val == target:
        #         return True
        #     elif val < target:
        #         tempx = x+1
        #         tempy = y+1
        #         if tempx<m:
        #             if visited[tempx][y] == False:
        #                 dq.append([matrix[tempx][y], tempx, y])
        #         if tempy<n:
        #             if visited[x][tempy] == False:
        #                 dq.append([matrix[x][tempy], x, tempy])
        #         if tempx<m and tempy<n:
        #             if visited[tempx][tempy] == False:
        #                 dq.append([matrix[tempx][tempy], tempx, tempy])
        # return False

