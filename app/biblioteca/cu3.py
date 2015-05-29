# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

cu3 = Blueprint('cu3', __name__)
from app import db, models


@cu3.route('/cu3/AIdentificacion', methods=['POST'])
def AIdentificacion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipalUsuario', 'msg':[ur'Vista de Usuario'], "actor":"usuario"}, {'label':'/VPrincipalAdministrador', 'msg':[ur'Vista de Administrador'], "actor":"administrador"}, {'label':'/VPrincipal', 'msg':[ur'No Identificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    username = params['unickname']
    password = params['ucontrasena']
    registered_user = models.Person.query.filter_by(nickname=username,contrasena=password).first()

    if registered_user is None:
        res = results[2]
    else:
        session['usrid'] = registered_user.idPerson
        if registered_user.admin:
            res = results[1]
        else:
            res = results[0]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu3.route('/cu3/ARegistro', methods=['POST'])
def ARegistro():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipal', 'msg':[ur'Registrado']}, {'label':'/VRegistro', 'msg':[ur'No Registrado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    name = params['nombres']
    lnam = params['apellidos']
    nick = params['nickname']
    pasw = params['contrasena']
    ages = params['edad']
    phon = params['telefono']
    mail = params['correo']
    admi = params['administrador']
    if admi == 'n' or admi == 'N':
        new_person = models.Person(nombres=name,apellidos=lnam,nickname=nick,contrasena=pasw,edad=ages,telefono=phon,correo=mail,admin=False)
    else:
        new_person = models.Person(nombres=name,apellidos=lnam,nickname=nick,contrasena=pasw,edad=ages,telefono=phon,correo=mail,admin=True)
    db.session.add(new_person)
    db.session.commit()


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu3.route('/cu3/ASalir')
def ASalir():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipal', 'msg':[ur'Sesion Cerrada'], "actor":None}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    del session['usrid']

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu3.route('/cu3/VPrincipal')
def VPrincipal():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu3.route('/cu3/VRegistro')
def VRegistro():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here