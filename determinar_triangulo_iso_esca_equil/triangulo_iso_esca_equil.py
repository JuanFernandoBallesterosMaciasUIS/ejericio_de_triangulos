# 2. Determinar si un triangulo es isoceles, escaleno, o equilatero.

print("-------------------------------------------------")
print("-----------VERIFICACIÓN-DE-TRIANGULO-------------")
print("-------------------------------------------------")
print("")

#input
a = int(input("Digite el primer lado del triangulo: "))
b = int(input("Digite el segudno lado del triangulo: "))
c = int(input("Digite el tercer lado del triangulo: "))

#proceso y salida

bandera = True

if (a+b > c):
    print("El triangulo se pudo formar")
    bandera = True
elif (b+c > a):
    print("El triangulo se pudo formar")
    bandera = True
elif (c+a > b):
    print("El triangulo se pudo formar")
    bandera = True
else:
    print("El triangulo no se puede formar")
    bandera = False
    
if bandera:
    if a == b == c:
        print("El triangulo es equilatero")
    elif a != b != c != a:
        print("El triangulo es escaleno")
    elif a == b or b == c or a == c:
        print("El triangulo es isoceles")