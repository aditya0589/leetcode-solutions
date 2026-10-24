class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxCount = 0
        found = set()
        for right in range(len(s)):
            while s[right] in found:
                found.remove(s[left])
                left += 1

            found.add(s[right])
            maxCount = max(right-left+1, maxCount) 

        return maxCount
                
