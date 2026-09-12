# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# 示例1:
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]

# 示例2:
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 注:里面可能存在val值相等的情况,假如存为dict,会导致丢失元素

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        ptr = head
        ls = []
        while ptr:
            ls.append(ptr)
            ptr = ptr.next
        ls.sort(key=lambda x:x.val)
        dummy = ListNode()
        ptr = dummy
        for i in ls:
            ptr.next = i
            ptr = ptr.next
        ptr.next = None
        return dummy.next