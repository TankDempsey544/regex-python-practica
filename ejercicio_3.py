import re

#criterios del programa
def validar(contraseña: str):
    errores = []

    if len(contraseña) < 8:
       errores.append("debe tener ocho caracteres")
    if not re.search(r"[a-z]", contraseña):
        errores.append("debe incluir alguna minuscula")
    if not re.search(r"[A-Z]", contraseña):
        errores.append("debe incluir alguna mayuscula")
    if not re.search(r"[0-9]", contraseña):
        errores.append("debe incluir numeros")
    if not re.search(r"[@$#%&!*_]", contraseña):
        errores.append("debe tener un caracter especial")
    
    if errores:
        return False, errores
    else:
        return True, ["contraseña valida"]

#programa principal
contraseña_usuario = input("ingresa tu contraseña")

valida, mensajes = validar(contraseña_usuario)

for m in mensajes: 
    print(m)