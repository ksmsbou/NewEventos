from flask import Flask, request, session
from flask.ext.script import Manager, Server
from random import SystemRandom
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os
from app import db 

app = Flask(__name__, static_url_path='')
manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=45)
    session.modified = True

@app.route('/')
def root():
    return app.send_static_file('index.html')

#Application code starts here

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+ os.path.join(basedir,'apl.db')
db = SQLAlchemy(app)


class Event(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    creador        = db.Column(db.String(128))
    nombre         = db.Column(db.String(128))
    descripccion   = db.Column(db.String(256))
    ubicacion      = db.Column(db.String(256))
    fecha          = db.Column(db.String(10))
    capacidad      = db.Column(db.Integer)
    disponibilidad = db.Column(db.Integer)
    afiche         = db.Column(db.Binary)

    def __repr__(self):
        return '<Event %r>' % (self.name)


class Person(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
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

#Application code ends here

from app.biblioteca.cu1 import cu1
app.register_blueprint(cu1)
from app.biblioteca.cu2 import cu2
app.register_blueprint(cu2)
from app.biblioteca.cu3 import cu3
app.register_blueprint(cu3)



if __name__ == '__main__':
    app.config.update(
      SECRET_KEY = repr(SystemRandom().random())
    )
    manager.run()