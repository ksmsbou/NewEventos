# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

cu1 = Blueprint('cu1', __name__)
from app import db, models
import os


@cu1.route('/cu1/ACrearEvento', methods=['POST'])
def ACrearEvento():
    #Access to POST/PUT fields using request.form['name']
    #Access to file fields using request.files['name']
    results = [{'label':'/VPrincipalAdministrador', 'msg':[ur'Evento Creado']}, {'label':'/VCrearEvento', 'msg':[ur'Evento No Creado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    cre = session['usrid']
    nam = request.form['nombre']
    des = request.form['descripcion']
    ubi = request.form['ubicacion']
    fec = request.form['fecha']
    cap = request.form['capacidad']
    dis = cap
    if 'afiche' in request.files:
        afic = request.files['afiche']
        if afic.filename[len(afic.filename)-4:] == '.pdf':
            path = os.path.abspath(os.path.dirname(__file__))
            new_event = models.Event(creador=cre,nombre=nam,descripcion=des,ubicacion=ubi,fecha=fec,capacidad=cap,disponibilidad=dis)
            db.session.add(new_event)
            evento = models.Event.query.filter(models.Event.nombre == nam).first()
            afic.save(path[0:len(path)-14]+'/afiches/afiche'+str(evento.idEvent)+'.pdf')
        else:
            res = results[1]
    else:
        new_event = models.Event(creador=cre,nombre=nam,descripcion=des,ubicacion=ubi,fecha=fec,capacidad=cap,disponibilidad=dis)
        db.session.add(new_event)
    db.session.commit()

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

    #Busca y elimina todas las reservaciones asociadas al evento
    reserve = models.Reservacion.query.filter(models.Reservacion.idEvent == session['idevento']).all()
    for reser in reserve:
        db.session.delete(reser)
    db.session.commit()
    #Elimina el afiche del evento si existe
    path = os.path.abspath(os.path.dirname(__file__))
    if os.path.exists(path[0:len(path)-14]+'/afiches/afiche'+str(session['idevento'])+'.pdf'):
        os.remove(path[0:len(path)-14]+'/afiches/afiche'+str(session['idevento'])+'.pdf')
    #Elimina ahora el evento
    event = models.Event.query.filter(models.Event.idEvent == session['idevento']).first()
    db.session.delete(event)
    db.session.commit()

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

    # TODO Agregar restricciones a la modificacion por fecha
    nam = request.form['nombre']
    des = request.form['descripcion']
    ubi = request.form['ubicacion']
    fec = request.form['fecha']
    cap = int(request.form['capacidad'])
    evento = models.Event.query.filter(models.Event.idEvent == session['idevento']).first()
    ocupados = int(evento.capacidad) - int(evento.disponibilidad)
    if cap < ocupados :
        res = results[1]
    else :
        evento.nombre = nam
        evento.descripcion = des
        evento.ubicacion = ubi
        evento.fecha = fec
        evento.capacidad = cap
        evento.disponibilidad = cap - ocupados
        db.session.commit()

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

    session['idevento'] = request.args['id']

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

    evento = models.Event.query.filter(models.Event.idEvent==session['idevento']).first()
    form = {
        'nombre' : evento.nombre,
        'descripcion' : evento.descripcion,
        'ubicacion' : evento.ubicacion,
        'fecha' : evento.fecha,
        'capacidad' : evento.capacidad,
        'disponibilidad' : evento.disponibilidad,
    }
    res['fEvento'] = form

    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VPrincipalAdministrador')
def VPrincipalAdministrador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    session['idevento'] = 0
    events = models.Event.query.filter(models.Event.creador == session['usrid']).order_by(models.Event.nombre)
    e = []
    for event in events:
        e.append({'idEvento':event.idEvent,'nombre':event.nombre,'fecha':event.fecha})
    res['data2'] = e

    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VVerEvento')
def VVerEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    # TODO Intentar relizar consultas mas eficientes
    event = models.Event.query.get(int(session['idevento']))
    e = {'nombre':event.nombre,'descripcion':event.descripcion,'ubicacion':event.ubicacion,'fecha':event.fecha,
             'capacidad':event.capacidad, 'disponibilidad':event.disponibilidad}
    res['data100'] = e
    p = []
    reservaciones = models.Reservacion.query.filter(models.Reservacion.idEvent == session['idevento'])
    for reservacion in reservaciones:
        persona = models.Person.query.filter(models.Person.idPerson == reservacion.idPerson).first()
        p.append({'idPersona':persona.idPerson,'nombres':persona.nombres,'apellidos':persona.apellidos})
    res['data3'] = p

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here