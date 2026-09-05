# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表。

# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 注：假设链表：   长a到环开始的距离   ————   快慢指针相遇的地方 b  ——————  回到环开始的地方c
# 公式为：
# 快：a+N(b+c)+b  慢：a+b
# a+N(b+c)+b = 2(a+b) 
# NL-b = a
# (N-1)L + c = a
# 所以，在快慢指针相遇后，ptr从head开始，slow从c处开始走会相遇，相遇的终点是环的起点

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow = head
        fast = head
        while fast!=None:
            slow = slow.next
            if fast.next == None:
                return None
            fast = fast.next.next
            if fast == slow:
                ptr = head
                while ptr!=slow:
                    ptr=ptr.next
                    slow=slow.next
                return ptr
        return None