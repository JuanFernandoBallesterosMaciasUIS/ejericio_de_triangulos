# 1. Dados tres números a, b y c, verificar si puede formar los lados de un triangulo.

print("-------------------------------------------------")
print("-----------VERIFICACIÓN-DE-TRIANGULO-------------")
print("-------------------------------------------------")
print("")

#input
a = int(input("Digite el primer lado del triangulo: "))
b = int(input("Digite el segudno lado del triangulo: "))
c = int(input("Digite el tercer lado del triangulo: "))

#proceso y salida

if (a+b > c):
    print("El triangulo se pudo formar")
elif (b+c > a):
    print("El triangulo se pudo formar")
elif (c+a > b):
    print("El triangulo se pudo formar")
else:
    print("El triangulo no se puede formar")