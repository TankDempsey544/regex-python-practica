# LENGUAJES-Y-AUTOMATAS
Repositorio De Trabajos Para La Materia de LENGUAJES Y AUTOMATAS

1. Validador de Correos Electrónicos

Descripción:
Este programa valida si una cadena de texto es un correo electrónico válido con formato usuario@dominio.com.

Criterios de validación:

Debe contener el símbolo @.

Debe tener texto antes y después de @.

Debe terminar con un dominio válido (.com, .mx, .org, etc.).

Ejemplo de uso:

usuario = input("Ingresa tu correo: ")
if validar_correo(usuario):
    print("Correo válido")
else:
    print("Correo inválido")


Casos de prueba:

"usuario@ejemplo.com" → Válido

"nombre.apellido@dominio.mx" → Válido

"usuarioejemplo.com" → Inválido

"@ejemplo.com" → Inválido

2. Extractor de Números de Teléfono

Descripción:
Este programa busca números de teléfono en un texto considerando formatos mexicanos de 10 dígitos.

Formatos soportados:

6461234567

646-123-4567

646 123 4567

(646) 123-4567

Ejemplo de uso:

texto_usuario = input("Ingresa un texto con teléfono: ")
telefonos = extraer(texto_usuario)
print("Teléfonos encontrados:", telefonos)


Salida esperada:

Teléfonos encontrados: ['646-123-4567', '(664) 987-6543', '5551234567']

3. Validador de Contraseñas Seguras

Descripción:
Valida si una contraseña cumple con criterios de seguridad básicos.

Criterios:

Mínimo 8 caracteres.

Al menos una letra mayúscula.

Al menos una letra minúscula.

Al menos un número.

Al menos un carácter especial (@$!%*?&#).

Ejemplo de uso:

contraseña_usuario = input("Ingresa tu contraseña: ")
valida, mensajes = validar(contraseña_usuario)
for m in mensajes:
    print(m)


Casos de prueba:

"Segura123!" → Válida

"contrasena" → Inválida

"MAYUSCULA123!" → Inválida

"P@ssw0rd" → Válida

4. Extractor de URLs y Dominios

Descripción:
Detecta URLs en un texto y separa protocolo, dominio y ruta.

Formatos soportados:

http://ejemplo.com

https://www.ejemplo.com/pagina

www.ejemplo.com

Ejemplo de uso:

texto_usuario = input("Ingresa un texto con URL: ")
urls_encontradas = extraer_url(texto_usuario)
for i, u in enumerate(urls_encontradas, 1):
    print(f"\nURL {i}: {u['url']}")
    print(f"  Protocolo: {u['protocolo']}")
    print(f"  Dominio: {u['dominio']}")
    if u['ruta']:
        print(f"  Ruta: {u['ruta']}")


Salida esperada:

URL 1: https://www.google.com
  Protocolo: https
  Dominio: www.google.com

URL 2: http://github.com/usuario
  Protocolo: http
  Dominio: github.com
  Ruta: /usuario

5. Analizador de Fechas y Formateador

Descripción:
Extrae fechas de un texto en distintos formatos y las convierte al formato YYYY-MM-DD.

Formatos detectados:

DD/MM/YYYY

YYYY-MM-DD

DD-MMM-YYYY

Mes DD, YYYY (soporta meses en español)

Ejemplo de uso:

texto = input("Ingresa un texto con fechas: ")
fechas = analizar_fechas(texto)
for original, estandar in fechas:
    print(f"Formato original: {original} → Estándar: {estandar}")


Ejemplo de entrada:

"La reunión es el 15/03/2024. El proyecto inicia el 2024-04-20 y termina en Junio 30, 2024. La entrega final es 01-Jul-2024."


Salida esperada:

Formato original: 15/03/2024 → Estándar: 2024-03-15
Formato original: 2024-04-20 → Estándar: 2024-04-20
Formato original: Junio 30, 2024 → Estándar: 2024-06-30
Formato original: 01-Jul-2024 → Estándar: 2024-07-01

Tecnologías utilizadas

Python 3.10

Módulo re (expresiones regulares)

Módulo urllib.parse (para URLs)