#2. Determinar si un triangulo es obtuso, recto o agudo.

print("----------------------------------------------------")
print("-----------TRIANGULO-OBTUSO-RECTO-O-AGUDO-----------")
print("----------------------------------------------------")

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
    
if(bandera):
    if c**2 < a**2 + b**2:
        print("El triangulo es agudo")
    elif c**2 == a**2 + b**2:
        print("El triangulo es recto")
    elif c**2 > a**2 + b**2:
        print("El triangulo es obtuso")
    else:
        print("El triangulo no tiene ninguno de estos nombres")