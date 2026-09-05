# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]

# 方法一：迭代法
# 注：这里不需要对默认的顶点默认赋值，而是直接赋值为None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        reList = None
        p = head
        while p:
            temp = p.next
            p.next = reList
            reList = p
            p = temp
        return reList
    

# 方法二：递归法
# 递归地反转链表，从最后一个节点开始，逐个反转每个节点的指针。
# 对head.next.next = head的理解：head.next是当前节点的下一个节点，head.next.next是下一个节点的下一个节点。通过将head.next.next指向head，我们将当前节点的下一个节点的指针指向当前节点，从而实现了反转。
# p1->p2->p3->p4->p5->None
# 假设 p1->p2->p3<-p4<-p5<-None, p3处要反转，p3.next是p4，p3.next.next=p3，完成反转，最后一个head.next=None，结束

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p