class respuesta():

    def __init__(self,idComentario,idProfesor,respuesta,fechaEmision,nombreCompleto,foto):
        self.idComentario=idComentario
        self.idProfesor=idProfesor
        self.respuesta=respuesta
        self.fechaEmision=fechaEmision
        self.nombreCompleto=nombreCompleto
        self.foto=foto

    
        
        
    def to_JSON(self):
        return{
            'idComentario': self.idComentario,
            'idProfesor': self.idProfesor,
            'respuesta': self.respuesta,
            'fechaEmision': self.fechaEmision,
            'nombreCompleto':self.nombreCompleto,
            'foto':self.foto
            
        }