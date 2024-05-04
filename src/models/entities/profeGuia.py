class profeGuia():

    def __init__(self, correo, nombre, telefono, celular, foto, nombreSede, contraseña, codigoSede):
        self.correo = correo
        self.nombre = nombre
        self.telefono = telefono
        self.celular = celular
        self.foto = foto
        self.nombreSede = nombreSede
        self.contraseña = contraseña
        self.codigoSede = codigoSede

    def to_JSON(self):
        return {
            'correo': self.correo,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'celular': self.celular,
            'foto': self.foto,
            'nombreSede': self.nombreSede,
            'contraseña': self.contraseña,
            'codigoSede': self.codigoSede

        }
