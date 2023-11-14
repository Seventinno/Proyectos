# Codigo que emula un recetario
import os
import shutil
from os import system
from pathlib import Path
from shutil import rmtree

menu = 0
mi_ruta = Path('C:\\Users\\jvetancourt\\Desktop\\Recetas')
finalizar_programa = False


'''def bienvenida(ruta):
    conteo = 0
    nombre = input('Ingresa tu nombre: ')
    system('cls')
    print(f'Hola {nombre}! Bienvenido a nuestro recetario')
    print(f'La direccion del recetario es {ruta}')
    for txt in Path(ruta).glob('**/*.txt'):
        conteo += 1
    print(f'Actualmente hay {conteo} recetas')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion')
        print(
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoria
        [4] - Eliminar receta
        [5] - Eliminar caategoria
        [6] - Salir del programa
        )
        eleccion_menu = input()
    return int(eleccion_menu)
'''
def mostrar_categorias(ruta):
    print('Categorias')
    categorias = Path(ruta)
    lista_categorias = []
    conteo = 1
    for carpetas in categorias.iterdir():
        print(f'{conteo} {carpetas.name}')
        conteo += 1
        lista_categorias.append(carpetas)
    return lista_categorias

def elegir_categorias(lista):
    eleccion_correcta = ''
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta = input('\nElige una categoria: ')

    return lista[int(eleccion_correcta)-1]

def mostrar_receta(ruta):
    print('Recetas')
    nueva_ruta = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in Path(nueva_ruta).glob('*.txt'):
        lista_recetas.append(receta)
        if len(lista_recetas) < 1:
            print('No hay recetas en esta carpeta')
        else:
            print(f'{contador} {receta.stem}')
            contador += 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = ''
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('Elige una receta: ')
    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print('Ingresa el nombre de tu receta')
        nombre_receta = input() + '.txt'
        print('Ingresa el contenido de la receta')
        contenido = input()
        ruta_nueva = Path(ruta,nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Esa receta ya existe')
            existe = True


def crear_categoria(ruta):
    existe = False
    while not existe:
        print('Igresa el nombre de la nueva categoria')
        nombre_categoria = input()
        ruta_nueva = Path(ruta,nombre_categoria )
        if not os.path.exists(ruta_nueva):
            os.mkdir(ruta_nueva)
            print(f'La categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Esa categoria ya existe')
            existe = True

def eliminar_receta(ruta):
        Path(ruta).unlink()
        print(f'La receta {ruta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    shutil.rmtree(categoria)
    print(f'La categoria {categoria.name} ha sido removida con exito')

def eleccion():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione V para volver al menu: ')

def bienvenida(ruta):
    conteo = 0
    nombre = input('Ingresa tu nombre: ')
    system('cls')
    print(f'Hola {nombre}! Bienvenido a nuestro recetario')
    print(f'La direccion del recetario es {ruta}')
    for txt in Path(ruta).glob('**/*.txt'):
        conteo += 1
    print(f'Actualmente hay {conteo} recetas')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion')
        print('''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoria
        [4] - Eliminar receta
        [5] - Eliminar caategoria
        [6] - Salir del programa
        ''')
        eleccion_menu = input()
    return int(eleccion_menu)

while not finalizar_programa:
    menu = bienvenida(mi_ruta)

    if menu == 1:
        mis_categorías = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorías)
        mis_recetas = mostrar_receta(mi_categoria)
        if len(mis_recetas) < 1:
            print('No hay recetas en esta categoria')
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        eleccion()


    elif menu == 2:
        mis_categorías = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorías)
        crear_receta(mi_categoria)
        eleccion()

    elif menu == 3:
        crear_categoria(mi_ruta)
        eleccion()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_receta(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        eleccion()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        eleccion()

    elif menu == 6:
        print('Gracias, esperamos verte de nuevo')
        finalizar_programa = True






