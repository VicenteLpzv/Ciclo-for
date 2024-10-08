#Vicente Y. Lopez V. - 240010
#Suma de los primeros N números naturales
n = int(input("Ingresa un numero positivo: "))
suma = 0
for n in range (0, n + 1):
    suma += n  #acumulador
    print(f"numero actual: {n}")
     

print(f"La suma de los primeros {n} numeros naturales es: {suma}")
     

print ("fin")
