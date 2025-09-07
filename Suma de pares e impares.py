# Suma de pares e impares
n=int(input("Ingresa un numero: "))
suma_pares = 0
suma_impares = 0
for i in range(1, n+1):
    if i%2==0:
        suma_pares =i+suma_pares
    else:
        suma_impares =i+suma_impares
print("La suma de los numeros pares es= ", suma_pares)
print("La suma de los numeros impares es= ", suma_impares)
