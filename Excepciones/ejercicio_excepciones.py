import random
from excepciones_cafe import  TemperaturaException, FrioTemperaturaException, CalienteTemperaturaException
from abc import ABC
import logging as log

log.basicConfig(filename='logs/bar.log', encoding='utf-8', level=log.DEBUG)

class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre


class TazaCafe:
    def __init__(self, temperatura, tipo_cafe):
        self.temperatura = temperatura
        self.tipo_cafe = tipo_cafe

class Camarero(Persona):
    ##No haria falta el __init__ ya que es igual que al del padre
    ##def __init__(self, nombre):
        ##super().__init__(nombre)

    def servir_taza(self):
        log.info("El camarero esta sirviendo el cafe")
        temperatura = random.randint(0,100)
        tipo_cafe = ["cafe solo", "cafe con leche", "Descafeinado", "Expresso"]
        cafe = random.choice(tipo_cafe)
        log.info("La taza de cafe esta a {} y es de {}".format(temperatura, cafe))
        taza_cafe = TazaCafe(temperatura, cafe)
        return taza_cafe



class Cliente(Persona):
    ##No haria falta el __init__ ya que es igual que al del padre
    ##def __init__(self, nombre):
        ##super().__init__(self,nombre = nombre)

    def tomar_cafe(self, TazaCafe):
        log.info("El cliente {} se ha tomado una taza de {} ".format(self.nombre,TazaCafe.tipo_cafe))
        ##Tirar la excepciones
        if TazaCafe.temperatura > 80:
            raise CalienteTemperaturaException("El cliente se ha quemado la lengua")
        elif TazaCafe.temperatura < 20:
            raise FrioTemperaturaException("El cliente protesta porque el café esta frio")



class Bar:
    def __init__(self, camarero):
        self.camarero = camarero

    def atender_cliente(self, cliente):
        taza_cafe = self.camarero.servir_taza()
        try:
            cliente.tomar_cafe(taza_cafe)
        except FrioTemperaturaException as frio:
            log.error(frio.message)
            log.error("El camarero le calienta un poco el café")
        except CalienteTemperaturaException as caliente:
            log.error(caliente.message)
            log.error("El camarero le enfría un poco el café")
        except Exception as e:
            log.error("El cliente se queja de algo")
        else:
            log.info("El cliente {} se ha tomado la taza".format(cliente.nombre))


if __name__ == "__main__":

    cliente = Cliente("Juan")
    camarero = Camarero("Pepe")
    bar = Bar(camarero)
    bar.atender_cliente(cliente)