from .actividadRealizada import ActividadRealizada
from .actividadCancelada import ActividadCancelada
from .actividadPlaneada import ActividadaPlaneada


class ActividadFactory:
    @staticmethod
    def crear_actividad(idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios=None,responsables=None, fotos=None, descripcion_cancelacion=None, fecha_cancelacion=None):
        print(responsables)
        if estado == 'Realizada':
            actividad = ActividadRealizada(idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables, fotos)
        elif estado == 'Cancelada':
            actividad = ActividadCancelada(idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables, descripcion_cancelacion, fecha_cancelacion)
        else:
            actividad = ActividadaPlaneada( idActividad,nombre,semana,direccion,tipo,modalidad
                 ,fechaPublicacion,fechaRealizacion,afiche,estado,fechaRecordatorio,comentarios,responsables)
        print(actividad.to_JSON())
        return actividad.to_JSON()
