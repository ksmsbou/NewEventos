# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

cu2 = Blueprint('cu2', __name__)


@cu2.route('/cu2/ACertificado')
def ACertificado():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventoInscrito', 'msg':[ur'Certificado obtenido']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/ACredencial')
def ACredencial():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventoInscrito', 'msg':[ur'Credencial recibida']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/AReservarEvento')
def AReservarEvento():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventosInscritos', 'msg':[ur'Reservado']}, {'label':'/VEventosNoInscritos', 'msg':[ur'No Reservado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/AVerEventoInscrito')
def AVerEventoInscrito():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventoInscrito', 'msg':[ur'Visto Inscrito']}, {'label':'/VEventosInscritos', 'msg':[ur'No Visto Inscrito']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/AVerEventoNoInscrito')
def AVerEventoNoInscrito():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventoNoInscrito', 'msg':[ur'Visto No Inscrito']}, {'label':'/VEventosNoInscritos', 'msg':[ur'No Visto No Inscrito']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/AVerEventosInscritos')
def AVerEventosInscritos():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventosInscritos', 'msg':[ur'Vistos Inscritos']}, {'label':'/VPrincipalUsuario', 'msg':[ur'No Vistos Inscritos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/AVerEventosNoInscritos')
def AVerEventosNoInscritos():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VEventosNoInscritos', 'msg':[ur'Vistos No Inscritos']}, {'label':'/VPrincipalUsuario', 'msg':[ur'No Vistos No Inscritos']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/VEventoInscrito')
def VEventoInscrito():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventoNoInscrito')
def VEventoNoInscrito():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventosInscritos')
def VEventosInscritos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventosNoInscritos')
def VEventosNoInscritos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VPrincipalUsuario')
def VPrincipalUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here