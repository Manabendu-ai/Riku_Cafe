from itertools import permutations

name = "riku"

per_name = permutations(name)
print(list(per_name))

per_name = list(permutations(name, 2))
print(per_name)