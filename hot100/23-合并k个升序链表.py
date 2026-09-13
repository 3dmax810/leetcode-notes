# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

# 示例 1：

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：

# 输入：lists = []
# 输出：[]
# 示例 3：

# 输入：lists = [[]]
# 输出：[]
 

# 提示：

# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4

# 问题在于:复杂度,以及关键边界判断
# 如果是每添加一个元素就判断k个链表,则复杂度是O(KN)
# 如果是按层添加,复杂度是O(Nlog2K)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeLists(self, p1, p2):
        dummy = ListNode()
        ptr = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                ptr.next = p1
                p1 = p1.next
            else:
                ptr.next = p2
                p2 = p2.next
            ptr = ptr.next
        ptr.next = p1 if p1 else p2
        return dummy.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        while n > 1:
            merged = []
            for i in range(0, n, 2):
                ls1 = lists[i]
                ls2 = lists[i+1] if (i+1)<n else None
                merged.append(self.mergeLists(ls1, ls2))
            lists = merged
            n = len(lists)
        return lists[0]
    
    
# 方法三,使用最小堆,插入取出元素
# heapq 的插入,移除方法
# heapq.heappush(堆名, (val, id, node))  这里补充id是因为val相同的情况下,自动比较元组的下一位
# val,id,node = heapq.heappop(堆名) 插入和移除的形式要一致
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        n = len(lists)
        for id, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, id, node))
        dummy = ListNode()
        ptr = dummy
        while heap:
            tmin, id, node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
        return dummy.next