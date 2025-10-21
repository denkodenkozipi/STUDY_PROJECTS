def vrem(a, b):
    print(f'Начало функции:\na = {a}\nb = {b}')
    temp = a
    a = b
    b = temp
    return f'Конец функции:\na = {a}\nb = {b}'

def nvrem(a, b):
    print(f'Начало функции:\na = {a}\nb = {b}')
    a, b = b, a
    return f'Конец функции:\na = {a}\nb = {b}'

def arifm(a, b):
    print(f'Начало функции:\na = {a}\nb = {b}')
    a += b
    b = a - b
    a -= b
    return f'Конец функции:\na = {a}\nb = {b}'

def xor(a, b):
    print(f'Начало функции:\na = {a}\nb = {b}')
    a ^= b
    b = a ^ b
    a ^= b
    return f'Конец функции:\na = {a}\nb = {b}'


text = \
'''
Выберете способ
1. Временная переменная 
2. Временная переменная (PY)
3. Арифметическая
4. XOR
>>> '''

a = int(input('a?\n>>> '))
b = int(input('b?\n>>> '))
choice = str(input(text))

if  choice == "1":
    print(resul:=vrem(a, b))
elif choice == "2":
    print(resul:=nvrem(a, b))
elif choice == "3":
    print(resul:=arifm(a, b))
elif choice == "4":
    print(resul:=xor(a, b))
else:
    input('! ! !')

'''
функции выполняют не зависимо от ввода 
по этому каждая функция имеет O(1)
'''