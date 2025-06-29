n = int(input())

nums = []

for i in range(n):
    data = [int(el) for el in input().split(", ")]
    nums.extend(data)

print(nums)