def binar(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 8, 12, 13, 16, 20, 23, 25, 38, 40, 45, 67, 89]
target = 45
print("Массив:", arr)
print(f"Ищем элемент {target}: индекс {binar(arr, target)}")