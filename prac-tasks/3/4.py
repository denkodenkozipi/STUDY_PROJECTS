def fiba(n):
    if n <= 1:
        return n
    return fiba(n - 1) + fiba(n - 2)

n = int(input())
print(f"Число Фибоначчи {n} = {fiba(n)}")