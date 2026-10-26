'''
This file has Mongosh instructions to test the DB Collections in the following order:

1. Mesas
2. Escuelas
3. Carreras
4. Envios
5. Alumni & Estudios

Step 5 makes simultaneous insertions to test crud_operations functions
'''
from db.crud_operations import db
from db.crud_operations import student_insert_many

# Inserta una mesa
def seed_mesas():
    seed = db.mesas.insert_one({
        "nombre": "Fulano de Tal", 
        "numero": 1
        })
    print(seed)


# Inserta una escuela
def seed_escuela():
    seed = db.escuelas.insert_one({
        "nombre": "Facultad de Medicina y Cirugía",
        "Siglas": "FMC|fmc"
    })
    print(seed)


# Inserta una carrera
def seed_carrera():
    seed = db.carreras.insert_one({
        "nombre": "Médico Cirujano",
        "grado": "Licenciatura",
        "mesa": "TODO encuentra la mesa a través de una instrucción ??" ### PENDIENTE
    })
    print(seed)


# Inserta un envío
def seed_envio():
    seed = db.envios.insert_one({
        "fecha": "20/11/2026",
        "cantidad": 2,
        "escuela": "TODO encuentra el _id de FMC" ### PENDIENTE
        "responsables": {
            "nombre":   "Sutanito de Té",
            "telefono": "1239874560",
            "correo:":  "correo@test.com"
        }
    })
    print(seed)


# Inserta dos alumnos y sus estudios
def seed_alumnos_y_estudios():
    seed = db.alumni.insert_many({
        {
            "curp": "ABCD123698HZZEFG11",
            "apellido_1": "Menganito",
            "apellido_2": "Sinapellido",
            "nombre": "NoSoy"
        },
        {
            "curp": "ZXCV745213HXXYTRE00",
            "apellido_1": "Canmexusa",
            "apellido_2": "Sinnombre",
            "nombre": "SiSoy"
        }
    })
    print(seed)

    seed2 = db.estudios.insert_many({
        {
            "curp": "TODO encuentra el id que le corresponde a la primera inserción de alumno", ###
            "carrera": "Médico Cirujano",
            "modalidad": "CENEVAL",
            "envio": "TODO encuentra el id del envío que corresponde",
            "entrega_mesa": None,
            "revision": None,
            "enviado_SS": None,
            "retorno_SS": None
        },
        {
            "curp": "TODO encuentra el id que le corresponde a la primera inserción de alumno", ###
            "carrera": "Médico Cirujano",
            "modalidad": "CENEVAL",
            "envio": "TODO encuentra el id del envío que corresponde",
            "entrega_mesa": None,
            "revision": None,
            "enviado_SS": None,
            "retorno_SS": None
        }
    })
    print(seed2)