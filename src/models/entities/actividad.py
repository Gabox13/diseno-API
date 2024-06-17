class actividad:
    def __init__(self,idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios=None,responsables=None):
        self.idActividad=idActividad
        self.nombre=nombre
        self.semana=semana
        self.direccion=direccion
        self.tipo=tipo
        self.modalidad=modalidad
        self.fechaPublicacion=fechaPublicacion
        self.fechaRealizacion=fechaRealizacion
        self.afiche=afiche
        self.estado=estado
        self.comentarios=comentarios
        self.fechaRecordatorio=fechaRecordatorio
        self.responsables=responsables
    def accept(self,visitor):
        visitor.visit(self)

    def to_JSON(self):
        return{
            'idActividad':self.idActividad,
            'nombre':self.nombre,
            'semana':self.semana,
            'direccion':self.direccion,
            'tipo':self.tipo,
            'modalidad':self.modalidad,
            'fechaPublicacion':self.fechaPublicacion,
            'fechaRealizacion':self.fechaRealizacion,
            'afiche':self.afiche,
            'estado':self.estado,
            'comentarios':self.comentarios,
            'fechaRecordatorio':self.fechaRecordatorio,
            'responsables':self.responsables
        }
