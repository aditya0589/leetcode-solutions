class Solution:
    def findPeakElement(self, nums):
        current = 0
        max_val = float('-inf')
        value = 0

        for i in range(len(nums)):
            current = nums[i]
            max_val = max(current, max_val)
