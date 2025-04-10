from collections import Counter as co

name = "Manabendu"

my_counter = co(name)

print(my_counter)
print(my_counter.most_common(2))
print(list(my_counter.elements()))