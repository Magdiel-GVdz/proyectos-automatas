# Ejemplo de código en Python

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = 5
resultado = factorial(numero)

print("El factorial de", numero, "es:", resultado)