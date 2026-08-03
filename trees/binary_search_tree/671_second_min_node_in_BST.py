class Solution:
    def traverse(self, root):
        if root is None:
            return []

        return (
            self.traverse(root.left)
            + [root.val]
            + self.traverse(root.right)
        )

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = self.traverse(root)

        arr = list(set(arr))
        arr.sort()

        if len(arr) < 2:
            return -1

        return arr[1]
