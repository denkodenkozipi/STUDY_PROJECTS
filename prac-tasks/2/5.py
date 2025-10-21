def chet():
    n = list(map(int, input().split()))
    total_2 = 0
    total_1 = 0
    for i in n:
        if i % 2 == 0:
            total_2 += 1
        else:
            total_1 += 1
    return f'Массив {n}\nЧетные = {total_2}\nНе четные = {total_1}'

print(resul:=chet())

'''
O-большое = количеству элементов массива
по этому O(n)
'''