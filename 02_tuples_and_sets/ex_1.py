nums = tuple([float(el) for el in input().split()])

data = {}

for el in nums:
    if el not in data:
        data[el] = nums.count(el)


for key, value in data.items():
    print(f"{key:.1f} - {value} times")
