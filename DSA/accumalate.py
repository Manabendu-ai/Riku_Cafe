from itertools import accumulate as ac
import operator

a = [1,2,3,4]
acc = ac(a)
print(list(acc))

pr = ac(a,func = operator.mul)
print(list(pr))


mx = ac(a, func=max)
print(list(mx))

sum = lambda x,y: x+y
print(sum(20,12))