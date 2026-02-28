nums = [2,5,6,0,0,1,2]
target = 3
left = 0
isFound = False
right = len(nums)-1

while left <= right:
    mid = left + (right-left) // 2
    
    if nums[mid] == target:
        isFound = True
        break
    
    if nums[left] <= nums[mid]:
        if nums[mid] < target and target < nums[left]:
            left = mid+1
        else:
            right = mid-1
            
    else:
        if target < nums[mid] and target > nums[right]:
            right = mid-1
        else:
            left = mid+1
            
print(isFound)
            
