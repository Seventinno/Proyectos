# codigo para realizar una consola de turno
from Decoradores import numeros

ticketF = numeros()
ticketC = numeros()
ticketP = numeros()
print('Hola bienvenida a nuestra famacia')
salida = True

while salida:
    print('¿Que seccion te interesa? (F)Farmacia,(C)Cosmetica,(P)Perfumeria.')
    eleccion = input().upper()

    if eleccion == 'F':
        print(f'Te toca el ticket: {eleccion}-{next(ticketF)}')

    elif eleccion == 'C':
        print(f'Te toca el ticket: {eleccion}-{next(ticketC)}')

    elif eleccion == 'P':
        print(f'Te toca el ticket: {eleccion}-{next(ticketP)}')

    opcion = input('¿Deseas salir?: S/N').upper()
    if opcion == 'S':
        salida = False

