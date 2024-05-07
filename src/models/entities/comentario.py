class comentario():

    def __init__(self,idComentario,idProfesor,comentario,fechaEmision,nombreCompleto,foto,respuestas):
        self.idComentario=idComentario
        self.idProfesor=idProfesor
        self.comentario=comentario
        self.fechaEmision=fechaEmision
        self.nombreCompleto=nombreCompleto
        self.foto=foto
        self.respuestas =respuestas


    
        
        
    def to_JSON(self):
        return{
            'idComentario': self.idComentario,
            'idProfesor': self.idProfesor,
            'comentario': self.comentario,
            'fechaEmision': self.fechaEmision,
            'nombreCompleto':self.nombreCompleto,
            'foto':self.foto,
            'respuestas':self.respuestas 
            
        }