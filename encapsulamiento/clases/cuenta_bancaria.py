class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular # doble guion bajo hace propiedad privada
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito de ${cantidad} exitoso!")
        else:
            print('No se puede depositar un saldo negativo!')
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitosamente")
        else:
            print('Fondos insuficientes o cantidad invalida')

    def get_saldo(self):
        return f"El saldo actual de la cuenta es ${self.__saldo}"