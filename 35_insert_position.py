nums = [1,3,5,6]
target = 4
low = 0
high = len(nums)-1
found = False

while low <= high:
    mid = low + (high-low) // 2
    
    if nums[mid] == target:
        print(mid)
        found = True
        break
    if nums[mid] < target:
        low = mid + 1
    if nums[mid] > target:
        high = mid - 1

if not found:
    print(low)  # why return low?
    
    # when high<low (the target is not found and while loop completes),
    # at that time low becomes the ideal position to insert the target value
