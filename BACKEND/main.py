from flask import Flask,jsonify, request
from flask_cors import CORS
from Usuario import  Us
from Canciones import Cancion
import json
from Comentarios import Comentario
from Playlist import Play
import re

app=Flask(__name__)
CORS(app)
#ARREGLOS PARA ALMACENAR DATOS
cont_canciones=0
cont_solicitudes=0

PLAYLIST=[]
COMENTARIOS=[]
USERS=[]
CANCIONES=[]
SOLICITUDES=[]

USERS.append(Us('Usuario','Maestro','admin','admin','0'))

@app.route('/', methods=['GET'])
def Rutainicial():
    return('PAGINA INICIAL')

#VISTA GENERAL
@app.route('/Usuario', methods=['GET'])
def ObtenerPersonas():
    global USERS
    Temp = []
    for i in USERS:
        Temp2 = {
            'nombre': i.getNombre(), 
            'apellido': i.getApellido(), 
            'usuario': i.getUsuario(),
            'password':i.getPassword(),
            'tipo':i.getTipo()

         }
        Temp.append(Temp2)
    respuesta = jsonify(Temp)
    return(respuesta)

#VISTA GENERAL CANCIONES
@app.route('/CANCIONES', methods=['GET'])
def MOSTRARCANCIONES():
    global CANCIONES,cont_canciones
    TempZ = []
    for i in CANCIONES:
        Temp3 = {
            'nombre' : i.getNombre(),
            'artista' : i.getArtista(), 
            'album' : i.getAlbum(),
            'imagen' : i.getImagen(),
            'fecha' : i.getFecha(),
            'linkS' : i.getLinkS(),
            'linkYT' : i.getLinkYT(),
            'identificador' : i.getID()
         }
        TempZ.append(Temp3)
    res = jsonify(TempZ)
    return(res)

#VISTA GENERAL DE SOLICITUDES
@app.route('/SOLICITUDES', methods=['GET'])
def MOSTRARSOLICITUDES():
    global SOLICITUDES
    TempZ = []
    for i in SOLICITUDES:
        Temp3 = {
            'nombre' : i.getNombre(),
            'artista' : i.getArtista(), 
            'album' : i.getAlbum(),
            'imagen' : i.getImagen(),
            'fecha' : i.getFecha(),
            'linkS' : i.getLinkS(),
            'linkYT' : i.getLinkYT(),
            'identificador' : i.getID()
         }
        TempZ.append(Temp3)
    res = jsonify(TempZ)
    return(res)     

#VISTA GENERAL COMENTARIOS
@app.route('/COMENTARIOS', methods=['GET'])
def MOSTRARCOMENTS():
    global COMENTARIOS
    TempZ = []
    for i in COMENTARIOS:
        Temp3 = {
            'comentario' : i.getComentario(),
            'usuario' : i.getUsuario(), 
            'id' : i.getID()
         }
        TempZ.append(Temp3)
    res = jsonify(TempZ)
    return(res)

#VISTA GENERAL PLAYLIST
@app.route('/PLAYLIST', methods=['GET'])
def MOSTRARPLAYLIST():
    global PLAYLIST
    TempZ = []
    for i in PLAYLIST:
        Temp3 = {
            'usuario' : i.getUsuario(), 
            'id' : i.getID()
         }
        TempZ.append(Temp3)
    res = jsonify(TempZ)
    return(res)

#BUSCAR NOMBRE ESPECIFICO 
@app.route('/Usuario/<string:usuario>', methods=['GET'])
def ObtenerUsuario(usuario):
    global USERS
    for i in USERS:
        if i.getUsuario()==usuario:
            Temp2 = {
                'nombre': i.getNombre(), 
                'apellido': i.getApellido(), 
                'usuario': i.getUsuario(),
                'password':i.getPassword(),
                'tipo':i.getTipo()
            }
            break
    respuesta = jsonify(Temp2)
    return(respuesta)
    
#BUSCAR CANCION ESPECIFICA   
@app.route('/CANCIONES/<int:id>', methods=['GET'])
def CANCIONESPE(id):
    global CANCIONES
    for i in CANCIONES:
        if i.getID()==id:
            Temp2 = {
                'nombre' : i.getNombre(),
            'artista' : i.getArtista(), 
            'album' : i.getAlbum(),
            'imagen' : i.getImagen(),
            'fecha' : i.getFecha(),
            'linkS' : i.getLinkS(),
            'linkYT' : i.getLinkYT()
            }
            break
    respuesta = jsonify(Temp2)
    return(respuesta)    

#MODIFICAR UN DATO ESPECIFICO 
@app.route('/Usuario/<string:usuario>', methods=['PUT'])
def ActualizarUsuario(usuario):
    global USERS
    confirmar=True
    cor=False
    Muser= request.json['usuario']
    confirm = request.json['password']
    contra = request.json['contraM']
    if contra==confirm:
        confirmar=False
    else:
        DAT = {
                'message':'Failed',
                'reason':'NO COINCIDEN CONTRASEÑAS'
            }

    for i in range(len(USERS)):
        if Muser==USERS[i].getUsuario() and Muser != usuario:
            cor=True
            break 
    if cor==False:
        for i in range(len(USERS)):
            if usuario == USERS[i].getUsuario() and confirmar==False:
                USERS[i].setNombre(request.json['nombre'])
                USERS[i].setApellido(request.json['apellido'])
                USERS[i].setUsuario(Muser)
                USERS[i].setPassword(contra)
                DAT = {
                    'message':'Sucess'
                }  
                break
    else:
       DAT = {
            'message':'Failed',
            'reason':'EL USUARIO YA ESTÁ EN USO'
        }   
    respuesta = jsonify(DAT)
    return(respuesta)

#BUSCAR COMENTARIOS ESPECÍFICOS   
@app.route('/COMENTARIOS/<int:id>', methods=['GET'])
def COMENT(id):
    global COMENTARIOS
    Temp=[]
    for i in COMENTARIOS:
        if i.getID()==id:
            Temp2 = {
            'comentario' : i.getComentario(),
            'usuario' : i.getUsuario()
            }
            Temp.append(Temp2)
    respuesta = jsonify(Temp)
    return(respuesta)    

#BUSCAR PLAYLIST DE USUARIO ESPECÍFICO  
@app.route('/PLAYLIST/<string:usuario>', methods=['GET'])
def VERPLAYLIST(usuario):
    global PLAYLIST,CANCIONES
    TEMP=[]
    for i in PLAYLIST:
        if i.getUsuario()==usuario:
            CANCION=i.getID()
            for j in CANCIONES:
                if CANCION==j.getID():
                    Temp3 = {
                    'nombre' : j.getNombre(),
                    'artista' : j.getArtista(), 
                    'album' : j.getAlbum(),
                    'imagen' : j.getImagen(),
                    'fecha' : j.getFecha(),
                    'linkS' : j.getLinkS(),
                    'linkYT' : j.getLinkYT()
                    }
                    TEMP.append(Temp3)
                    break
    res = jsonify(TEMP)    
    return(res)    

#MODIFICAR CANCION ESPECÍFICA
@app.route('/CANCIONES/<int:id>', methods=['PUT'])
def ActualizarCANCION(id):
    global CANCIONES
    cor=True
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    imagen = request.json['imagen']
    fecha = request.json['fecha']
    linkSpotify = request.json['linkS']
    linkYoutube = request.json['linkYT'] 

        
    if cor==True:
        for i in range(len(CANCIONES)):
            if id == CANCIONES[i].getID():
                CANCIONES[i].setNombre(nombre)
                CANCIONES[i].setArtista(artista)
                CANCIONES[i].setAlbum(album)
                CANCIONES[i].setImagen(imagen)
                CANCIONES[i].setFecha(fecha)
                CANCIONES[i].setLinkS(linkSpotify)
                CANCIONES[i].setLinkYT(linkYoutube)                
                DAT = {
                    'message':'Sucess'
                }  
                break
    else:
       DAT = {
            'message':'Failed',
            'reason':'EL USUARIO YA ESTÁ EN USO'
        }   
    respuesta = jsonify(DAT)
    return(respuesta)

#ELIMINAR UN USUARIO ESPECIFICO 
@app.route('/Usuario/<string:usuario>', methods=['DELETE'])
def EliminarUsuario(usuario):
    global USERS
    for i in range(len(USERS)):
        if usuario == USERS[i].getUsuario():
            del USERS[i]
            break
    respuesta = jsonify({'message':'se eliminó usuario correctamente'})
    return(respuesta)    

#ELIMINAR UNA CANCION ESPECIFICA
@app.route('/CANCIONES/<int:id>', methods=['DELETE'])
def EliminarCancion(id):
    global CANCIONES
    for i in range(len(CANCIONES)):
        if id == CANCIONES[i].getID():
            del CANCIONES[i]
            break
    respuesta = jsonify({'message':'se eliminó cancion correctamente'})
    return(respuesta)    


#AGREGAR USUARIOS
@app.route('/Usuarios/', methods=['POST'])
def AgregarUsuario():
    global USERS
    TempADD= Us(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['password'],request.json['tipo'])
    USERS.append(TempADD)
    return('SE AGREGO EL USUARIO')

#MÉTODO PARA LOGEAR USUARIOS
@app.route('/Login/', methods=['POST'])
def Login():
    global USERS
    usuario = request.json['usuario']
    password = request.json['password']
    for i in USERS:
        if i.getUsuario() == usuario and i.getPassword() == password:
            Dato={
                'message': 'Sucess',
                'usuario': i.getUsuario(),
                'tipo':i.getTipo()
            }
            break
        else:
            Dato={
                'message': 'Failed',
                'usuario': ''
            }
    respuesta=jsonify(Dato)
    return (respuesta)

#MÉTODO RECUPERAR CONTRASEÑA
@app.route('/Recuperar/', methods=['POST'])
def Recuperar():
    global USERS
    usuario = request.json['usuarioR']
    for i in range(len(USERS)):
        if USERS[i].getUsuario() == usuario:
            Dato={
                'message': 'Sucess',
                'lol': USERS[i].getPassword()
            }
            break
        else:
            Dato={
                'message': 'Failed',
                'lol': 'no, no hay'
            }
    respuesta=jsonify(Dato)
    return (respuesta)    

#REGISTRAR TIPO USUARIO
@app.route('/Registrar/', methods=['POST'])
def SIGNUP():
    global USERS
    condicion=True
    nombreR = request.json['nombreR']
    apellidoR = request.json['apellidoR']
    usuarioR = request.json['usuarioR']
    contraR = request.json['contraR']
    contrasR = request.json['contraRR']
    tipo = "1"
              
    if contraR == contrasR:
        for i in range(len(USERS)):
            if USERS[i].getUsuario() == usuarioR:
                Dat={
                    'message': 'Failed',
                    'motivo' : 'EL USUARIO YA EXISTE'
                }
                condicion=False
                break
            else:
                condicion=True 
        
        if condicion==True:
            NUSER= Us(nombreR,apellidoR,usuarioR,contraR,tipo)
            USERS.append(NUSER)
            Dat = {
                'message': 'Sucess'
            } 
    else:
        Dat = {
         'message': 'Failed',
         'motivo': 'NO COINCIDEN CONTRASEÑAS'
        } 
       
    respo=jsonify(Dat)
    return(respo)

#REGISTRAR TIPO ADMINISTRADOR
@app.route('/RegistrarADMIN/', methods=['POST'])
def SIGNUPADMIN():
    global USERS
    condicion=True
    nombreR = request.json['nombreR']
    apellidoR = request.json['apellidoR']
    usuarioR = request.json['usuarioR']
    contraR = request.json['contraR']
    contrasR = request.json['contraRR']
    tipo = "0"
              
    if contraR == contrasR:
        for i in range(len(USERS)):
            if USERS[i].getUsuario() == usuarioR:
                Dat={
                    'message': 'Failed',
                    'motivo' : 'EL USUARIO YA EXISTE'
                }
                condicion=False
                break
            else:
                condicion=True 
        
        if condicion==True:
            NUSAD= Us(nombreR,apellidoR,usuarioR,contraR,tipo)
            USERS.append(NUSAD)
            Dat = {
                'message': 'Sucess'
            } 
    else:
        Dat = {
         'message': 'Failed',
         'motivo': 'NO COINCIDEN CONTRASEÑAS'
        } 
       
    respo=jsonify(Dat)
    return(respo)

#SOLICITAR UNA CANCION
@app.route('/SOLICITAR/', methods=['POST'])
def CrearSolicitud():
    global SOLICITUDES,cont_solicitudes
    nombre = request.json['NombreS']
    artista = request.json['ArtistaS']
    album = request.json['AlbumS']
    imagen = request.json['ImagenS']
    fecha = request.json['FechaS']
    linkSpotify = request.json['LinkSS']
    linkYoutube = request.json['LinkYTS'] 
    ident=cont_solicitudes

    NSOLI=Cancion(nombre,artista,album,imagen,fecha,linkSpotify,linkYoutube,ident)
    SOLICITUDES.append(NSOLI)
    cont_solicitudes+=1

    respo=jsonify({'message':'SE CREÓ SOLICITUD'})
    return(respo)

#AGREGAR UNA CANCION
@app.route('/CANCIONES/', methods=['POST'])
def AGREGARCANCION():
    global CANCIONES,cont_canciones
    nombre = request.json['NombreS']
    artista = request.json['ArtistaS']
    album = request.json['AlbumS']
    imagen = request.json['ImagenS']
    fecha = request.json['FechaS']
    linkSpotify = request.json['LinkSS']
    linkYoutube = request.json['LinkYTS'] 
    ident=cont_canciones

    NSOLI=Cancion(nombre,artista,album,imagen,fecha,linkSpotify,linkYoutube,ident)
    CANCIONES.append(NSOLI)
    cont_canciones +=1

    respo=jsonify({'message':'SE CARGÓ UNA CANCION'})
    return(respo)    

#AGREGAR UNA CANCION DE SOLICITUDES
@app.route('/SOLICITUDES/<int:id>', methods=['POST'])
def AGREGARSOLICITUD(id):
    global CANCIONES,cont_canciones
    global SOLICITUDES,cont_solicitudes

    for i in SOLICITUDES:
        if i.getID()==id:
            nombre = i.getNombre() 
            artista =  i.getArtista()
            album =  i.getAlbum()
            imagen = i.getImagen()
            fecha = i.getFecha()
            linkSpotify =i.getLinkS() 
            linkYoutube =i.getLinkYT()
            break
    
    ident=cont_canciones
    NSOLI=Cancion(nombre,artista,album,imagen,fecha,linkSpotify,linkYoutube,ident)
    CANCIONES.append(NSOLI)
    cont_canciones +=1
    for i in range(len(SOLICITUDES)):
        if id == SOLICITUDES[i].getID():
            del SOLICITUDES[i]
            break

    respo=jsonify({'message':'SE ACEPTÓ UNA CANCION'})
    return(respo)  

#RECHAZAR UNA SOLICITUD
@app.route('/SOLICITUDES/<int:id>', methods=['DELETE'])
def RECHAZARSOLICITUD(id):
    global SOLICITUDES,cont_solicitudes
    for i in range(len(SOLICITUDES)):
        if id == SOLICITUDES[i].getID():
            del SOLICITUDES[i]
            break

    respo=jsonify({'message':'SE RECHAZÓ LA CANCION'})
    return(respo)


#AGREGAR COMENTARIOS
@app.route('/COMENTARIO/<int:id>', methods=['POST'])
def SAVECOMENT(id):
    global COMENTARIOS
    
    comen=request.json['comentario']
    usuario=request.json['usuario']
    NCOMENT=Comentario(comen,usuario,id)
    COMENTARIOS.append(NCOMENT)

    respo=jsonify({'message':'SE AGREGÓ EL COMENTARIO'})
    return(respo)

#AGREGAR CANCION A PLAYLIST
@app.route('/PLAYLIST/<int:id>', methods=['POST'])
def SAVECANCION(id):
    global PLAYLIST,CANCIONES
    val=True
    usuario=request.json['usuario']
    
    for i in PLAYLIST:
        if i.getUsuario()==usuario:
                if i.getID()==id:  
                    val=False
                    break

    if val==True:
        NCOMENT=Play(usuario,id)
        PLAYLIST.append(NCOMENT)
        DATO={
            'message':'Sucess'
        }    
    else:
        DATO={
            'message':'Failed'
        }
    respo=jsonify(DATO)
    return(respo)

#BUSCADOR
@app.route('/BUSCAR/<string:word>', methods=['GET'])
def BUSCADOR(word):
    global CANCIONES
    Temp=[]
    for i in CANCIONES:
        chain=i.getNombre()
        if chain.find(word)>=0:
            Temp2 = {
            'nombre' : i.getNombre(),
            'artista' : i.getArtista(), 
            'album' : i.getAlbum(),
            'imagen' : i.getImagen(),
            'fecha' : i.getFecha(),
            'linkS' : i.getLinkS(),
            'linkYT' : i.getLinkYT(),
            'identificador' : i.getID()
            }
            Temp.append(Temp2)
    respuesta = jsonify(Temp)
    return(respuesta)    

if __name__ == "__main__":
    app.run(port=3000,debug=True)
