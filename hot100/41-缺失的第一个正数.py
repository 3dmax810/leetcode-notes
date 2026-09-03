# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

# 示例 1：

# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
# 示例 2：

# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
# 示例 3：

# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。


# 注：ls.index() 和 if i in ls 这两个方法的时间复杂度都是 O(n)，所以不能使用
# 注：if i in dct 这个方法的时间复杂度是 O(1)，hash 所以可以使用

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ls = dict()
        for i in nums:
            ls[i] = 1
        for i in range(1, n+2):
            if i not in ls:
                return i
            
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            val = abs(nums[i])
            if val<=n:
                if nums[val-1]>0:
                    nums[val-1] = -nums[val-1]
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1