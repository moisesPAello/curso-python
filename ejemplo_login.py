# Credenciales
usuario = "Moises"
contraseña = "admin123"

usuario_input = None
contraseña_input = None

intentos = 3

while usuario_input != usuario:
    usuario_input = input("Ingrese usuario: ")
    if usuario_input.isdigit():
        print("Nombre de usuario no valido. Intentalo de nuevo")
    
    elif usuario_input != usuario:
        print("Incorrecto. Intentalo de nuevo.")

while contraseña_input != contraseña and intentos != 0:
    contraseña_input = input("Ingrese su contraseña: ")
    if contraseña_input == None:
        print("Debes ingresar al menos un caracter")
    
    elif contraseña_input != contraseña:
        intentos = intentos - 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos")
if intentos == 0:
    print("Has alcanzado el limite de intentos. Intentelo de nuevo mas tarde.")
else:
    print(f"¡Bienvenido {usuario}!")
