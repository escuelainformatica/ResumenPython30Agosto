# modelo.

class Cliente():
    rut:str=""
    nombre:str=""
    edad:int=0

    # el constructor
    def __init__(self,**kwargs) -> None:
        if len(kwargs)>=3:
            self.rut=kwargs['rut']
            self.nombre=kwargs['nombre']
            self.edad=kwargs['edad']


