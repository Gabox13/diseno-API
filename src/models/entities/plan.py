class plan():

    def __init__(self,idPlan,equipo,semestre,año):
        self.idPlan=idPlan
        self.equipo=equipo
        self.semestre=semestre
        self.año=año
        
        
    def to_JSON(self):
        return{
            'idPlan': self.idPlan,
            'equipo': self.equipo,
            'semestre':self.semestre,
            'año':self.año
        }