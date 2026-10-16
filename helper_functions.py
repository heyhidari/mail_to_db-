import helper_objects as obj

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
    

