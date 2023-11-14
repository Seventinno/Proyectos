def cambiar_letras(tipo):
    def mayusculas(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayusculas

    elif tipo == 'min':
        return minusculas

operacion = cambiar_letras('may')
operacion('palabra')


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


#el arroba se utiliza para envolver una funcion en otra y asi decorarla
@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


def minusculas(texto):
    print(texto.lower())

mayusculas('celeste')

prueba = decorar_saludo(minusculas)

prueba('MARIA')

# Funcion para el proyecto 8
def numeros():
    num = 1
    while True:
        yield num
        num += 1

