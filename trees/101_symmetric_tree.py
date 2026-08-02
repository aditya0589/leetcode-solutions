# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, leftTree, rightTree):
        if not leftTree and not rightTree:
            return True

        if not leftTree or not rightTree:
            return False

        return (leftTree.val == rightTree.val and self.dfs(leftTree.left, rightTree.right) and self.dfs(leftTree.right, rightTree.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
