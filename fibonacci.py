#Vicente Y. Lopez V. - 240010
#Genera los primeros N términos de la secuencia de Fibonacci.

n = int(input("Ingresa un numero: "))
a = 0
b = 1
for i in range (n):
   c = a + b
   a = b
   b = c
   print(f"numero actual {c}")
    
print(f"Los primeros {n} términos de la secuencia de Fibonacci son: {c}")
 