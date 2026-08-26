# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, list1, list2, resultNode):
        if list1 is None:
            resultNode.next = list2
            return

        if list2 is None:
            resultNode.next = list1
            return

        if list1.val < list2.val:
            resultNode.next = list1
            list1 = list1.next
        else:
            resultNode.next = list2
            list2 = list2.next

        self.mergeNodes(list1, list2, resultNode.next)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = ListNode()

        self.mergeNodes(list1, list2, resultNode)

        return resultNode.next
