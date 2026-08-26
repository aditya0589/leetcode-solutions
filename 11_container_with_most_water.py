class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        max_water = 0
        left, right = 0, len(height)-1

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -=1
        
        return max_water





