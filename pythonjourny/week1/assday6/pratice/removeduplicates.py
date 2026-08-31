nums = [1, 2, 2, 3, 4, 4, 5]
numbs = set(nums)
print(numbs)
num = []
for x in nums:
    if x not in num:
        num.append(x)
print(num)