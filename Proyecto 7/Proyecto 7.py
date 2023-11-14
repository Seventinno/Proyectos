#Codigo que recrea una cuenta bancaria

class Persona():

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Bienvenido {self.nombre} {self.apellido}'

class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Bienvenido {self.nombre} {self.apellido}\n Balance de cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')


    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    print('Bienvenido, por favor ingresa tu nombre: ')
    nombre = input()
    print('Ingresa tu apellido: ')
    apellido = input()
    num_cuenta = input('Ingrese su numero de cuenta: ')
    cliente1 = Cliente(nombre, apellido,num_cuenta)

    return cliente1

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print('Elije: Depositar(D), Retirar(R), o Salir(S)')
        opcion = input().title()
        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto retiro: '))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)

    print('Gracias por operar en banco python')

inicio()


