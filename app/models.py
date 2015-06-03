from app import db

class Event(db.Model):
    idEvent        = db.Column(db.Integer, primary_key=True)
    creador        = db.Column(db.Integer, db.ForeignKey('person.idPerson'))
    nombre         = db.Column(db.String(128))
    descripcion    = db.Column(db.String(256))
    ubicacion      = db.Column(db.String(256))
    fecha          = db.Column(db.String(10))
    capacidad      = db.Column(db.Integer)
    disponibilidad = db.Column(db.Integer)
    

    def __repr__(self):
        return '<Event %r>' % (self.nombre)

class Person(db.Model):
    idPerson   = db.Column(db.Integer, primary_key=True)
    nombres    = db.Column(db.String(128))
    apellidos  = db.Column(db.String(128))
    nickname   = db.Column(db.String(64), index=True, unique=True)
    contrasena = db.Column(db.String(16))
    edad       = db.Column(db.Integer)
    telefono   = db.Column(db.String(11))
    correo     = db.Column(db.String(120), index=True, unique=True)
    admin      = db.Column(db.Boolean)

    def __repr__(self):
        return '<Person %r>' % (self.nombres) % (self.apellidos)

class Reservacion(db.Model):
    idReservacion = db.Column(db.Integer, primary_key=True)
    idEvent      = db.Column(db.Integer, db.ForeignKey('event.idEvent'  ))
    idPerson     = db.Column(db.Integer, db.ForeignKey('person.idPerson'))
    asistio      = db.Column(db.Boolean)
    #events       = db.relationship('Event', backref=db.backref('eventos', lazy='dynamic'))

    def __repr__(self):
        return '<Reservacion %r>' % (self.idReservacion)


