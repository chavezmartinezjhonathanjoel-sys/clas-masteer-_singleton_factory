from abc import ABC, abstractmethod


class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        raise NotImplementedError()


class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        return f"Pagando ${monto} con tarjeta"


class PagoPaypal(MetodoPago):
    def pagar(self, monto):
        return f"Pagando ${monto} con PayPal"


class PagoTransferencia(MetodoPago):
    def pagar(self, monto):
        return f"Pagando ${monto} por transferencia bancaria"


class FabricaPago:
    @staticmethod
    def crear_pago(tipo):
        if tipo == "tarjeta":
            return PagoTarjeta()
        elif tipo == "paypal":
            return PagoPaypal()
        elif tipo == "transferencia":
            return PagoTransferencia()
        else:
            raise ValueError("Tipo de pago no soportado")
