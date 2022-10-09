from .db import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first_name

    def serialize(self):                                          #defino el dictionary de mi clase para que le asigne las propiedades a mi objeto
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
            #"password": self.password, do not serialize the password, its a security breach
        }
        

class People_Favorites(db.Model):
    #estoy creando una clase People  
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)                                        #este tipo de dato me permite escoger en tre imagen video o galeria
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True,unique=False)#esta es la unica llave foranea obligatoria necesaria
    usuario = db.relationship(User, lazy=True, backref="people") #relacion de uno a muchos un usuario tiene muchos favoritos 
    name = db.Column(db.String(250), unique=False, nullable=True) #este dato lo recibo de mi starwars api
    picture_url = db.Column(db.String(250), unique=False, nullable=True) #este dato lo recibo de mi starwars api
    description = db.Column(db.String(250), unique=False, nullable=True) #este dato lo recibo de mi starwars api
    

    def __repr__(self):
        return '<PeopleFavorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "usuario": self.user_id,
            "name": self.name,
            "picture_url": self.picture_url,
            "description": self.description          
        }

class Planets_Favorites(db.Model):
    #estoy creando una clase PLANETAs media que hereda el ID de mi tabla Post
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True,unique=False)#esta es la unica llave foranea obligatoria necesaria
    usuario = db.relationship(User, lazy=True, backref="planetas") #relacion de uno a muchos un usuario tiene muchos favoritos                                        #este tipo de dato me permite escoger en tre imagen video o galeria
    planetas_name = db.Column(db.String(250)) #este dato lo recibo de mi starwars api
    planetas_picture_url = db.Column(db.String(250)) #este dato lo recibo de mi starwars api
    planetas_description = db.Column(db.String(250)) #este dato lo recibo de mi starwars api

    
    def __repr__(self):
        return '<Planets_Favorites %r>' % self.id
        
    def serialize(self):
        return {
            "id": self.id,
            "usuario": self.user_id,
            "name": self.planetas_name,
            "pictura_url": self.planetas_picture_url,
            "description":self.planetas_description       
        }
