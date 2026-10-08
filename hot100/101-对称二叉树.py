# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

# 输入：root= [1,2,2,3,4,4,3]
# 输出：true

# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 暴力方法：先复制原node，然后交换，然后逐个对比

class Solution:
    def copy(self, root: Optional[TreeNode]):
        if root:
            rt2 = TreeNode(val=root.val)
            rt2.left = self.copy(root.left)
            rt2.right = self.copy(root.right)
            return rt2 
        else:
            return None

    def exchange(self, root: Optional[TreeNode]):
        if root == None:
            return None
        left = self.exchange(root.left)
        right = self.exchange(root.right)
        root.left, root.right = root.right, root.left
        return root

    def judge(self, root, rt2):
        if not root and not rt2:
            return True
        if (not root and rt2) or (not rt2 and root):
            return False
        if root.val!=rt2.val:
            return False
        return self.judge(root.left, rt2.left) and self.judge(root.right, rt2.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        rt2 = self.copy(root)
        rt2 = self.exchange(rt2)
        return self.judge(root, rt2)
    
# 极简递归
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)