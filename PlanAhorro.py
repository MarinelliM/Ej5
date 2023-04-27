class PlanAhorro:
    __codigo_plan: int
    __modelo: str
    __version_vehiculo:str
    __valor_vehiculo: int
    __cant_cuotas_plan = 0
    __cant_cuotas_licitar = 0
    __valor_cuota:int
    
    def __init__(self, codigo_plan, modelo, version_vehiculo, valor_vehiculo) -> None:
        self.__codigo_plan = codigo_plan
        self.__modelo = modelo
        self.__version_vehiculo = version_vehiculo
        self.__valor_vehiculo = valor_vehiculo

    def importe_cuota(self):
        self.__valor_cuota = (self.__valor_vehiculo / self.__cant_cuotas_plan) + self.__valor_vehiculo * 0.10

    def getvalorcuota(self):
        return self.__valor_cuota
    
    def getcodigoplan(self):
        return self.__codigo_plan

    def mostrar(self):
        return print('Codigo del plan: {} modelo: {} version del vehiculo: {}' .format(self.__codigo_plan, self.__modelo, self.__version_vehiculo,))
    
    def mostrar2(self):
        return print('Codigo del plan: {} modelo: {} version del vehiculo: {} valor del vehiculo: {}' .format(self.__codigo_plan, self.__modelo, self.__version_vehiculo, self.__valor_vehiculo))
    
    def __str__(self) -> str:
        return '({},{},{},{},{},{},{})'.format(self.__codigo_plan, self.__modelo, self.__version_vehiculo, self.__valor_vehiculo, self.getcuotasplan(), self.getcuotaslicitar(), self.__valor_cuota)
    
    def setvalorvehiculo(self, valor: int):
        self.__valor_vehiculo = valor
        print('Valor actualizado del vehiculo: {}' .format(self.__valor_vehiculo))

    @classmethod
    def setcantidadcuotasplan(cls, valor: int):
        cls.__cant_cuotas_plan = valor

    @classmethod
    def setcantidadcuotaslicitar(cls, valor: int):
        cls.__cant_cuotas_licitar = valor

    @classmethod
    def getcuotasplan(cls):
        return cls.__cant_cuotas_plan
    
    @classmethod
    def getcuotaslicitar(cls):
        return cls.__cant_cuotas_licitar
    
    @classmethod
    def verPlanes(cls):
        print('Informacion del Plan')
        print('Cantidad de cuotas del plan: ' + str(cls.getcuotasplan()))
        print('Cantidad de cuotas que debe tener pagas para licitar el vehiculo: ' + str(cls.getcuotaslicitar()))
    
    def monto_para_licitar(self):
        return self.__cant_cuotas_licitar*self.importe_cuota()
