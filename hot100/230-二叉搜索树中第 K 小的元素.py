# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。

# 1.输入：root = [3,1,4,null,2], k = 1
# 输出：1

# 2.输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3

# 提示：

# 树中的节点数为 n 。
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 

# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

# 二叉搜索树的性质：左子树均小于根节点，右子树均大于根节点
# 可以通过中序遍历，获取完整的排序顺序，然后选取第k个元素

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中序遍历
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, ls):
            if not node:
                return
            temp = helper(node.left, ls)
            ls.append(node.val)
            if len(ls) >= k:
                return ls[k-1]
            temp = helper(node.right, ls)
        ls = []
        x = helper(root, ls)
        return ls[k-1]

# 若二叉树频繁插入删除
# 新建一个类，维护一个哈希字典，存储每个子节点含有的节点数，每次插入删除时，更新数组，查找第k小的元素时直接返回数组的第k个元素
# 若左字数节点数<need，转右子树，然后在右子树里遍历左子树或右子树。若>need，转左子树里的左子树或右子树遍历