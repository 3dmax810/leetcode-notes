# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回 滑动窗口中的最大值 。


# 示例 1：

# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：

# 输入：nums = [1], k = 1
# 输出：[1]

import heapq
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 队列：队尾进，队首出
        # 双端队列
        # 注：q[0] 表示队首，q[-1] 表示队尾
        n = len(nums)
        q = deque()
        rec = []
        for i in range(n):
            while q and q[0]<=i-k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k-1:
                rec.append(nums[q[0]])
        return rec
    

class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 大根堆
        n = len(nums)
        rec = []
        heap = []
        for i in range(n):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i-k:
                heapq.heappop(heap)
            if i >= k-1:
                rec.append(-heap[0][0])
        return rec
            