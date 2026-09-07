# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.

# 示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]

# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. **不要在循环里无条件创建下一个节点**：先算当前位；下一轮要用到的时候，再生成节点。
# 2. while 退出后，如果进位`pre>0`，要额外 append 一个进位节点。
# 3. 常用技巧：**虚拟头结点 dummy**，避免处理头节点特殊逻辑。

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        p1, p2 = l1, l2
        pre = 0
        while p1 is not None or p2 is not None or pre!=0:
            temp = pre
            if p1!=None:
                temp += p1.val
                p1 = p1.next
            if p2!=None:
                temp += p2.val
                p2 = p2.next
            pre = temp // 10
            ptr.next = ListNode(temp % 10)
            ptr = ptr.next
        return head.next