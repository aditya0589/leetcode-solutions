# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, minimum, maximum):
        if root is None:
            return True

        if root.val > maximum or root.val < minimum:
            return False

        checkLeft = self.check(root.left, minimum, root.val-1)
        checkRight = self.check(root.right, root.val+1, maximum)

        return checkLeft and checkRight

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -1000000000000000, 10000000000000)
