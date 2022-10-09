"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
#from .db import db
from api.models import db, User, Planets_Favorites, People_Favorites
from api.utils import generate_sitemap, APIException
from flask_bcrypt import Bcrypt
#from flask_jwt_extended import JWTManager, create_access_token,create_refresh_token, jwt_required, get_jwt_identity,get_jwt
import datetime 
import tempfile

app = Flask(__name__)
api = Blueprint('api', __name__)
bcrypt = Bcrypt(app)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

#ruta para crear el usuario
@api.route('/signup', methods=['POST'])
def crear_usuario():
    
    email=request.json.get("email")
    first_name=request.json.get("first_name")
    last_name=request.json.get("last_name")
    password=request.json.get("password")
    newUser=User(email=email, first_name=first_name, last_name=last_name, password=password, is_active= True )
    db.session.add(newUser)
    db.session.commit()
    response_body = {
        "message": "usuario creado exitosamente",
        "first_name":newUser.first_name,
        "last_name":newUser.last_name
    }
    return jsonify(response_body), 201

#ruta para obtener los usuarios
@api.route('/user', methods=['GET'])
def listar_usuarios():
    usuarios = User.query.all()
    usuarios = list(map(lambda user: user.serialize(), usuarios ))
    
    response_body = {
        "message": "Hello, this is your GET /user response ",
        "lista_usuarios": usuarios
    }

    return jsonify(response_body), 200

#ruta para agregar a una persona a favoritos base Favorites_People()
@api.route('/favorites/people', methods=['POST'])
def crear_personaje():

    user_id=request.json.get("user_id")
    name=request.json.get("name")
    picture_url=request.json.get("picture_url")
    description=request.json.get("description")
    newPeople=People_Favorites(user_id=user_id, name=name, picture_url=picture_url, description=description)
    db.session.add(newPeople)
    db.session.commit()

    response_body = {
        "message": "Personaje creado exitosamente ",
        "name": newPeople.name
    }
    return jsonify(response_body), 200

#ruta para obtener la lista de personajes favoritos de un usuario filtrar por usuario id actual
@api.route('/favorites/people', methods=['GET'])
def listar_personajes():
    personajes = People_Favorites.query.all()
    personajes = list(map(lambda people: people.serialize(), personajes ))
    
    response_body = {
        "message": "Hello, this is your GET /favorites/people response ",
        "lista_usuarios": personajes
    }

    return jsonify(response_body), 200

#ruta para obtener detalle de un personaje de los favoritos
@api.route('/favorites/people/<int>', methods=['GET'])
def listar_people2():
     response_body = {
        "msg": "Hello, this is your GET /people response "
    }

#ruta agregar un plalneta al listado de los favoritos base Favorites_Planets()
@api.route('/favorites/planet', methods=['POST'])
def create_planet():

    user_id=request.json.get("user_id")
    planetas_name=request.json.get("planetas_name")
    planetas_picture_url=request.json.get("planetas_picture_url")
    planetas_description=request.json.get("planetas_description")
    
    newPlanet=Planets_Favorites(user_id=user_id, planetas_name=planetas_name, planetas_picture_url=planetas_picture_url, planetas_description=planetas_description)
    db.session.add(newPlanet)
    db.session.commit()
    response_body = {
        "message": "planeta creado exitosamente",
        "name":newPlanet.planetas_name
        
    }
    return jsonify(response_body), 201

#ruta para obtener listado de planetas favoritos de un usuario filtrar por usuario id actual
@api.route('/favorites/planet', methods=['GET'])
def listar_planetas():    
    planetas = Planets_Favorites.query.all()
    planetas = list(map(lambda planetas: planetas.serialize(), planetas ))
    
    response_body = {
        "message": "Hello, this is your GET /favorites/planets response ",
        "lista_usuarios": planetas
    }

    return jsonify(response_body), 200

#ruta para obtener el listado de planetas favoritos de un usuario
@api.route('/favorites/planet/<int>', methods=['GET'])
def listar_planetas1():    
    response_body = {
        "msg": "Hello, this is your GET /people response "
    }


#ruta para obtener los planetas y personajes favoritos de un usuario
@api.route('/favorites', methods=['GET'])
def listar_Favoritos():    
    planetas = Planets_Favorites.query.all()
    planetas = list(map(lambda planetas: planetas.serialize(), planetas ))
    personajes = People_Favorites.query.all()
    personajes = list(map(lambda people: people.serialize(), personajes ))
    
    response_body = {
        "message": "Hello, this is your GET /favorites response ",
        "lista_planetas":planetas,
        "lista_personajes": personajes
    }
    return jsonify(response_body), 200