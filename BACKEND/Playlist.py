class Play:
    
    def __init__(self,usuario,id):
        self.usuario = usuario
        self.id = id
        
    
    #METODOS GETTER
    def getUsuario(self):
        return self.usuario
    
    def getID(self):
        return self.id
    
    
    #METODOS SETTER

    def setUsuario(self, usuario):
        self.usuario = usuario
    
    def setID(self, id):
        self.id = id