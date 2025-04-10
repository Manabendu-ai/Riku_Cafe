from collections import deque as dq

d = dq()

d.append(1)
d.append(10)
d.append(50)
d.appendleft(-10)

d.extendleft([8,-9,-6])

print(d)

d.rotate(1)
print(d)

d.rotate(3)
print(d)

def game():
    nums = dq()
    nums.extend([0,1,0,0,0,0,0])
    i = 0
    while nums[-1] != 1:
        press = int(input())
        nums.rotate(press)
        print(nums)
    print(nums)

game()