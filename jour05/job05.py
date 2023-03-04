def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 23
list_fibonacci = fibonacci(n)
print(f"Le {n}-ème nombre de la suite de Fibonacci est : {list_fibonacci}")