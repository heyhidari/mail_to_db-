'''
Versión 1
Este programa lee los correos que envían las facultades previo a la entrega de expedientes profesionales 
y envía los datos a una base de datos MongoDB.

file_name:: El formato de nombre

POR MEJORAR:
- Buscar compatibilidad de bases de datos entre esta y Access (Ver Profesionales_1.bddb).
- Asegurar que la ruta de archivos sea válida, por ahora sólo se busca y envía un error a posteriori.
'''
import helper_objects as obj
import helper_functions as func
import readxl as xl
import readwd as wd

from sys import argv


def main():
    print("TEST Running")
    folder_root = "/Users/hidari/Downloads/"
    # Read argv values
    if len(argv) < 2:
        print("Intenta de nuevo, incluye el nombre del archivo. DEBE ESTAR EN LA CARPETA DOWNLOADS")
        return

    # Analize the file type
    file_name = folder_root + argv[1]
    extension = file_name.rsplit(".",2)

    if extension[1] not in ["xlsm", "xlsb"]:
        print(extension, "Este archivo no es compatible conmigo, revísalo.")
        return
    else:
        print("File is correct")
    
    # Analize file name format in case we can retrieve data from here
    file_name_format = argv[1].split('_')
    fac = ""
    gdo = ""
    carr = ""
    fec = ""

    if len(file_name_format) < 4:
        print("Este archivo tiene errores en el formato del nombre. Notificar al remitente.")
        return
    else:
        fac = file_name_format[0]
        gdo = file_name_format[1]
        carr = file_name_format[2]
        fec = file_name_format[3].strip(extension[1]).strip(".")

        print(fac, gdo, carr, fec)

    # Open file
    print("Opening file")
    archivo = xl.wb(file_name)
    hoja1 = archivo["Hoja1"]

    # Iterate data sent from Escuela (iter_rows gets data as a single value tuple)
    data_from_sender = []
    for cell in hoja1.iter_rows(min_row=2, min_col=10, max_row=6, max_col=10, values_only=True):
        data_from_sender.append(cell[0])

    sender = obj.Escuela(
        siglas="",
        grado=data_from_sender[4],
        carrera="",
        fecha_envio=data_from_sender[3],
        num_exp=data_from_sender[2],
        responsable=data_from_sender[1])

    # Check up for empty values in the sender, (TBD correct and continue)
    sender.is_sender_empty()

    print(" testing helper_functions")
    print(" end_testing helper_functions")

    # Check the 
    print("Closing file")
    archivo.close()

    print("TEST END")
    return

    if len(file_name_format) < 3 or len(file_name_format) > 4:
        print("El formato del nombre de archivo no es adecuado para realizar esta operación")
        # TODO: Abrir módulo cambiar nombre
        """
        Módulo para cambiar nombre del archivo a algo que sea compatible con:

        Facultad_Grado_Carrera_Fecha

        De esta manera se asegura que todos los archivos sean compatibles con este nombre
        Sin embargo, queda pendiente limitar las opciones al Formato Digital, es decir,
        falta excluir los archivos que no son de excel 
        """
    else:
        print('Processing file')

    

if __name__ == '__main__':
    main()