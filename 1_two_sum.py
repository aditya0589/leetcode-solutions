nums = [3,2,4]
target = 6
dictionary = {}

for i in range(len(nums)):
    remaining = target - nums[i]
    if remaining in dictionary:
        print((i, dictionary[remaining]))
        break
    else:
        dictionary[nums[i]] = i
