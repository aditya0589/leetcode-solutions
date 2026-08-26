class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))

        result = []

        for num in nums:
            result.append(num ** 2)

        return result
