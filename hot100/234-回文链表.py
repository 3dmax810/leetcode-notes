# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# 输入：head = [1,2,2,1]
# 输出：true

# 输入：head = [1,2]
# 输出：false

# 完整遍历，如果从中间为终点，左边正序，右边反序，如果一致则输出True
# list.reverse() 是原地进行修改

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        length = len(ls)
        if head==None or length==1:
            return True 
        ls1 = ls[:int(length/2)]
        ls2 = ls[-int(length/2):]
        print(ls1, ls2)
        ls2.reverse()
        if ls1 == ls2:
            return True
        else:
            return False

# =======================================

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        return ls == ls[::-1]
