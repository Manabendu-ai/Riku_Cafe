arr = [
    [1,2,3,4],
    [5,6,7,8],
    [12,13,45,67],
    [11,9,81,34]
]

for i in range(len(arr)):
    for j in range(i):
        arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

for rows in arr:
    print(rows)