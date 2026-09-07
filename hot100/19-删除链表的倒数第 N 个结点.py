# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

# 示例 1：


# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：

# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：

# 输入：head = [1,2], n = 1
# 输出：[1]
 

# 提示：

# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 

# 进阶：你能尝试使用一趟扫描实现吗？


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 通过在head之前新增一个dummy结点，保证 length-n+1的合法，随后返回dummy.next；同时，删除头节点也不会被影响

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getlength(head:ListNode) -> int:
            p = head
            length = 0
            while p:
                p = p.next
                length += 1
            return length
        
        length = getlength(head)
        dummy = ListNode(0, head)
        cur = dummy
        for _ in range(1, length-n+1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next