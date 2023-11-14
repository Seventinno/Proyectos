import math
import re
import time
import zipfile
import shutil
import os
from datetime import datetime
from datetime import date
from pathlib import Path

inicio =time.time()
ruta = 'C:\\Users\\jvetancourt\\Desktop\\Python\\Day 9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
nros_encontrados = []
archivos_encontrados = []

# Funcion para obtener la fecha con el formato dia/mes/año


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
              "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    mensaje = f'{day}/{month}/{year}'

    return mensaje

# Funcion para busqueda de numeros de serie
def buscar_numero(archivo,patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        ''

def crear_listas():
    for carpetas, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpetas,a),mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda:{current_date_format()}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice + 1
    print('\n')
    print(f'Numeros encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('_' * 50)

crear_listas()
mostrar_todo()






