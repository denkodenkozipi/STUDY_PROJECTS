def fac():
    n = int(input('факториал числа n\n>>> '))
    total = 1
    for i in range(1, n + 1):
        total *= i
    return f'факториал числа {n} = {total}'

print(a:=fac())

'''
Из-за факториала числа n
программа O(n)
'''