'''
This file contains the necessary commands to set up the database collections,
the schema and validations. 

For data examples refer to db_seeds.py

Order of creation
1. Mesas
2. Escuelas
3. Carreras
4. Envios
5. Alumni & Estudios
'''
from db_connection import db
# Run all collections
def collections_create():
    create_mesas()
    create_escuelas()
    create_carreras()
    create_envios()
    create_alumni()
    create_estudios()


def create_mesas():
    mesas = db.create_collection("mesas", {
        "validator": {
            "$jsonSchema": { 
                "bsonType": "object", 
                "title": "Mesas Object Validator", 
                "required": ["nombre", "numero"], 
                "properties": { 
                    "nombre": { 
                        'bsonType': "string", 
                        "description": "Debe ser string y es requerido" 
                    }, 
                    "numero": { 
                        "bsonType": "int", 
                        "minimum": 1, 
                        "maximum": 15, 
                        "description": "Es el numero de mesa, debe ser un entero entre 1 y 15" 
                    }
                }
            }
        }
    })
    print(mesas)


def create_escuelas():
    escuelas = db.create_collection("escuelas", {
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "title": "Escuelas Object Validator",
                "required": ["nombre", "siglas"],
                "properties": {
                    "nombre": {
                        "bsonType": "string",
                        "description": "Nombre de la Escuela o Facultad"
                    },
                    "siglas": {
                        "bsonType": "string",
                        "description": "Cadena separada por '|' que contiene todas las variaciones de siglas"
                    }
                    }
            }
        }
    })

    print(escuelas)


def create_carreras():
    carreras = db.create_collection("carreras", {
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "title": "Carreras Object Validator",
                "required": ["nombre", "grado", "mesaSG"],
                "properties": {
                    "nombre": {
                        "bsonType": "string",
                        "description": "Nombre de la carrera"
                    },
                    "grado": {
                        "bsonType": "string",
                        "description": "Grado académico que corresponde a la carrera"
                    },
                    "mesaSG": {
                        "bsonType": "objectid",
                        "description": "ID de la mesa que corresponde" ### TODO ¿cómo asignar este valor?
                    }
                }
            }
        }
    })


def create_envios():
    envios = ""


def create_alumni():
    alumni = ""


def create_estudios():
    estudios = ""


if __name__ == "__main__":
    collections_create()
