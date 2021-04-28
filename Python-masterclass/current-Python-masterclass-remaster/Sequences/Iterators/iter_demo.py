nums = [1, 2, 3]

i_nums = iter(nums)  # nums.__iter__()
print(dir(i_nums))
print(i_nums)

print(next(i_nums))
print(next(i_nums))

for num in nums:
    print(num)

