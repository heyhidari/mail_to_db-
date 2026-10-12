'''
This are the objects needed to perform the tasks to analize WORD or EXCEL files and populate the data base

ESCUELA: Es el contenedor de los datos de la escuela o facultad que envía el archivo.
ALUMNO: Es cada uno de los elementos que son encontrados en el archivo enviado por la escuela o facultad.
'''
import regex 

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
        for attr in vars(self):
            if not attr.startswith("__"):
                """
                TODO
                This part should loop through the attributes of Escuela and determine if they are empty
                If so, call __mod_sender
                
                print(callable(attr))
                print(getattr(attr))
                """

    # Reescribe atributos si los datos de la Unidad Académica que envía son Nulos o Incorrectos
    def __mod_sender(self):
        if self._siglas == "":
            self._siglas = input("Escriba la Unidad Académica que corresponda")
        elif self._grado == "":
            self._grado = input("Escriba el grado académico que corresponda")
        elif self._carrera == "":
            self._carrera = input("Escriba la carrera que corresponda")
        elif self._fecha_envio == "":
            self._fecha_envio = input("Escriba la fecha de envío que corresponda (dd/mm/aaaa)")
        elif self._expedientes == "":
            self._expedientes = int(input("Escriba con número la cantidad de expedientes que corresponda"))
        elif self._responsable == "":
            self._responsable = input("Escriba el nombre de la persona responsable del envío")
        else:
            raise Exception
        
            

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