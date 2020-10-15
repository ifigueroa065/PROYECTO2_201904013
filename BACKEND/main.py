from flask import Flask,jsonify, request
from flask_cors import CORS
from Usuario import  Us
import json

app=Flask(__name__)
CORS(app)
USERS=[]

USERS.append(Us('DARLENY_MI_AMOR','T0XICA_YUMAN','admin','1234','0'))
USERS.append(Us('ALEJANDRO','GER','ale','sol','1'))
USERS.append(Us('PACO','LOF','pac','pac14','0'))
USERS.append(Us('PABLO','VALLE','cato','taquito1','1'))

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

#MODIFICAR UN DATO ESPECIFICO 
@app.route('/Usuario/<string:usuario>', methods=['PUT'])
def ActualizarUsuario(usuario):
    global USERS
    confirm = request.json['password']
    contra = request.json['contraM']
    for i in range(len(USERS)):
        if usuario == USERS[i].getUsuario():
            USERS[i].setNombre(request.json['nombre'])
            USERS[i].setApellido(request.json['apellido'])
            USERS[i].setUsuario(request.json['usuario'])
            if contra==confirm:
                USERS[i].setPassword(request.json['password'])    
            else:
                DAT={
                'message':'Failed',
                'reason': 'NO COICIDEN CONTRASEÑAS'
            }
            break
    DAT={
        'message':'Sucess'
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


if __name__ == "__main__":
    app.run(port=3000,debug=True)
