# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]

# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
 
# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000

# 当**第一组就发生反转**的时候，原来的 `head` 已经不再是链表头了！所以不能直接返回 head ，而是返回 dummy.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseListNode(self, pre: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = pre.next
        for _ in range(k-1):
            removed = cur.next
            cur.next = removed.next
            removed.next = pre.next
            pre.next = removed
        return cur
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        while True:
            check = pre
            for _ in range(k):
                check = check.next
                if check==None:
                    return dummy.next
            pre = self.reverseListNode(pre, k)
                