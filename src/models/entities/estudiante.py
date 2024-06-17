from .userComponent import UserComponent
class estudiante(UserComponent):

    def __init__(self,carne,nombre,apellido,apellido2,correo,celular,idSede,segundoNombre=None):
        self.carne=carne
        self.nombre=nombre
        self.segundoNombre=segundoNombre
        self.apellido=apellido
        self.apellido2=apellido2
        self.correo=correo
        self.celular=celular
        self.idSede=idSede
       
        
        
    def to_JSON(self):
        return{
            'Carnet': self.carne,
            'Nombre': self.nombre,
            'Segundo Nombre':self.segundoNombre,
            'Apellido':self.apellido,
            'Segundo Apellido':self.apellido2,
            'Correo':self.correo,
            'Cel':self.celular,
            'Sede':self.idSede
        }