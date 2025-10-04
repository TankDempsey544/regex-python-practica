import re

#aqui extraemos los numeros en distintos formatos
def extraer(texto: str):
    patron = re.compile(r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}')
    telefonos = patron.findall(texto)
    return telefonos

#programa para insertar los numeros
texto_usuario = input("ingresa para buscar un telefono")

telefono_encontrado = extraer(texto_usuario)

if telefono_encontrado:
  print("telefono encontrado: ", telefono_encontrado)
else:
  print("no se encontro: ")