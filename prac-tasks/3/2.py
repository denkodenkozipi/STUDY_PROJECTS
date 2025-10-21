def Insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [64, 25, 12, 22, 11]
print("Исходный массив:", arr)
print("Отсортированный массив:", Insertion(arr.copy()))