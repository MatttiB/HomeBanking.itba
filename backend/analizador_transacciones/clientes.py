from abc import ABC
from abc import abstractclassmethod

SIN_LIMITE = ""
CUENTAS_BANCARIAS = {
    "CLASSIC": {"LIMITE_EXTRACCION_DIARIO": 10000,
                "LIMITE_TRANSFERENCIA_RECIBIDA": 150000,
                "MONTO": 0,
                "COSTO_TRANSFERENCIA": 0.01,
                "SALDO_DESCUBIERTO_DISPONIBLE": 0
    },
    "GOLD": {"LIMITE_EXTRACCION_DIARIO": 20000,
                "LIMITE_TRANSFERENCIA_RECIBIDA": 500000,
                "MONTO": 0,
                "COSTO_TRANSFERENCIA": 0.005,
                "SALDO_DESCUBIERTO_DISPONIBLE": 10000
    },
    "BLACK": {"LIMITE_EXTRACCION_DIARIO": 100000,
                "LIMITE_TRANSFERENCIA_RECIBIDA": SIN_LIMITE,
                "MONTO": 0,
                "COSTO_TRANSFERENCIA": 0,
                "SALDO_DESCUBIERTO_DISPONIBLE": 10000
    }
}

class Cliente(ABC):
    def __init__(self, kwargs, tipo_cliente):
        self.__nombre = kwargs.get('nombre') + " " + kwargs.get('apellido')
        self.__numero = kwargs.get('numero')
        self.__dni = kwargs.get('dni')
        
        self.__direccion = Direccion(kwargs.get('direccion'))
        self.__cuenta = Cuenta(CUENTAS_BANCARIAS.get(tipo_cliente))
        
    def obtener_nombre(self):
        return self.__nombre

    def obtener_numero(self):
        return self.__numero

    def obtener_dni(self):
        return self.__dni

    def obtener_direccion(self):
        return self.__direccion
    
    def obtener_cuenta(self):
        return self.__cuenta

    @abstractclassmethod
    def puede_crear_chequera(self):
        pass
    
    @abstractclassmethod
    def puede_comprar_dolares(self):
        pass
    
    @abstractclassmethod
    def puede_crear_tarjeta_credito(self):
        pass
    
class Classic(Cliente):
    def __init__(self, kwargs, tipo_cliente):
        
        super().__init__(kwargs, tipo_cliente)

        self.__cant_max_tarjeta = 0
        self.__cant_max_chequera = 0
        self.__cant_tarjeta = 0        
        
    def puede_crear_chequera(self):
        return False
    
    def puede_comprar_dolares(self):
        return False
    
    def puede_crear_tarjeta_credito(self):
        return False
    
class Gold(Cliente):
    def __init__(self, kwargs, tipo_cliente):
        
        super().__init__(kwargs, tipo_cliente)
        
        self.__cant_max_tarjeta = 1
        self.__cant_max_chequera = 1

    def getCantTarjetas(self):
        return self.__cant_max_tarjeta

    def getCantChequera(self):
        return self.__cant_max_chequera

    def puede_crear_chequera(self):
        return True
    
    def puede_comprar_dolares(self):
        return True
    
    def puede_crear_tarjeta_credito(self):
        return True
    
class Black(Cliente):
    def __init__(self, kwargs, tipo_cliente):
        
        super().__init__(kwargs, tipo_cliente)
        
        self.__cant_max_tarjeta = 5
        self.__cant_max_chequera = 2
        
    def getCantTarjetas(self):
        return self.__cant_max_tarjeta

    def getCantChequera(self):
        return self.__cant_max_chequera
        
    def puede_crear_chequera(self):
        return True
    
    def puede_comprar_dolares(self):
        return True
    
    def puede_crear_tarjeta_credito(self):
        return True
          
class Direccion:

    def __init__(self, kwargs):

        self.calle = kwargs.get('calle')
        self.numero = kwargs.get('numero')
        self.ciudad = kwargs.get('ciudad')
        self.provincia = kwargs.get('provincia')
        self.pais = kwargs.get('pais')

    def __str__(self):

        return '{}({})'.format(self.calle,self.numero, self.ciudad,  self.provincia, self.pais)
    
class Cuenta:

    def __init__(self, kwargs):

        self.__limite_extraccion_diario = kwargs.get('LIMITE_EXTRACCION_DIARIO')
        self.__limite_transferencia_recibida = kwargs.get('LIMITE_TRANSFERENCIA_RECIBIDA')
        self.__monto = kwargs.get('MONTO')
        self.__costo_transferencia = kwargs.get("COSTO_TRANSFERENCIA")
        self.__saldo_descubierto_disponible = kwargs.get('SALDO_DESCUBIERTO_DISPONIBLE')

    def obtener_limite_extraccion(self):
        return self.__limite_extraccion_diario

    def obtener_limite_transferencia_recibida(self):
        return self.__limite_transferencia_recibida

    def obtener_monto(self):
        return self.__monto

    def cambiar_monto(self, nuevo_monto):
        self.__monto = nuevo_monto

    def obtener_costo_transferecia(self):
        return self.__costo_transferencia

    def obtener_saldo_descubierto_disponible(self):
        return self.__saldo_descubierto_disponible

    def cambiar_saldo_descubierto(self, nuevo_saldo_descubieto):
        self.__saldo_descubierto_disponible = nuevo_saldo_descubieto

    def __str__(self):
        return '{}'.format(self.__saldo_descubierto_disponible)
