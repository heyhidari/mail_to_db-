'''
This are the objects needed to perform the tasks to analize WORD or EXCEL files and populate the data base

ESCUELA: Es el contenedor de los datos de la escuela o facultad que envía el archivo.
ALUMNO: Es cada uno de los elementos que son encontrados en el archivo enviado por la escuela o facultad.
'''
import re

class Escuela:
    def __init__(self, siglas: str, grado: str, carrera: str, fecha_envio: str, num_exp: int, responsable: str):
        self._siglas = siglas
        self._grado = grado
        self._carrera = carrera
        self._fecha_envio = fecha_envio
        self._expedientes = num_exp
        self._responsable = responsable

    def __str__(self):
        return f'{self._siglas}, a través de {self._responsable} envía {self._expedientes} expedientes de {self._grado} en {self._carrera} en la fecha {self._fecha_envio}'

    # Verifica que los datos de la Unidad Académica sean correctos
    def is_sender_empty(self):
        for item in self.__dict__.items():
            if item[1] == "" or item[1] == None:
                self.__mod_sender()
            else:
                continue
        
        print("Los datos del remitente parecen ser correctos:")
        for item in self.__dict__.items():
            print(item[0], ": ", item[1])

    # Reescribe atributos si los datos de la Unidad Académica que envía son Nulos o Incorrectos
    def __mod_sender(self):
        if self._siglas == "" or self._siglas == None:
            self._siglas = input("Escriba la Unidad Académica que corresponda:\n")
        elif self._grado == "" or self._grado == None:
            self._grado = input("Escriba el grado académico que corresponda:\n")
        elif self._carrera == "" or self._carrera == None:
            self._carrera = input("Escriba la carrera que corresponda\n")
        elif self._fecha_envio == "" or self._fecha_envio == None:
            self._fecha_envio = input("Escriba la fecha de envío que corresponda (dd/mm/aaaa)\n")
        elif self._expedientes == "" or self._expedientes == None:
            self._expedientes = int(input("Escriba con número la cantidad de expedientes que corresponda\n"))
        elif self._responsable == "" or self._responsable == None:
            self._responsable = input("Escriba el nombre de la persona responsable del envío\n")
        else:
            raise Exception
            

class Alumno:
    def __init__(self, CURP:str, primer_ap:str, segundo_ap:str, nombre: str, modalidad:str = "", especialidad:str = ""):
        self._curp = CURP.strip()
        self._primer_ap = primer_ap.strip()
        self._segundo_ap = segundo_ap.strip()
        self._nombre = nombre.strip()
        self._modalidad = modalidad.strip()
        self._especialidad = especialidad.strip()

        self.__verify_curp__()
    
    def __str__(self):
        return f'CURP: {self._curp},\nNombre: {self._nombre} {self._primer_ap} {self._segundo_ap},\nModalidad de Titulación: {self._modalidad},\nEspecialidad: {self._especialidad}'

    def __verify_curp__(self):
        if len(self._curp) < 10:
            print("CURP is not consistent with the official format, input the correct one.\n")
            self._curp = input("Type the correct CURP: ")
        
        if re.match("[a-zA-z]{4}[0-9]{6}[hHmM][a-zA-Z]{5}..", self._curp):
            print("Valid\n", self)
        else:
            self._curp = input("Type the correct CURP: ")

    def is_alumn_empty(self):
        