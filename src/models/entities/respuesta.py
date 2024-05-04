class respuesta():

    def __init__(self,idComentario,idProfesor,respuesta,fechaEmision):
        self.idComentario=idComentario
        self.idProfesor=idProfesor
        self.respuesta=respuesta
        self.fechaEmision=fechaEmision

    
        
        
    def to_JSON(self):
        return{
            'idComentario': self.idComentario,
            'idProfesor': self.idProfesor,
            'respuesta': self.respuesta,
            'fechaEmision': self.fechaEmision,
            
        }