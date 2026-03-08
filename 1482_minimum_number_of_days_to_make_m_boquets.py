class Solution:
    def minDays(self, bloomDay, m, k):
        
        if m * k > len(bloomDay):
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)
        answer = -1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            count = 0
            curr = 0
            
            for flower in bloomDay:
                if flower <= mid:
                    count += 1
                    if count == k:
                        curr += 1
                        count = 0
                else:
                    count = 0
            
            if curr >= m:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
