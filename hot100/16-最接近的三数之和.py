# 给定一个长度为 n 的整数数组 nums 和 一个整数 target。

# 请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。

# 返回这三个数的和。

# 假定每组输入只存在 恰好 一个解。

 

# 示例 1：

# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
# 示例 2：

# 输入：nums = [0,0,0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
 

# 提示：

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

# 注意：
# 最接近：best应该保存的是三数和，而不是差值

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ls = nums
        def partition(ls, left, right):
            x = (left + right)//2
            ls[x], ls[left] = ls[left], ls[x]
            temp = ls[left]
            start = left
            while left < right:
                while left < right and ls[right] >= temp:
                    right -= 1
                while left < right and ls[left] <= temp:
                    left += 1
                ls[left], ls[right] = ls[right], ls[left]
            
            ls[start], ls[left] = ls[left], ls[start] # 为什么必须有交换
            return left

        def quicksort(ls, left, right):
            if left >= right:
                return 
            x = partition(ls, left, right)
            quicksort(ls, left, x-1)
            quicksort(ls, x+1, right)

        n = len(ls)
        quicksort(ls, 0, n-1)
        print(ls)
        best_distance = float('inf')
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                temp = ls[i]+ls[left]+ls[right]
                if temp == target:
                    return target
                else:
                    if abs(target-best_distance) > abs(target-temp):
                        best_distance = temp
                    if temp < target:
                        left += 1
                        while left < right and ls[left] == ls[left-1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and ls[right] == ls[right+1]:
                            right -= 1
        return best_distance