import re
from urllib.parse import urlparse

#extractor de url
def extraer_url(texto: str):
    #detector de url
    patron = re.compile(
        r'(https?://[^\s]+|www\.[^\s]+)'
    )

    urls = patron.findall(texto)
    resultados = []

    for url in urls:
        #protocolo
        url_parseable = url if url.startswith('http') else 'http://' + url
        partes = urlparse(url_parseable)

        resultado = {
            "url": url,
            "protocolo": partes.scheme if partes.scheme else "",
            "dominio": partes.netloc,
            "ruta": partes.path if partes.path else ""
        }
        resultados.append(resultado)

    return resultados

#programa principal
texto_usuario = input("ingresa un texto con url: ")

urls_encontradas = extraer_url(texto_usuario)

#muestra de resultados
for i, u in enumerate(urls_encontradas, 1):
    print(f"\nURL {i}: {u['url']}")
    print(f"  Protocolo: {u['protocolo']}")
    print(f"  Dominio: {u['dominio']}")
    if u['ruta']:
       print(f"  Ruta: {u['ruta']}")