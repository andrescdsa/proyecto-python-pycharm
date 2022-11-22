##Importar util para los logs de hospital
import datetime

import utils.loggin_hospital as log
##Importar abc para usar las clases abstractas y el metodo abstracto
from abc import ABC, abstractmethod
##Importa la funcion random para generar numero random
import random
##Importa la lista de enfermedades de utils_hospital
import utils.utils_hospital as util
##Importa de general_utils la funcion de generar un booleano aleatorio
from utils.general_utils import generar_aleatorio_booleano


##Clase abstracta persona: con nombre apellido.
class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return "Se llama {} {} con dni: {}".format(self.nombre, self.apellido, self.dni)


class Enfermo(Persona):
    def __init__(self, nombre, apellido, dni, enfermedad):
        super().__init__(nombre=nombre, apellido=apellido, dni=dni)
        self.enfermedad = enfermedad


class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, sintoma=[]):
        super().__init__(nombre=nombre, apellido=apellido, dni=dni)
        self.sintoma = sintoma


##Hereda de persona, de ABC para hacer una función abstracta para que la usen doctor y enfermero
class Empleado(Persona, ABC):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.ultimo_fichaje = None
        self.servicio = False

    @abstractmethod
    def fichar(self):
        pass


class Doctor(Empleado):
    def __init__(self, nombre, apellido, dni, especialidad):
        super().__init__(nombre, apellido, dni)
        self.especialidad = especialidad

    ##Metodo de fichar doctor en el que envia un log con la fecha y hora/minuto/segundo de cuando ficha el doctor
    def fichar(self):
        dt = datetime.datetime.now()
        self.ultimo_fichaje = dt
        ##No esta en servicio
        self.servicio = not self.servicio
        log.info("El doctor {} ha fichado el dia {}/{}/{} {}:{}:{}".format(self.nombre, self.ultimo_fichaje.day,
                                                                           self.ultimo_fichaje.month,
                                                                           self.ultimo_fichaje.year,
                                                                           self.ultimo_fichaje.hour,
                                                                           self.ultimo_fichaje.minute,
                                                                           self.ultimo_fichaje.second))

    def tratar_paciente(self, paciente):
        log.info("El doctor {} trata al paciente {}".format(self.nombre, paciente.nombre))
        paciente_esta_enfermo = generar_aleatorio_booleano(0)
        enfermedad = random.choice(util.ENFERMEDADES)

        if (paciente_esta_enfermo):
            log.warn("El paciente {} esta enfermo de {}".format(paciente.nombre, enfermedad))
            enfermo = Enfermo(paciente.nombre, paciente.apellidos, paciente.dni, enfermedad)
            return enfermo
        else:
            log.info("El paciente {} esta sano, se le manda a casa".format(paciente.nombre))
            return None


class Enfermero(Empleado):

    def __init__(self, nombre, apellido, dni, planta):
        super().__init__(nombre, apellido, dni)
        self.planta = planta

    def fichar(self):
        dt = datetime.datetime.now()
        self.ultimo_fichaje = dt
        ##No esta en servicio
        self.servicio = not self.servicio
        log.info("El enfermero/a {} ha fichado el dia {}/{}/{} {}:{}:{}".format(self.nombre, self.ultimo_fichaje.day,
                                                                                self.ultimo_fichaje.month,
                                                                                self.ultimo_fichaje.year,
                                                                                self.ultimo_fichaje.hour,
                                                                                self.ultimo_fichaje.minute,
                                                                                self.ultimo_fichaje.second))

    def atiende_paciente(self, paciente, consulta):
        log.info("El enfermero {} asigna el paciente {} a la consulta {}".format(self.nombre, paciente.nombre
                                                                                 , consulta.nombre))


class Consulta:
    def __init__(self, nombre, doctor):
        self.nombre = nombre
        self.doctor = doctor
        ##Al principio no tiene paciente hasta que el enfermero asigna el paciente a la consuilta
        self.paciente = None
