# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
# 示例 1：

# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：

# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：

# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/2?2 = 1/4 = 0.25

# 注意：
# 不要使用 round，使用后默认已经发生了影响精度的操作
# 若n<0，x取-x再累积乘积，会导致大的误差。应该在最后用1除以sum，避免误差累积。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPow(x: float, n: int) -> float:
            rec = 1.0
            while n > 0:
                if n & 1 == 1:
                    rec *= x
                x *= x
                n >>= 1
            return rec
        if n < 0:
            return 1/quickPow(x, -n)
        return quickPow(x, n)