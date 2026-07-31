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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = Queue()
        ans = []

        if root is None:
            return ans

        queue.push(root)
        count = 0

        while queue.size() > 0:
            l = queue.size()
            level = []

            for _ in range(l):
                node = queue.pop()
                level.append(node.val)

                if node.left:
                    queue.push(node.left)

                if node.right:
                    queue.push(node.right)

            if count % 2 == 1:
                level.reverse()

            ans.append(level)
            count += 1

        return ans
