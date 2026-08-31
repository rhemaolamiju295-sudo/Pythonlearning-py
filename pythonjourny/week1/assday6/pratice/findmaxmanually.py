nums = [4, 9, 2, 7]

smallest = nums[0] 
highest = nums[0]

for numbs in nums:
    if numbs > highest:
        highest = numbs
print(highest)