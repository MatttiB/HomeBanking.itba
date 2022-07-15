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
    def __init__(self, kwargs):
        self.__nombre = kwargs.get('nombre')
        self.__apellido = kwargs.get('apellido')
        self.__numero = kwargs.get('numero')
        self.__dni = kwargs.get('dni')
        
        self.__direccion = Direccion(kwargs.get('direccion'))
        
    def __str__(self):
        return '{} {} {} {}'.format(self.__nombre, self.__apellido, self.__numero, self.__dni)
        
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
    def __init__(self, kwargs):
        
        super().__init__(kwargs)
        
        self.__cuenta = Cuenta(CUENTAS_BANCARIAS.get("CLASSIC"))
        
    def puede_crear_chequera(self):
        return False
    
    def puede_comprar_dolares(self):
        return False
    
    def puede_crear_tarjeta_credito(self):
        return False
    
class Gold(Cliente):
    def __init__(self, kwargs):
        
        super().__init__(kwargs)
        
        self.__cant_max_tarjeta = 1
        self.__cant_max_chequera = 1
        
        self.__cuenta = Cuenta(CUENTAS_BANCARIAS.get("GOLD"))
        
    def puede_crear_chequera(self):
        return True
    
    def puede_comprar_dolares(self):
        return True
    
    def puede_crear_tarjeta_credito(self):
        return True
    
class Black(Cliente):
    def __init__(self, kwargs):
        
        super().__init__(kwargs)
        
        self.__cant_max_tarjeta = 5
        self.__cant_max_chequera = 2
        
        self.__cuenta = Cuenta(CUENTAS_BANCARIAS.get("BLACK"))
        
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

    def str(self):

        return '{}({})'.format(self.calle,self.numero, self.ciudad,  self.provincia, self.pais)
    
class Cuenta:

    def __init__(self, kwargs):

        self.limite_extraccion_diario = kwargs.get('LIMITE_EXTRACCION_DIARIO')
        self.limite_transferencia_recibida = kwargs.get('LIMITE_TRANSFERENCIA_RECIBIDA')
        self.monto = kwargs.get('MONTO')
        self.costo_transferencia = kwargs.get('COSTO_TRANFERENCIA')
        self.saldo_descubierto_disponible = kwargs.get('SALDO_DESCUBIERTO_DISPONIBLE')
