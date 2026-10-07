'''
This are the objects needed to perform the tasks to analize WORD or EXCEL files and populate the data base

ESCUELA: Es el contenedor de los datos de la escuela o facultad que envía el archivo.
ALUMNO: Es cada uno de los elementos que son encontrados en el archivo enviado por la escuela o facultad.
'''
import regex 

class Escuela:
    def __init__(self, siglas: str, grado: str, carrera: str, fecha_envio: str, expedientes: list = []):
        self._siglas = siglas
        self._grado = grado
        self._carrera = carrera
        self._fecha_envio = fecha_envio
        self._expedientes = expedientes


    def __str__(self):
        return f'{self._siglas} envía {len(self._expedientes)} expedientes de {self._grado} en {self._carrera} en la fecha {self._fecha_envio}'


class Alumno:
    def __init__(self, CURP:str, primer_ap:str, segundo_ap:str, nombre: str, modalidad:str = ""):
        self._curp = CURP
        self._primer_ap = primer_ap
        self._segundo_ap = segundo_ap
        self._nombre = nombre
        self._modalidad = modalidad

    def __verify_curp__():
        if Alumno._curp.length < 10:
            print("CURP is not consistent with the official format, input the correct one.\n")
            Alumno._curp = input("Type the correct CURP: ")

    def __str__(self):
        return f'CURP: {self._curp}, Nombre: {self._nombre} {self._primer_ap} {self._segundo_ap}, Modalidad de Titulación: {self._modalidad}'