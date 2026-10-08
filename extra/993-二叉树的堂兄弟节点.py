# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false

# 示例 1：
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 示例 2：
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info = {}
        def dfs(node, parent, depth):
            if not node:
                return None
            if node.val == x or node.val == y:
                info[node.val] = (depth, parent)
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)

        dfs(root, None, 0)
        dx, px = info[x]
        dy, py = info[y]
        return dx == dy and px != py