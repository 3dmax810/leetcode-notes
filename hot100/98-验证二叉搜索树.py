# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 严格小于 当前节点的数。
# 节点的右子树只包含 严格大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


# 输入：root = [2,1,3]
# 输出：true

# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            left, right = True, True
            if root.left:
                left = helper(root.left, low, root.val)
            if root.right:
                right = helper(root.right, root.val, high)
            return left and right
        return helper(root, -float(inf), float(inf))