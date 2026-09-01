# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

# 示例 1:

# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:

# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
 

# 提示：

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# 输入 保证 数组 answer[i] 在  32 位 整数范围内
 

# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）


# 定义左乘积列表，右乘积列表，然后相乘
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre = [1]
        post = [1]
        #  统计公共前缀和后缀
        temp = 1
        for i in range(1, n):
            temp = temp * nums[i-1]
            pre.append(temp)
        temp = 1
        for i in range(n-2, -1,-1):
            temp = temp * nums[i+1]
            post.append(temp)
        post.reverse()
        out = [i*j for i,j in zip(pre,post)]
        return out

# left作为ouput,定义R作为右的临时乘积，再和left对应元素乘
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = [1]
        #  统计公共前缀和后缀
        temp = 1
        for i in range(1, n):
            temp = temp * nums[i-1]
            out.append(temp)
        temp = 1
        for i in range(n-2, -1,-1):
            temp = temp * nums[i+1]
            out[i]=out[i]*temp
        return out
