# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 1.
# 输入：root = [1,2,3,null,5,null,4]
# 输出：[1,3,4]

# 2.
# 输入：root = [1,2,3,4,null,null,null,5]
# 输出：[1,3,4,5]


# 通过层序遍历，获取每层末尾元素值来实现
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, ls):
            if not node:
                return ls
            q = collections.deque()
            q.append(node)
            while q:
                n = len(q)
                x = None
                for _ in range(n):
                    x = q.popleft()
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
                ls.append(x.val)
            return ls
        ls = helper(root, [])
        return ls