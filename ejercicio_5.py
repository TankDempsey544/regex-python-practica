import re

texto = input("ingresa un texto con una fecha: ")

#buscador de fechas en tres formatos
fechas = re.findall(r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}|\d{2}-[A-Za-z]{3}-\d{4}', texto)

#meses abreviados
meses = {
    "ene": "01", "enero": "01",
    "Feb": "02", "Febrero": "02",
    "Mar": "03", "Marzo": "03",
    "Abr": "04", "Abril": "04",
    "May": "05", "Mayo": "05",
    "Jun": "06", "Junio": "06",
    "Jul": "07", "Julio": "07",
    "Ago": "08", "Agosto": "08",
    "Sep": "09", "Septiembre": "09",
    "Oct": "10", "Octubre": "10",
    "Nov": "11", "Noviembre": "11",
    "Dic": "12", "Diciembre": "12"
}

#regex para los formatos
fechas = re.findall(
    r'\d{2}/\d{2}/\d{4}|'
    r'\d{2}-\d{2}-\d{2}|'
    r'\d{2}-[A-Za-z]{3}-\d{4}|'
    r'(?:' + '|'.join(meses.keys()) + r') \d{1,2}, \d{4}', texto
)

for f in fechas:
    if "/" in f: 
        d, m, y = f.split("/")
        print("formato original:", f, "estandar:", y + "-" + m + "-" + d)
    elif "-" in f:
        partes = f.split("-")
        if len(partes[0]) == 4:
            print("formato original:", f, "estandar:", f)
        else:
            d, mes, y = partes
            m = meses.get(mes.capitalize(), "00")
            print("Formato original:", f, "→ Estándar:", y + "-" + m + "-" + d)
    elif "," in f:
        for mes_nombre in meses:
            if f.startswith(mes_nombre):
                mes_num = meses[mes_nombre]
                resto = f.replace(mes_nombre + " ", "")
                dia, ano = resto.replace(",", "").split()
                print("formato original:", f, "estandar:", ano + "-" + mes_num + "-" + dia.zfill(2))
