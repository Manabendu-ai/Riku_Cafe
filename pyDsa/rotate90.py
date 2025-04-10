arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
n = len(arr)
for i in range(n):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for rows in arr:
    for i in range(len(rows)//2):
        rows[i],rows[len(rows)-i-1] = rows[len(rows)-i-1],rows[i]


for row in arr:
    print(row)