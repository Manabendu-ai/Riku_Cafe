from itertools import combinations, combinations_with_replacement

nums = [1,9,8,6]

comb = combinations(nums,2)
print(list(comb))
comb_wr = combinations_with_replacement(nums,2)
print(list(comb_wr))
