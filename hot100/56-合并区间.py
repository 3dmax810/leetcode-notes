# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

# 示例 1：

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：

# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 示例 3：

# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。



# 思路：不需要详细判断i的右端点和j的右端点大小关系，如果<1，则append，如果>，取更大的值
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sIntervals = sorted(intervals, key=lambda x:x[0])
        n = len(sIntervals)
        merged = []
        for interval in sIntervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
                