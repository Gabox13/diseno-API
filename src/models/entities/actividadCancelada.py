from .actividad import actividad

class ActividadCancelada(actividad):
    def __init__(self, idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables,descripcion_cancelacion,fecha_cancelacion):
        super().__init__(idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables)
        self.descripcion_cancelacion = descripcion_cancelacion
        self.fecha_cancelacion =fecha_cancelacion
    def to_JSON(self):
       valores=super().to_JSON()
       return{
           'valoresGenerales': valores,
           'descripcionCancelacion':self.descripcion_cancelacion,
           'fechaCancelacion':self.fecha_cancelacion
       }
