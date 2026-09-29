# Pseudocode to extract students and add them to a SQLite DB

## Main
1. Ingresar el archivo para integrar los nombres a la BD (¿formatos permitidos? WORD [docx, doc] , EXCEL [xlsm, xlsx, xls])
2. Verificar el nombre del archivo que cumpla con el formato (separado por guion bajo):
    - siglas de la facultad
    - grado académico
    - nombre de carrera
    - fecha de envío de correo
3. si no cumple con estos requisitos levantar un mensaje de que no está bien formateado y permitir reescribirlo (Módulo Reescribir FileName)
4. si cumple con los requisitos de nombre, construir un contenedor para los datos (objeto de escuela) y heredarlo a la llamada al módulo que corresponda más abajo
5. analizar el formato, si es parte o no del formato de envío de expedientes profesionales ¿cómo? todos tienen una tabla secundaria en la segunda hoja que no es visible.
6. si WORD ver Módulo Lectura de Word si no, next
7. si EXCEL ver Módulo Lectura de Excel.
8. Terminar la extracción y mostrar los registros que serán añadidos en un resumen (Módulo Resumen)
9. Añadir a la BD.
10. Cerrar archivo de lectura.
11. ¿Desea ingresar otro archivo? 
    Sí => Ir a 1
    No => Cerrar programa

## Módulo Word
1. Parse content: dependiendo de la escuela, pedir homologar los formatos en tabla con los encabezados NOMBRE, PRIMER APELLIDO, SEGUNDO APELLIDO, CURP.
2. Cuando encuentre una CURP (regex CURP), copiar y crear un objeto ALUMNO.
3. Buscar nombre, que corresponda a las 4 primeras letras de la CURP en un 75% (Verificar los casos donde se cambian por X)
4. Crear una lista y añadir el alumno. 
5. Parse donde encontró la CURP y Nombre si se verificó. Buscar otra CURP, ir a 2.
6. EOF:`return` Lista de ALUMNOs a ESCUELA['expedientes'].

## Módulo Excel
1. Este archivo debe ser uno de los enviados através del 'Formato de envío de expedientes profesionales', si no, insertar manualmente hasta siguiente versión.
2. El formato es:
    ESCUELA se alimenta del nombre del archivo así como de J[2: 6]
    Fila 19 encabezados (B: CURP, D: Primer Apellido, F: Segundo Apellido, H: Nombre(s), J: Modalidad de titulación)
3. For fila 20 to EOF
    Si not EOF
    Crear ALUMNO por fila 
    Append a lista
4. EOF: `return` Lista de ALUMNOS a ESCUELA['expedientes']


## Módulo Resumen
1. Muestra el contenido de la lista ESCUELA en un formato legible
2. Preguntar Si está de acuerdo con el contenido:
    `return` `true`  o `false`

## Módulo Reescribir FileName
1. Función reescribir nombre (nombre original del archivo)
2. Crear objeto ESCUELA con los datos pertinente (prompt user for it)
3. Cierra el archivo y reescribe el nombre con el formato predeterminado usando las propiedades de ESCUELA
4. Salir

### OBJETOS
ALUMNO[Nombre, Primer Apellido, Segundo Apellido, CURP, Carrera, Modalidad de titulación]
ESCUELA[siglas, grado, carrera, fecha de envio: , expedientes: lista de objetos]
