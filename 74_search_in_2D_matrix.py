matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

ROWS = len(matrix)
COLS = len(matrix[0])

top, bottom = 0, ROWS-1
while top <= bottom:
    row = top + (bottom-top) // 2
    if target > matrix[row][-1]:
        top = row+1
    elif target < matrix[row][0]:
        bottom = row-1
    else:
        break

if not (top <= bottom):
    print(False)

row =top + (bottom - top) // 2
left, right = 0, COLS-1
while left <= right:
    mid = left + (right-left) // 2
    if target == matrix[row][mid]:
        print(True)
        break
    elif target < matrix[row][mid]:
        right = mid-1
    elif target > matrix[row][mid]:
        left = mid+1
    else:
        print(False)
    
        
