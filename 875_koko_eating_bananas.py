import math
piles = [3,6,7,11]
h = 8
search_array = []   # applying binary search on the answers

for i in range(1, max(piles)+1):
    search_array.append(i)

left = 0
right = len(search_array)-1
res = right

while left <= right:
    mid = left + (right-left) // 2
    
    total = 0
    for p in piles:
        total += math.ceil(p/mid)
    if total <= h:
        res = min(res, mid)
        right = mid-1
    else:
        left = mid+1

print(res)
