from itertools import groupby

def smaller_than_3(x):
    return x<3

a = [1,2,3,4]
grp_obj = groupby(a, key=smaller_than_3)
for key, val in grp_obj:
    print(key, list(val))

def check(name):
    if name in "deeksha":
        return True
    return False

name = "manabendu"
name_obj = groupby(name, key=check)
inter = []
for key, val in name_obj:
    if key == True:
        inter.append(list(val))

print(inter)