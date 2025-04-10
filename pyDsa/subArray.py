nums = list(map(int, input().split()))

l = len(nums)+1

for i in range(l):
    for j in range(i,l):
        for k in range(i,j):
            print(nums[k], end=' ')
        print()
