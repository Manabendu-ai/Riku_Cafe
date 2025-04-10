array = [8,5,9,1,6,7]

def mergeSort(array, l, r):
    if l<r:
        mid = (l + r) // 2
        mergeSort(array, l, mid)
        mergeSort(array, mid + 1, r)
        merge(array, l, mid, r)


def merge(array,l,mid,r):
    larr = array[l:mid + 1]
    rarr = array[mid + 1:r + 1]
    i=0
    j=0
    k=l
    while i<len(larr) and j <len(rarr):
        if larr[i] <= rarr[j]:
            array[k] = larr[i]
            i+=1
        else:
            array[k] = rarr[j]
            j+=1
        k+=1

    while i<len(larr):
        array[k] = larr[i]
        i+=1
        k+=1
    while j<len(rarr):
        array[k] = rarr[j]
        j+=1
        k+=1




mergeSort(array, 0, len(array)-1)
print(array)