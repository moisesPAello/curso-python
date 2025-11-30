#numero = 123
numero = -3
if numero == 123:  #false o true
    print(f"numero es igual a 123")
else:
    print("numero no es igual 123")

print("Estoy fuera del IF")

if numero < 0:
    print("numero es negativo")

if numero > 0:
    print("numero es positivo")

# IF espera un booleano
if True:
    print()

if False:
    print()

#elseif
calificacion = 70

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("Repobrobado")


# Operadores condicionales
# <, >, ==, != y se pueden combinar <=, >=.

# AND, OR, XOR
#and
print(True and True)

#or
print(True or False)
print(True or True)

#xor
print(True != False)


#Rangos
edad = 18

if edad >= 18 and edad < 90:
    print("Puedes votar!")
else:
    print("No puedes votar")