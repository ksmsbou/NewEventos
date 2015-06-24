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
    # TODO Buscar forma de mostrar todos los errores a la vez sin repetir codigo
    evento = models.Event.query.filter(models.Event.nombre == nam).first()
    if evento is None:
        if 'afiche' in request.files:
            afic = request.files['afiche']
            if afic.filename[len(afic.filename)-4:] == '.pdf':
                path = os.path.abspath(os.path.dirname(__file__))
                new_event = models.Event(creador=cre,nombre=nam,descripcion=des,ubicacion=ubi,fecha=fec,capacidad=cap,disponibilidad=dis)
                db.session.add(new_event)
                evento = models.Event.query.filter(models.Event.nombre == nam).first()
                afic.save(path[0:len(path)-14]+'/afiches/afiche'+str(evento.idEvent)+'.pdf')
                db.session.commit()
            else:
                results[1]['msg'].append('Tipo de archivo no permitido, el afiche debe estar en formato PDF de tamaño menor a 16MB.')
                res = results[1]
        else:
            new_event = models.Event(creador=cre,nombre=nam,descripcion=des,ubicacion=ubi,fecha=fec,capacidad=cap,disponibilidad=dis)
            db.session.add(new_event)
            db.session.commit()
    else:
        results[1]['msg'].append('Nombre de evento no disponible.')
        res = results[1]
    if res['label'] == '/VCrearEvento':
        session['formEv'] = {'nombre': nam, 'descripcion': des, 'ubicacion': ubi, 'fecha': fec, 'capacidad': int(cap)}

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
    # TODO Buscar forma de mostrar todos los errores a la vez sin repetir codigo
    if cap < ocupados:
        results[1]['msg'].append('Capacidad no puede ser menor a las reservaciones ya hechas, reservaciones: '+str(ocupados))
        res = results[1]
    else:
        old_evento = models.Event.query.filter(models.Event.nombre == nam).first()
        if (old_evento is None) or (evento.nombre == nam): # Ver si ya hay un evento con el nombre nuevo o si no se cambio el nombre.
            if 'afiche' in request.files: # Ver si se quiere agregar/modificar el afiche
                afic = request.files['afiche']
                if afic.filename[len(afic.filename)-4:] == '.pdf': # Ver si el archivo de afiche es un pdf
                    path = os.path.abspath(os.path.dirname(__file__))
                    if os.path.exists(path[0:len(path)-14]+'/afiches/afiche'+str(session['idevento'])+'.pdf'): # Ver si ya hay un afiche asociado a este evento
                        os.remove(path[0:len(path)-14]+'/afiches/afiche'+str(session['idevento'])+'.pdf') # Borrarlo si lo hay
                    evento.nombre = nam
                    evento.descripcion = des
                    evento.ubicacion = ubi
                    evento.fecha = fec
                    evento.capacidad = cap
                    evento.disponibilidad = cap - ocupados
                    afic.save(path[0:len(path)-14]+'/afiches/afiche'+str(evento.idEvent)+'.pdf')
                    db.session.commit()
                else:
                    results[1]['msg'].append('Tipo de archivo no permitido, el afiche debe estar en formato PDF de tamaño menor a 16MB.')
                    res = results[1]
            else:
                evento.nombre = nam
                evento.descripcion = des
                evento.ubicacion = ubi
                evento.fecha = fec
                evento.capacidad = cap
                evento.disponibilidad = cap - ocupados
                db.session.commit()
        else:
            results[1]['msg'].append('Nombre de evento ya existe')
            res = results[1]

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

    usr_to_confirm = request.args['id']
    reserv = models.Reservacion.query.filter(models.Reservacion.idPerson == usr_to_confirm, models.Reservacion.idEvent == session['idevento']).first()
    if reserv is None:
        results[1]['msg'].append('Error. Reservacion no existente')
        res = results[1]
    else:
        if reserv.asistio:
            reserv.asistio = False
            res['msg'] = [ur'Asistencia Anulada']
        else:
            reserv.asistio = True
        db.session.commit()

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

    if 'formEv' in session:
        res['fEvento'] = session['formEv']
        del session['formEv']

    #Action code ends here
    return json.dumps(res)



@cu1.route('/cu1/VModificarEvento')
def VModificarEvento():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    evento = models.Event.query.filter(models.Event.idEvent == session['idevento']).first()
    res['fEvento'] = {
        'nombre': evento.nombre,
        'descripcion': evento.descripcion,
        'ubicacion': evento.ubicacion,
        'fecha': evento.fecha,
        'capacidad': evento.capacidad,
        'disponibilidad': evento.disponibilidad,
    }

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
    path = os.path.abspath(os.path.dirname(__file__))
    pdfpath = ''
    e = {'nombre':event.nombre,'descripcion':event.descripcion,'ubicacion':event.ubicacion,'fecha':event.fecha,
             'capacidad':event.capacidad, 'disponibilidad':event.disponibilidad,'id':event.idEvent}
    if os.path.exists(path[0:len(path)-14]+'/afiches/afiche'+str(event.idEvent)+'.pdf'):
        pdfpath = path[0:len(path)-14]+'/afiches/afiche'+str(event.idEvent)+'.pdf'
        e['path'] = pdfpath
        e['filename'] = 'afiche'+str(event.idEvent)+'.pdf'
    res['data100'] = e
    p = []
    asistencia = 'Si'
    reservaciones = models.Reservacion.query.filter(models.Reservacion.idEvent == session['idevento'])
    for reservacion in reservaciones:
        if reservacion.asistio:
            asistencia = 'Si'
        else:
            asistencia = 'No'
        persona = models.Person.query.filter(models.Person.idPerson == reservacion.idPerson).first()
        p.append({'idPersona':persona.idPerson,'nombres':persona.nombres,'apellidos':persona.apellidos,'asistencia':asistencia})
    res['data3'] = p

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here