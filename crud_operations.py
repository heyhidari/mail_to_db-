"""
This file contains all the instructions necessary to perform CRUD Operations on the MongoDB Cluster. 
All of these are summoned through expedientes_db.py, so try to keep all logic within this file for better encapsulation.

This is the schema of the MongoDB Atlas UABJO Cluster. 
If changes are to be made to the DB, this part must be updated.

SCHEMA
==========
Alumni{
    CURP:           string, not null, PRIMARY_KEY                   # CURP del alumno, validado por re.match
    Apellido_1:     string, not null                                # Primer apellido
    Apellido_2:     string,                                         # Segundo apellido opcional
    Nombre:         string, not null                                # Nombre(s) del alumno
}

Estudios{
    id:             autonumber, not null, PRIMARY_KEY
    curp:           string, not null, foreign_key(Alumni)           # Un alumno puede tener varias carreras
    carrera:        int, not null, foreign_key(Carreras)            # Selecciona la carrera
    modalidad:      string, not null                                # Modalidad de Titulación ¿Crear tabla?
    envio:          int, not null, foreign_key(Envíos)              # Selecciona el id del envío
    entrega_mesa:   date                                            # Entregado a la mesa que corresponde en esta fecha
    revision:       string                                          # Descripción de problemas, si null, no hubo problema
    enviado_SS:     date                                            # Si enviado a Servicio Social, fecha
    retorno_SS:     date                                            # Regresado a la Secretaría General en esta fecha

}

Mesas{
    _id:            auto, not null, PRIMARY_KEY
    nombre:         string, not null                                # Nombre de la encargada de mesa
    numero:         int, not null                                   # Número de mesa
}

Escuelas{
    escuela_id:     autonumber, not null, PRIMARY_KEY
    Nombre:         string, not null, unique                        # Solo puede existir un único registro por escuela 
    Siglas:         string, not null                                # Se creará un string concatenando las variaciones, divididas por |, recuperar toda la cadena y verificar que haya compatibilidad.
}

Carreras{
    carrera_id:     autonumbre, not null, PRIMARY_KEY
    Nombre:         string, not null, unique                        # Solo puede haber un nombre de carrera, verificar variaciones
    grado:          int, not null, foreign_key(GradosAcademicos)    # Un grado por carrera, este par subsana las carreras que comparten nombre en otros grados
    mesaSG:         int, not null, foreign_key(Mesas)
    GradosAcademicos{
        grado_id:   autonumber, not null, PRIMARY_KEY
        Nombre:     string, not null, unique                        # Solo puede haber un nombre de grado
    }
}

Envíos{
    id:             autonumber, not null, PRIMARY_KEY
    Fecha:          datetime, not null                              # Fecha en que se hace el envío
    Cantidad:       int, not null                                   # Cantidad de expedientes que envía
    Escuela:        int, not null, foreign_ke(Escuelas)             # Escuela que hace el envío
    Responsables    {
        responsable_id: autonumber, not null, PRIMARY_KEY
        Nombre:         string, not null, unique                    # Solo puede existir un nombre, verificar las variaciones
        Telefono:       string, not null                            # Número telefónico de contacto
        Correo:         string, not null                            # Correo electrónico de contacto
        Escuela:        int, not null, foreign_key(Carreras)        # Un responsable por carrera, verificar que no se repitan
    }
}
    
====
"""
import pymongo
from db_connection import db

# This function inserts one student record, needs an alumno and Escuela
def student_insert_one(datos_alumno: dict):
    print("Inserting one record")
    return db.al


# this function inserts a bulk of students from a single Escuela
def student_insert_many():
    print("Inserting all records")


# This funtion inserts a new school to the DB
def escuela_insert_one():
    print("Inserting one school")


# This function inserts a new carrera
def carrera_insert_one():
    print("Inserting one carrera")


# This function inserts a new mesa
def mesa_insert_one():
    print("Inserting a new mesa")