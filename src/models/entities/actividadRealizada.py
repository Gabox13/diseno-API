from .actividad import actividad

class ActividadRealizada(actividad):
    def __init__(self, idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables,fotos):
        super().__init__(idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables)
        self.fotos=fotos

    def to_JSON(self):
       valores=super().to_JSON()
       return{
           'valoresGenerales': valores,
            'fotos':self.fotos

       }
