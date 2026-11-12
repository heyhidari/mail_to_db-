'''
This are the objects needed to perform the tasks to analize WORD or EXCEL files and populate the data base

ESCUELA: Es el contenedor de los datos de la escuela o facultad que envía el archivo.
ALUMNO: Es cada uno de los elementos que son encontrados en el archivo enviado por la escuela o facultad.
'''
import re


class Escuela:
    def __init__(self, siglas: str, grado: str, carrera: str, fecha_envio: str, num_exp: int, responsable: str):
        # Variables que provienen de la lectura del Formato de Envío de Expedientes
        self._siglas = siglas
        self._grado = grado
        self._carrera = carrera
        self._fecha_envio = fecha_envio
        self._expedientes = num_exp
        self._responsable = responsable

        # Variables necesarias para crear un nuevo registro de Escuela
        self._edit_escuela_nombre = ""
        self._edit_escuela_siglas = ""
        self._edit_carrera_nombre = ""
        self._edit_carrera_grado = ""
        self._edit_carrera_mesaSG = ""

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
        try:
            if self._siglas == "" or self._siglas == None: self._siglas = input("Escriba la Unidad Académica que corresponda:\n")
            if self._grado == "" or self._grado == None: self._grado = input("Escriba el grado académico que corresponda:\n")
            if self._carrera == "" or self._carrera == None: self._carrera = input("Escriba la carrera que corresponda\n")
            if self._fecha_envio == "" or self._fecha_envio == None: self._fecha_envio = input("Escriba la fecha de envío que corresponda (dd/mm/aaaa)\n")
            if self._expedientes == "" or self._expedientes == None: self._expedientes = int(input("Escriba con número la cantidad de expedientes que corresponda\n"))
            if self._responsable == "" or self._responsable == None: self._responsable = input("Escriba el nombre de la persona responsable del envío\n")
        except Exception as e: print("Algo salió mal al ingresar los datos. Intenta de nuevo o revisa el siguiente problema:\n", e)

    # Busca datos existentes en la BD para no repetir y para poder vincular a través de _id's
    def data_integrity_and_validation(self, db: object):
        # Busca las siglas en las escuelas
        if not db.Escuelas.find_one({"siglas": {"$regex": self._siglas, "$options": "i"}}) is None:
            # Si no se encuentran las siglas, ingresa los datos de la escuela y la carrera en cuestión
            self._edit_escuela_nombre = input("Ingresa el nombre de la escuela:\n")                                             # Nombre de la Escuela
            self._edit_escuela_siglas = self._siglas                                                                            # Siglas reconocibles para la escuela
            self._edit_carrera_nombre = input(f'{"La carrera es:{self._carrera}, ¿estás de acuerdo? (y/n)"}')                   # Nombre de la carrera
            if not self._edit_carrera_nombre == "y": self._carrera = input("Ingresa el nombre de la carrera que corresponda")    
            self._edit_carrera_grado = input(f'{"El grado es:{self._grado}, ¿estás de acuerdo? (y/n)"}')                        # Grado de la carrera
            if not self._edit_carrera_grado == "y": self._grado = input("Ingresa el grado de la carrera que corresponda")
            self._edit_carrera_mesaSG = int(input(f'{"Ingresa el número de la mesa:\n"}'))                                      # Mesa de SG, buscar el id que corresponda
            with db.Mesas.find_one({"numero": self._edit_carrera_mesaSG}, {"nombre":0, "numero":0}) as mesa_cursor:
                self._edit_carrera_mesaSG = mesa_cursor
                




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
        if self._primer_ap is (None or ""):
            self._curp = input("Ingresa una curp correcta: ")
        elif self._segundo_ap is (None or ""):
            self._segundo_ap = input("Ingresa un segundo apellido, si no cuenta con uno presiona #")
        elif self._nombre is (None or ""):
            self._nombre = input("Ingresa el nombre")
        elif self._modalidad is (None or ""):
            self._modalidad = input("Ingresa la modalidad de titulación")
        

