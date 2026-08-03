# use inorder traversal but keep the track to find the kth element

class Solution:
    def __init__(self):
        self.count = 0
        self.answer = None

    def inorder(self, root, k):
        if root is None or self.answer is not None:
            return

        self.inorder(root.left, k)

        self.count += 1
        if self.count == k:
            self.answer = root.val
            return

        self.inorder(root.right, k)

    def kthSmallest(self, root, k):
        self.inorder(root, k)
        return self.answer
