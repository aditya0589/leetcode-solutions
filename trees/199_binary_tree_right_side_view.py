# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.queue = []

    # Insert element at the rear
    def push(self, value):
        self.queue.append(value)

    # Remove and return the front element
    def pop(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        return self.queue.pop(0)

    # Return the front element
    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[0]

    # Return the size of the queue
    def size(self):
        return len(self.queue)

    # Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = Queue()
        ans = []

        if root is None:
            return ans

        queue.push(root)
        ans.append(root.val)
        

        while queue.size() > 0:
            l = queue.size()

            level = []

            for i in range(l):
                front = queue.pop()

                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)

                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)
            if len(level) > 0:
                ans.append(level[-1])

        return ans
