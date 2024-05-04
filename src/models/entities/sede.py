class sede():

    def __init__(self,idSede,nombre):
        self.idSede=idSede
        self.nombre=nombre
        
        
    def to_JSON(self):
        return{
            'idSede': self.idSede,
            'nombre': self.nombre,
            
        }
