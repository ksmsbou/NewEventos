# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

cu2 = Blueprint('cu2', __name__)
from app import db, models


@cu2.route('/cu2/ACertificado')
def ACertificado():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VCertificado', 'msg':[ur'Certificado recibido']}, ]
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
    results = [{'label':'/VCredencial', 'msg':[ur'Credencial Recibida']}, ]
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

    new_reservacion = models.Reservacion(idEvent=session['idevento'],idPerson=session['usrid'],asistio=False)
    evento = models.Event.query.filter(models.Event.idEvent == session['idevento']).first()
    evento.disponibilidad -= 1
    db.session.add(new_reservacion)
    db.session.commit()

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

    session['idevento'] = request.args['id']

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

    session['idevento'] = request.args['id']

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@cu2.route('/cu2/VCertificado')
def VCertificado():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    event = models.Event.query.get(int(session['idevento']))
    e = {'nombre':event.nombre,'fecha':event.fecha, 'ubicacion': event.ubicacion}

    person = models.Person.query.get(int(session['usrid']))
    e.update({'nperson':person.nombres, 'aperson':person.apellidos})

    res['data103'] = e

    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VCredencial')
def VCredencial():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    event = models.Event.query.get(int(session['idevento']))
    e = {'nombre':event.nombre,'idevento':event.idEvent}

    person = models.Person.query.get(int(session['usrid']))
    e.update({'nperson':person.nombres, 'aperson':person.apellidos, 'idperson':person.idPerson})

    res['data102'] = e


    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventoInscrito')
def VEventoInscrito():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    event = models.Event.query.get(int(session['idevento']))
    reserv = models.Reservacion.query.filter(models.Reservacion.idEvent == session['idevento'], models.Reservacion.idPerson == session['usrid']).first()
    if reserv is not None:
        res['data101'] = {'nombre':event.nombre,'descripcion':event.descripcion,'ubicacion':event.ubicacion,'fecha':event.fecha,
                 'capacidad':event.capacidad, 'disponibilidad':event.disponibilidad}
    else:
        # TODO Pensar una mejor manera de informar al usuario
        res['data101'] = {'nombre':'Error en el intento de acceso a pagina, evento no reservado'}

    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventoNoInscrito')
def VEventoNoInscrito():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    event = models.Event.query.get(int(session['idevento']))
    reserv = models.Reservacion.query.filter(models.Reservacion.idEvent == session['idevento'], models.Reservacion.idPerson == session['usrid']).first()
    if reserv is None:
        res['data102'] = {'nombre':event.nombre,'descripcion':event.descripcion,'ubicacion':event.ubicacion,'fecha':event.fecha,
                'capacidad':event.capacidad, 'disponibilidad':event.disponibilidad}
    else:
        # TODO Pensar una mejor manera de informar al usuario
        res['data102'] = {'nombre':'Error en el intento de acceso a pagina, evento ya reservado'}

    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventosInscritos')
def VEventosInscritos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    # TODO Intentar relizar consultas mas eficientes
    session['idevento'] = 0
    e = []
    reservaciones = models.Reservacion.query.filter(models.Reservacion.idPerson == session['usrid'])
    for reservacion in reservaciones:
        event = models.Event.query.filter(models.Event.idEvent == reservacion.idEvent).first()
        e.append({'idEvento':event.idEvent,'nombre':event.nombre,'fecha':event.fecha})
    res['data0'] = e

    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VEventosNoInscritos')
def VEventosNoInscritos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    # TODO Intentar relizar consultas mas eficientes
    session['idevento'] = 0
    e = []
    reservaciones = models.Reservacion.query.filter(models.Reservacion.idPerson == session['usrid'])
    for evento in models.Event.query.all():
        event_is_here = False
        for reservacion in reservaciones:
            if evento.idEvent == reservacion.idEvent:
                event_is_here = True
                break
        if not event_is_here:
            e.append({'idEvento':evento.idEvent,'nombre':evento.nombre,'fecha':evento.fecha})
    res['data0'] = e

    #Action code ends here
    return json.dumps(res)



@cu2.route('/cu2/VPrincipalUsuario')
def VPrincipalUsuario():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    session['idevento'] = 0

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here