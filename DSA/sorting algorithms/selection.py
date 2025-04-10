def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min] :
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr

print(selection_sort([1,10,2,8,5,13]))