"""
Functions to manipulate files.

This functions allow to interact with the files, such as to modify their name. 

TODO:
Migrate as many fuctions as possible from main to craete a more readable program.
"""

# Function to modify the name of a file.
def file_name_mod(filename: str):
    # Get the file extension
    extension = filename.rsplit(".",2)

    # Ingresa los campos necesarios para modificar el nombre del archivo
    facultad = input("Ingrese el código de la Facultad:\n")
    grado = input("Ingresa el grado que se estará recibiendo:\n")
    carrera = input("Ingresa la carrera que corresponde:\n")
    fecha = input("Ingresa la fecha en que se envía el archivo (ddmesaaaa)")

    # Regresa el formato correcto para el nombre
    return f'{facultad}_{grado}_{carrera}_{fecha}.{extension}'
    

# Function to extract all variations of acronyms
def acronym_extraction(acronyms: str):    
    # Split and return acronyms string separated by |
    return acronyms.strip.split("|")
