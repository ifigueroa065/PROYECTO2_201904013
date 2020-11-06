class Comentario:
    
    def __init__(self,comentario,usuario,id):
        self.comentario = comentario
        self.usuario = usuario
        self.id = id
        
    
    #METODOS GETTER
    def getComentario(self):
        return self.comentario

    def getUsuario(self):
        return self.usuario
    
    def getID(self):
        return self.id
    
    
    #METODOS SETTER

    def setComentario(self,comentario):
        self.comentario = Comentario

    def setUsuario(self, usuario):
        self.usuario = usuario
    
    def setID(self, id):
        self.id = id

    