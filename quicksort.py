arr=[7,9,0,2,4,8,6]

def pivot(arr, low, high):
    pos = low
    for i in range(low, high):
        if arr[i] <= arr[high]:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1
    arr[pos], arr[high] = arr[high], arr[pos]
    return pos

def quicksort(arr, low, high):
    if low >= high:
        return

    pi = pivot(arr, low, high)

    quicksort(arr, low, pi - 1)
    quicksort(arr, pi + 1, high)

quicksort(arr,0,len(arr)-1)
print(*arr)
