class TarjetaCredito:
    tarjetas_creadas = []  # BONUS: lista de todas las tarjetas

    def __init__(self, saldo_pagar=0, limite_credito=100000, intereses=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas_creadas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar:.0f}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("\n=== Todas las Tarjetas ===")
        for idx, tarjeta in enumerate(cls.tarjetas_creadas, start=1):
            print(f"Tarjeta {idx}: Saldo: ${tarjeta.saldo_pagar:.0f}, Límite: ${tarjeta.limite_credito}, Interés: {tarjeta.intereses}")
        print("==========================\n")


# Tarjeta 1 → 2 compras, 1 pago, cobra interés, muestra info (encadenado)
tarjeta1 = TarjetaCredito(limite_credito=150000, intereses=0.03)
tarjeta1.compra(40000).compra(30000).pago(20000).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 2 → 3 compras, 2 pagos, cobra interés, muestra info (encadenado)
tarjeta2 = TarjetaCredito(limite_credito=100000, intereses=0.025)
tarjeta2.compra(20000).compra(15000).compra(30000).pago(10000).pago(5000).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 3 → 5 compras que exceden el límite, mostrar info (encadenado)
tarjeta3 = TarjetaCredito(limite_credito=50000, intereses=0.02)
tarjeta3.compra(10000).compra(15000).compra(20000).compra(12000).compra(8000).mostrar_info_tarjeta()

# BONUS: mostrar todas las tarjetas creadas
TarjetaCredito.mostrar_todas_las_tarjetas()
