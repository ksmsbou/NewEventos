# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

cu1 = Blueprint('cu1', __name__)
from app import db, models


@cu1.route('/cu1/ACrearEvento', methods=['POST'])
def ACrearEvento():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VPrincipalAdministrador', 'msg':[ur'Evento Creado']}, {'label':'/VCrearEvento', 'msg':[ur'Evento No Creado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    cre = session['usrid']
    nam = request.form['nombre']
    des = request.form['descripccion']
    ubi = request.form['ubicacion']
    fec = request.form['fecha']
    cap = request.form['capacidad']
    dis = request.form['disponibilidad']
    print 'ola k ase'
    afi = request.files['afiche']
    print afi
    new_event = models.Event(creador=cre,nombre=nam,descripccion=des,ubicacion=ubi,fecha=fec,capacidad=cap,disponibilidad=dis,afiche=afi)
    db.session.add(new_event)
    if db.session.commit():
        res = results[0]
    #else:
    #    print db.session.commit()
    #    res = results[1]

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu1.route('/cu1/AEliminarEvento')
def AEliminarEvento():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VPrincipalAdministrador', 'msg':[ur'Evento Eliminado']}, {'label':'/VVerEvento', 'msg':[ur'Evento No Eliminado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu1.route('/cu1/AModificarEvento', methods=['POST'])
def AModificarEvento():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VVerEvento', 'msg':[ur'Evento Modificado']}, {'label':'/VModificarEvento', 'msg':[ur'Evento No Modificado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu1.route('/cu1/APersonaAsistio')
def APersonaAsistio():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VVerEvento', 'msg':[ur'Asistencia Confirmada']}, {'label':'/VVerEvento', 'msg':[ur'Asistencia No Confirmada']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu1.route('/cu1/AVerEvento')
def AVerEvento():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VVerEvento', 'msg':[ur'Evento Visto']}, {'label':'/VPrincipalAdministrador', 'msg':[ur'Evento No Visto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu1.route('/cu1/VCrearEvento')
def VCrearEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VModificarEvento')
def VModificarEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VPrincipalAdministrador')
def VPrincipalAdministrador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VVerEvento')
def VVerEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here