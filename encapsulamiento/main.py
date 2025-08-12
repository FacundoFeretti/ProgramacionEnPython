from encapsulamiento.clases.cuenta_bancaria import CuentaBancaria


cuenta = CuentaBancaria('Facundo Feretti', 1000)

print(cuenta.get_saldo())

cuenta.depositar(-650)
print(cuenta.get_saldo())

cuenta.retirar(1650)
print(cuenta.get_saldo())
