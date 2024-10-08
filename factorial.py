#Vicente Y. Lopez V. - 240010
#Factorial de un número

n = int(input("Ingresa un numero entero positivo para calcular su factorial: "))
fac = 1

for i in range (1, n + 1):
    fac *= i
    print (f"numero actual {n}")

print (f"factorial de {n} es {fac}")