nums = list(map(int, input().split()))
n = len(nums)
for i in range(n//2):
    nums[i],nums[n-i-1] = nums[n-i-1],nums[i]

print(nums)

si = 0
ei = n-1

while(si<ei):
    nums[si],nums[ei] = nums[ei],nums[si]
    si+=1
    ei-=1


print(nums)
