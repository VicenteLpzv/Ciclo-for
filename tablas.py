#Vicente Y. Lopez V. - 240010
#tablas de multiplicar

n = int(input("Ingresa un numero del 1 al 10: "))

if n >0 and n<=10:
    for i in range(1 ,11, 1): # i va de uno en uno
        r = n * i #aqui será n x i, y como y va de uno en uno, ira del 1 hasta el 10
        print (f"{n} x {i} = {r}" )
else:
    print ("no valido")

