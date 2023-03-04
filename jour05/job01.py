def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Entrez un nombre entier : "))
factorial = factorial(number)
print(f"La factorielle de {number} est : {factorial}")