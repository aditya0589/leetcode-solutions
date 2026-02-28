arr = [4,5,6,7,0,1,2]
target = 3
left = 0
found = False
right = len(arr)-1

while left <= right:
    mid = left + (right-left) // 2
    
    if target == arr[mid]:
        print(mid)
        found = True
        break
    if arr[left] <= arr[mid]:
        if target < arr[mid] and target < arr[left]:
            left = mid+1
        else:
            right = mid-1
    else:
        if target < arr[mid] and target > arr[right]:
            right = mid-1
        else:
            left = mid+1
            
if not found:
    print(-1)
