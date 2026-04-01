class CuentaBancaria:
    def __init__ (self, titular, saldo_inicial):
        self.titular = titular
        self.__historial = []
        self.__saldo = 0
        self.depositar(saldo_inicial)
    
    #geters


    def get_historial(self):
        return self.__historial
    def get_saldo(self):
        return self.__saldo
    
    #seters
    def set_historial(self, historial):
        self.__historial = historial

    def set_saldo(self, saldo):
        if saldo < 0:
            print("No se puede establecer saldo negativo")
            return
        self.__saldo = saldo


    #Funcionalidades

    def depositar(self, cantidad):
        if cantidad < 0:
            print("El valor a depositar no puede ser negativo")
            return

        self.__saldo += cantidad
        self.get_historial().append("Depósito: " + str(cantidad))
        print("Depósito exitoso. Saldo actual: " + str(self.get_saldo()))

    def retirar(self, cantidad):
        if cantidad < 0:
            print("El valor a retirar no puede ser negativo")
            return

        if cantidad > self.__saldo:
            print("Saldo insuficiente para retirar")
            return

        self.__saldo -= cantidad
        self.get_historial().append("Retiro: " + str(cantidad))
        print("Retiro exitoso. Saldo restante: " + str(self.get_saldo()))   

    def ver_saldo(self):
        print("Saldo actual: " + str(self.get_saldo()))

    def ver_historial(self):
        print("Historial de transacciones:")
        for transaccion in self.get_historial():
            print(transaccion)


def main():
    cuenta1 = CuentaBancaria("Juan Perez", 100000)
    print(f"Cuenta creada para: {cuenta1.titular} y su saldo inicial es: {cuenta1.get_saldo()}")
    cuenta1.depositar(50000)
    cuenta1.retirar(20000)
    cuenta1.ver_saldo()
    cuenta1.ver_historial()

main()