# Piramide de asteriscos
h=int(input("Ingresa la altura de la piramide: "))
for i in range(1,h+1):
    huecos=h-i          
    asteriscos=2*i-1        
    print(" " * huecos + "*" * asteriscos)
