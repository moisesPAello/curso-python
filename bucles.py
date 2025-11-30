# Estructuras de repeticion en Python
# for - definido (limite)
for i in range(1, 6):
    print("Interacion: ", i)

tabla = int(input("Ingrese el numero para generar tabla: "))
print(f"Tabla del {tabla}")
for i in range(1, 11):
    print(f"{i} x {tabla} = {tabla * i}")


# while - indefinido (condicion)
# Ejemplo capcha
respuesta = None
capcha = "8U&r"

print(f"Capcha: {capcha}")
while respuesta != capcha:
    print("Resuelve el capcha para continuar: ")
    respuesta = input()
    if respuesta != capcha:
        print("Error. Intentalo de nuevo")
    else:
        print("Correcto!")
print("Bienvenido!")
