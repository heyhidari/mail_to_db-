"""
This file contains all the instructions necessary to perform CRUD Operations on the MongoDB Cluster.
This is the schema of the MongoDB Atlas UABJO Cluster. 
If changes are to be made to the DB, this part must be updated.

SCHEMA
==========
Alumni{
    CURP:           string, not null, primary_key
    Apellido_1:     string, not null
    Apellido_2:     string, not null
    Nombre:         string, not null
    }

Estudios{
    id:             autonumber, not null, primary_key
    curp:           string, not null, foreign_key(Alumni)           # Un alumno puede tener varias carreras
    carrera:        int, not null, foreign_key(Carreras)            # Selecciona la carrera
    modalidad:      string, not null                                # Modalidad de Titulación ¿Crear tabla?
    envio:          int, not null, foreign_key(Envíos)              # Selecciona el id del envío
}

Escuelas{
    escuela_id:     autonumber, not null, primary_key
    Nombre:         string, not null, unique                        # Solo puede existir un único registro por escuela 
}

SiglasEscuelas{
    siglas_id:      autonumber, not null, primary_key
    Siglas:         string, not null, unique                        # Solo puede existir un único registro de variación de siglas
    Escuela:        int, not null, foreign_key(Escuela)             # Unas siglas solo corresponden a una escuela
}

Responsables{
    responsable_id: autonumber, not null, primary_key
    Nombre:         string, not null, unique                        # Solo puede existir un nombre, verificar las variaciones
    Telefono:       string, not null                                # Número telefónico de contacto
    Correo:         string, not null                                # Correo electrónico de contacto
    Escuela:        int, not null, foreign_key(Carreras)            # Un responsable por carrera, verificar que no se repitan
}

GradosAcademicos{
    grado_id:       autonumber, not null, primary_key
    Nombre:         string, not null, unique                        # Solo puede haber un nombre de grado
}

Carreras{
    carrera_id:     autonumbre, not null, primary_key
    Nombre:         string, not null, unique                        # Solo puede haber un nombre de carrera, verificar variaciones
    grado:          int, not null, foreign_key(GradosAcademicos)    # Un grado por carrera, este par subsana las carreras que comparten nombre en otros grados
}

Envíos{
    id:             autonumber, not null, primary_key
    Fecha:          datetime, not null                              # Fecha en que se hace el envío
    Cantidad:       int, not null                                   # Cantidad de expedientes que envía
    Escuela:        int, not null, foreign_ke(Escuelas)             # Escuela que hace el envío
    Responsable:    int, not null, foregin_key(Responsables)        # Responsable que envía
}
    
====
"""
import pymongo
