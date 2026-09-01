# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

# 示例 1:

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:

# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
 

# 提示：

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105


# 除了定义额外存储空间，还可通过三次反转获得
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # if k > n:
        #     k = k%n
        # ls = nums[n-k:]
        # nums[:] = ls+nums[:n-k]
        nums[:] = nums[::-1]
        k = k % n
        def reverse(ls, left, right):
            a = left
            b = right
            while a<b:
                ls[a], ls[b] = ls[b], ls[a]
                a+=1
                b-=1
            return ls[left:right+1]
        nums[:k] = reverse(nums, 0, k-1)
        nums[k:] = reverse(nums, k, n-1)

