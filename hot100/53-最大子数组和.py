# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组是数组中的一个连续部分。

 

# 示例 1：

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：

# 输入：nums = [1]
# 输出：1
# 示例 3：

# 输入：nums = [5,4,-1,7,8]
# 输出：23


# 粗糙的方法：新建dp数组，下三角矩阵，存放前k的数值的和

# 优化方法：第i个位置的最大值 = Max(第i-1个位置的最大值+第i个位置的数值，第i个位置的数值)，第i个元素结尾
# 对比全局最大值 maxAns = max(maxAns, pre)，最大值不一定是第i个元素结尾

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = -10000
        pre = 0
        curTemp = nums[0]
        for i in range(n):
            pre = max(pre+nums[i], nums[i])
            maxSum = max(maxSum, pre)
        return maxSum