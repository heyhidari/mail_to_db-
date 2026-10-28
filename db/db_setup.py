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

Validator created with the guidance of MongoDB AI who transformed the code in the following link to Python 
https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/


'''
from db_connection import db
# Run all collections
def collections_create():
    try:
        collections = db.list_collection_names()
        if not "mesas" in collections:
            create_mesas()
        if not "escuelas" in collections:
            create_escuelas()
        if not "carreras" in collections:
            create_carreras()
        if not "envios" in collections:
            create_envios()
        if not "alumni" in collections:
            create_alumni()
        if not "estudios" in collections:
            create_estudios()
        else:
            print("All collections have been created.")
    except Exception as e: print(e)
    


def create_mesas():
    mesas_validator = {
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
    mesas = db.create_collection("mesas", validator = mesas_validator)
    print(mesas)


def create_escuelas():
    escuelas_validator = {
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
    escuelas = db.create_collection("escuelas", validator= escuelas_validator)
    print(escuelas)


def create_carreras():
    carreras_validator = {
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
                    "bsonType": "objectId",
                    "description": "ID de la mesa que corresponde" ### TODO ¿cómo asignar este valor?
                }
            }
        }
    }
    carreras = db.create_collection("carreras", validator= carreras_validator)
    print(carreras)


def create_envios():
    envios_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "Envíos Object Validator",
            "required": ["fecha", "cantidad", "escuela"],
            "properties": {
                "fecha": {
                    "bsonType": "date",
                    "description": "Fecha de envío de listado de expedientes"
                },
                "cantidad": {
                    "bsonType": "int",
                    "description": "Cantidad de expedientes en el listado"
                },
                "escuela": {
                    "bsonType": "objectId",
                    "description": "Escuela que envía el listado" ### TODO, asignar el objectId que corresponda
                }
            }
        }
    }
    envios = db.create_collection("envios", validator= envios_validator)
    print(envios)


def create_alumni():
    alumni_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "Alumni Object Validator",
            "required": ["curp", "apellido_1", "nombre"],
            "properties": {
                "curp": {
                    "bsonType": "string",
                    "description": "CURP del alumno, debe ser única y está verificada por ReGex"
                },
                "apellido_1": {
                    "bsonType": "string",
                    "description": "Primer apellido del alumno, el segundo es opcional"    
                },
                "nombre": {
                    "bsonType": "string",
                    "description": "Nombre(s) del alumno, debe poder hacer queries"
                }
            }
        }
    }
    alumni = db.create_collection("alumni", validator= alumni_validator)
    print(alumni)


def create_estudios():
    estudios_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "Estudios Object Validator",
            "required": ["curp", "carrera", "modalidad", "envio"],
            "properties": {
                "curp":{
                    "bsonType": "objectId",
                    "description": "El Id del alumno que corresponda"
                },
                "carrera": {
                    "bsonType": "objectId",
                    "description": "El Id de la carrera que corresponda"
                },
                "modalidad": {
                    "bsonType": "string",
                    "description": "Modalidad de titulación"
                },
                "envio": {
                    "bsonType": "objectId",
                    "description": "El Id del envío que quedó registrado"
                }
            }
        }
    }
    estudios = db.create_collection("estudios", validator= estudios_validator)
    print(estudios)


if __name__ == "__main__":
    collections_create()
