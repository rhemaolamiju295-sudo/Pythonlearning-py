nums = [3, 8, 1, 6]

smallest = nums[0]

for x in nums:
    if x < smallest:
        smallest = x
print(smallest)