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
        self._edit_escuela_nombre = "na"
        self._edit_escuela_siglas = "na"
        self._edit_carrera_nombre = "na"
        self._edit_carrera_grado = "na"
        self._edit_carrera_mesaSG = "na"

    def __str__(self):
        return f'{self._siglas}, a través de {self._responsable} envía {self._expedientes} expedientes de {self._grado} en {self._carrera} en la fecha {self._fecha_envio}'

    # Verifica que los datos de la Unidad Académica sean correctos
    def is_sender_empty(self):
        required = ["_siglas", "_grado", "_carrera", "_fecha_envio", "_expedientes", "_responsable"]
        empty = False

        for attribute in required:
            value = getattr(self, attribute)
            if value == "" or value == None:
                self.__mod_sender(attribute)
                empty = True
            else:
                continue

        if empty == True:
            print("Los datos del remitente estaban incompletos, ahora son:")
            for attribute in required:
                print(f'{attribute}: {getattr(self, attribute)}')
            

        return empty
    

    # Reescribe atributos si los datos de la Unidad Académica que envía son Nulos o Incorrectos
    def __mod_sender(self, attribute_to_modify):
        try:
            value = input(f'Ingrese el valor de {attribute_to_modify}')
            self.__setattr__(attribute_to_modify, value)

        except Exception as e: print("Algo salió mal al ingresar los datos. Intenta de nuevo o revisa el siguiente problema:\n", e)
        else:
            return f'Se modificó {attribute_to_modify} con el valor: {value}'

    # Busca datos existentes en la BD para no repetir y para poder vincular a través de _id's
    def data_integrity_and_validation(self, db: object):
        print(f'Entering data_integrity_and_validation:')
        # Busca las siglas en las escuelas
        if db.escuelas.find_one({"siglas": {"$regex": self._siglas, "$options": "i"}}) is None:
            print(f'No hay coincidencias de escuela para "{self._siglas}"')

            # Si no se encuentran las siglas, ingresa los datos de la escuela y la carrera en cuestión
            self._edit_escuela_nombre = input("Ingresa el nombre de la escuela:\n")                              
            self._edit_escuela_siglas = self._siglas                                                             

            self._edit_carrera_nombre = input(f'La carrera es: {self._carrera}, ¿estás de acuerdo? (y/n)')       
            if not self._edit_carrera_nombre == "y": self._carrera = input("Ingresa el nombre de la carrera que corresponda\n") 
            ans = "n"   
            while ans != "y":
                ans = input(f'La carrera elegida es: {self._carrera}, ¿estás de acuerdo? (y/n)')
                if ans == "n": self._carrera = input("Ingresa el nombre de la carrera que corresponda\n")
            
            self._edit_carrera_grado = input(f'El grado es: {self._grado}, ¿estás de acuerdo? (y/n)')            
            if not self._edit_carrera_grado == "y": self._grado = input("Ingresa el grado de la carrera que corresponda\n")
            ans = "n"
            while ans != "y":
                ans = input(f'El grado elegido es: {self._grado}, ¿estás de acuerdo? (y/n)')
                if ans != "y": self._grado = input("Ingresa el grado de la carrera que corresponda\n")
            
            try:
                self._edit_carrera_mesaSG = int(input(f'Ingresa el número de la mesa:\n'))                           
            except Exception as e: print("La mesa debe ser un entero entre 3 y 13", e)
            else:
                self._edit_carrera_mesaSG = db.mesas.find_one({"numero": self._edit_carrera_mesaSG}, {"nombre":0, "numero":0}).get("_id")

            return f'Los datos ingresados son: {self._edit_escuela_siglas}, {self._edit_escuela_nombre}, {self._edit_carrera_nombre}, {self._edit_carrera_grado}, Mesa: {self._edit_carrera_mesaSG}'

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
        

