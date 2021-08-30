class MaterialImpreso():
    titulo:str=""
    cant_paginas:int=0

    def mostrar(self):
        print("Material impreso:")
        print(self.titulo)
        print(self.cant_paginas)


class Libro(MaterialImpreso):
    titulo:str=""   # se sobreescribe la herencia
    autor:str=""

    def mostrar(self): # sobreescribir la funcion
        super().mostrar() # llamar al padre
        print(self.autor)

class Revista(MaterialImpreso):
    pass

class Comic(MaterialImpreso):
    pass


