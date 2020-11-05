class Cancion:
    
    def __init__(self,nombre,artista,album,imagen,fecha,linkS,linkYT,identificador):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.fecha= fecha
        self.linkS = linkS
        self.linkYT = linkYT
        self.identificador=identificador
    
    #METODOS GETTER
    def getNombre(self):
        return self.nombre

    def getArtista(self):
        return self.artista
    
    def getAlbum(self):
        return self.album
    
    def getImagen(self):
        return self.imagen

    def getFecha(self):
        return self.fecha
    
    def getLinkS(self):
        return self.linkS
    
    def getLinkYT(self):
        return self.linkYT

    def getID(self):
        return self.identificador
    
    
    #METODOS SETTER

    def setNombre(self,nombre):
        self.nombre = nombre

    def setArtista(self, artista):
        self.artista = artista
    
    def setAlbum(self, album):
        self.album = album

    def setImagen(self,imagen):
        self.imagen = imagen
    
    def setFecha(self,fecha):
        self.fecha = fecha
     
    def setLinkS(self,linkS):
        self.linkS = linkS

    def setLinkYT(self, linkYT):
        self.linkYT = linkYT
    
    def setID(self, identificador):
        self.identificador = identificador
    
    