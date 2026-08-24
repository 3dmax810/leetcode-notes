# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。

# 示例 1：

# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：

# 输入：nums = [1,2,3], k = 3
# 输出：2

# 提示：

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# 历史错误
class Solution_Error(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rec = 0
        left = 0
        right = 0
        n = len(nums)
        temp = nums[0]
        while right < n and left<=right:
            if temp < k:
                right += 1
                if right<n:
                    temp += nums[right]
            elif temp > k:
                if left == right:
                    left+=1
                    right+=1
                    if right <n:
                        temp = nums[left]
                else:
                    temp -= nums[left]
                    left+=1
            else:
                rec += 1
                right += 1
                if right<n:
                    temp+=nums[right]
                else:
                    break
        return rec

## 错误原因
### 1.每次right/left都需要对temp修改，且right的值限制在n-1以内
### 2.滑动窗口的方式仅针对正数，若存在负数，则<k右移，>k左移的规则可能不成立，如：[-1,-1,1]

## 解法：前缀和 + hash存储
### 字典判断是否存在某值，若不存在则新建并+1
### dct.get(x, 0) + 1
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        countSum = {0:1}
        n = len(nums)
        temp = 0
        rec = 0
        for i in range(n):
            temp += nums[i]
            target = temp - k
            rec += countSum.get(target, 0)
            countSum[temp] = countSum.get(temp, 0) + 1
        return rec