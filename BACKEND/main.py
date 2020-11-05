from flask import Flask,jsonify, request
from flask_cors import CORS
from Usuario import  Us
from Canciones import Cancion
import json

app=Flask(__name__)
CORS(app)
#ARREGLOS PARA ALMACENAR DATOS
cont_canciones=0
USERS=[]
CANCIONES=[]
SOLICITUDES=[]

USERS.append(Us('DARLENY_MI_AMOR','T0XICA_YUMAN','admin','1234','0'))
USERS.append(Us('ALEJANDRO','GER','ale','sol','1'))
USERS.append(Us('PACO','LOF','pac','pac14','0'))
USERS.append(Us('PABLO','VALLE','cato','taquito1','1'))

SOLICITUDES.append(Cancion("A","A","A","A","A","A","A","A"))
SOLICITUDES.append(Cancion("b","b","b","b","b","b","b","b"))
SOLICITUDES.append(Cancion("A","A","A","A","A","A","A","A"))



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

#ELIMINAR UN DATO ESPECIFICO 
@app.route('/Usuario/<string:nombre>', methods=['DELETE'])
def EliminarUsuario(nombre):
    global USERS
    for i in range(len(USERS)):
        if nombre == USERS[i].getNombre():
            del USERS[i]
            break
    respuesta = jsonify({'message':'se elimino correctamente'})
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
    global SOLICITUDES
    nombre = request.json['NombreS']
    artista = request.json['ArtistaS']
    album = request.json['AlbumS']
    imagen = request.json['ImagenS']
    fecha = request.json['FechaS']
    linkSpotify = request.json['LinkSS']
    linkYoutube = request.json['LinkYTS'] 
    ident=0

    NSOLI=Cancion(nombre,artista,album,imagen,fecha,linkSpotify,linkYoutube,ident)
    SOLICITUDES.append(NSOLI)

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

if __name__ == "__main__":
    app.run(port=3000,debug=True)
