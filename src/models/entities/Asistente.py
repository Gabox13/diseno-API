class Asistente():

    def __init__(self,correo,contra,idSede):
        self.correo=correo
        self.contra=contra
        self.idSede=idSede

    def to_JSON(self):
        return{
            'correo': self.correo,
            'contra': self.contra,
            'idSede': self.idSede
        }