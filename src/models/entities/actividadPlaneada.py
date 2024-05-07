from .actividad import actividad

class ActividadaPlaneada(actividad):

    def to_JSON(self):
        return {'valoresGenerales':super().to_JSON()}
    