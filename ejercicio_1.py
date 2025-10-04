import re

email_regex = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Zaa-z0-9.-]+\.[A-Za-z]{2,}$')

#es para devolver el true si el correo si es valido
def correo_valido(email: str) -> bool:
    if not email or '@' not in email:
        return False
    return bool(email_regex.match(email))

#programa para ingresar los correos

correo = input("ingresa un correo")

if correo_valido(correo):
    print("correo valido")
else:
    print("correo no valido")