class profeIntegrante():

    def __init__(self, correo,nombreCompleto,activo,telefono,celular,idSede,foto=None,contraseña=None,codigoSede=None,coordinador=None,idEquipo=None):

        self.correo = correo
        self.nombreCompleto = nombreCompleto
        self.activo = activo
        self.telefono = telefono
        self.celular = celular
        self.idSede = idSede
        self.foto = foto
        self.contraseña = contraseña
        self.codigoSede = codigoSede
        self.coordinador = coordinador
        self.idEquipo = idEquipo

    def to_JSON(self):
        return {
            "correo":self.correo,
            "nombreCompleto":self.nombreCompleto,
            "activo":self.activo,
            "telefono":self.telefono,
            "celular":self.celular,
            "idSede":self.idSede,
            "foto":self.foto,
            "contraseña":self.contraseña,
            "codigoSede":self.codigoSede,
            "coordinador":self.coordinador,
            "idEquipo":self.idEquipo

        }