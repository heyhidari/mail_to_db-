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
import readxl
import readwd

from sys import argv


def main():
    print("Running")
    # Read argv values
    if len(argv) < 2:
        print("Intenta de nuevo, agrega la ruta del archivo que será agregado a la base de datos")
        return

    # Analize the file name format
    file_name = argv[1]
    file_name_format = file_name.split('_')
    
    if len(file_name_format) < 3:
        print("El formato del nombre de archivo no es adecuado para realizar esta operación")
        
        # TODO: Abrir módulo cambiar nombre
    else:
        print('Processing file')

    

if __name__ == '__main__':
    main()