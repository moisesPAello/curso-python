# Declaracion de valores
#int / Numero Entero
numero = 10

#float / Decimal
float = 13.14

#Character / Caracter
character = '$'

#String / cadena de caracteres
cadena = "hola como estas yo muy bien y tu"

#Booleano / true o false
booleano = True
booleano2= False
# Binario 01

# Mal uso de indetificadores
# Contraintuitivo
palabra = 123
#X no nos dice nada sobre que representa la variable
x = "hola mundo"
#No abreviaciones. 0 motivos para abreviar
num = 10


# Mostrar los resultados
print(f"Esto es un entero: {numero}")
print(f"Esto es un decimal: {float}")
print(f"Esto es un caracter: {character}")
print(f"Esto es una cadena de caracteres (string): {cadena}")

# Reasignacion de valor
numero = 13345
numero = 1234
numero = 15
print(f"Nuevo valor de la variable numero: {numero}")


cuenta_bancaria = 20000.99
retiro = 100
saldo_despues_retiro = cuenta_bancaria - retiro

print(f"Saldo en la cuenta: {cuenta_bancaria}")
print(f"Saldo despues del retiro: {saldo_despues_retiro}")

#Cambiando el valor de la variable
cuenta_bancaria = saldo_despues_retiro
print(f"Saldo acutal: {cuenta_bancaria}")