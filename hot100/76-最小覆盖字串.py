# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

# 测试用例保证答案唯一。 

# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。

# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

from collections import defaultdict

class Solution(object):
    # 暴力求解
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ns = len(s)
        nt = len(t)
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        rec = ""
        for i in t:
            count_t[i] += 1
        for x in range(ns-nt+1):
            for y in range(x+nt, ns+1):
                temp = s[x:y]
                count_s.clear()

                for i in temp:
                    count_s[i] += 1
                state = True
                for i in count_t:
                    if count_t[i] <= count_s[i]:
                        continue
                    else:
                        state = False
                        break
                if state==True:
                    rec = temp if (not rec or len(temp) < len(rec)) else rec
        return rec
    
    
from collections import defaultdict

class Solution(object):
    # 使用滑动窗口，但复杂度m*n
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ns = len(s)
        nt = len(t)
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        rec = ""
        for i in t:
            count_t[i] += 1
        left = 0
        for right in range(ns):
            count_s[s[right]] += 1
            def check():  # 定义函数帮忙判断是否滑动窗口包含了t
                for i in count_t:
                    if count_s[i] < count_t[i]:
                        return False
                return True
            while check(): # 滑动窗口包含t
                cur = s[left:right+1]
                if not rec or len(rec)>len(cur):  # 注意 or
                    rec = cur 
                count_s[s[left]] -= 1
                left += 1
        return rec
            

#  引入distance     
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        windows = defaultdict(int)
        need = defaultdict(int)
        n = len(s)
        left = 0
        start = 0
        min_len = n + 1
        distance = 0
        for i in t:
            need[i] += 1
        for right in range(n):
            windows[s[right]] += 1
            if s[right] in need:
                if need[s[right]] == windows[s[right]]:
                    distance += 1
            while distance == len(need):
                cleft = s[left]
                temp_len = right - left + 1
                if temp_len < min_len:
                    min_len = temp_len
                    start = left
                left += 1
                if cleft in need:
                    if need[cleft] == windows[cleft]:
                        distance -= 1
                windows[cleft] -= 1
        if min_len == n +1:
            return ""
        return s[start:start + min_len]
