class profe():

    def __init__(self,correo,nombre, activo, telefono, celular, foto,idSede):
        self.correo=correo
        self.nombre=nombre
        self.activo=activo
        self.telefono=telefono
        self.celular=celular
        self.foto=foto
        self.idSede=idSede
        
    def to_JSON(self):
        return{
            'correo': self.correo,
            'nombre': self.nombre,
            'activo': self.activo,
            'telefono':self.telefono,
            'celular':self.celular,
            'foto':self.foto,
            'idSede':self.idSede
        }

