class Recordatorio:
    def __init__(self,idFecRec,idActividad,fechaR):
        self.idFecRec=idFecRec
        self.idActividad=idActividad
        self.fechaR=fechaR
    def to_JSON(self):
        return {
            'idFecRec':self.idFecRec,
            'idActividad':self.idActividad,
            'fechaR':self.fechaR
        }
        