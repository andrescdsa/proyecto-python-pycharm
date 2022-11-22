import utils.logging_hospital as log
import Clases as c


class Hospital:
    def __init__(self,nombre, consultas, sala_espera, enfermeros):
        self.nombre = nombre
        self.consultas = consultas
        self.sala_espera = sala_espera
        #estan vacias hasta que se le pasa el enfermo
        self.habitaciones = [None, None, None]
        self.enfermeros = enfermeros


    def inicio_hospital(self):
        log.debug("Iniciando el hospital")
        #Los empleados fichan
        self.fichar_empleados()

        #se atienden los pacientes
        while(self.hay_pacientes()):
            self.atender_pacientes_salaespera()
            self.atender_pacientes_consulta()

        #Fichan al salir
        self.fichar_empleados()

    def hay_pacientes(self):
        return len(self.sala_espera)>0

    def fichar_empleados(self):
        log.debug("Fichar doctores")
        for consulta in self.consultas:
            consulta.doctor.fichar()

        log.debug("Fichar enfermeros")
        for enfermero in self.enfermeros:
            enfermero.fichar()


    def atender_pacientes_consulta(self):
        for consulta in self.consultas:
            if(not consulta.paciente == None):
                enfermo = consulta.doctor.tratar_paciente(consulta.paciente)
                if(not enfermo == None):
                    self.asignar_enfermo_habitacion(enfermo)
                else:
                    log.info("el paciente {} se ha despedido".format(consulta.paciente.nombre))

            consulta.paciente = None

    def asignar_enfermo_habitacion(self, enfermo_registrado):

        habitacion_asignada = False
        for habitacion, enfermo in enumerate(self.habitaciones):
            if enfermo == None:
                self.habitaciones[habitacion] = enfermo_registrado
                log.info("Enfermo {} esta en la habitacion {}".format(enfermo_registrado.nombre, habitacion))
                habitacion_asignada = True
                break

        if (not habitacion_asignada):
            log.warn("No ha habitaciones disponibles")

    def atender_pacientes_salaespera(self):
        for enfermero in self.enfermeros:
            paciente = self.obtener_paciente()
            consulta = self.obtener_consulta_libre()
            if not paciente == None and not consulta == None:
                enfermero.atiende_paciente(paciente, consulta)

    def obtener_paciente(self):
        paciente = None
        if(len(self.sala_espera)>0):
            ##coge el paciente de sala de espera
            paciente = self.sala_espera.pop(0)

        return paciente

    def obtener_consulta_libre(self):
        for consulta in self.consultas:
            if(consulta.paciente==None):
                return consulta

        return None


if __name__ == '__main__':

    doctor1 = c.doctor("Juan","Perez", "091273516x", "Cirujia")
    doctor2 = c.doctor("Maria", "Martin", "091271236x", "Pediatria")

    consulta1 = c.Consulta("consulta 1", doctor1)
    consulta2 = c.Consulta("consulta 2", doctor2)

    listado_consultas = [consulta1,consulta2]

    paciente1 = c.Paciente("Luis", "Mejia", "123123d", ["Dolor oido","mocos"])
    paciente2 = c.Paciente("Juan", "Medina", "12678693d", ["Dolor oido", "mocos"])
    paciente3 = c.Paciente("Jenny", "Me", "1212318693d", ["Dolor oido", "mocos"])
    paciente4 = c.Paciente("Isabel", "Guzman", "1290763d", ["Dolor oido", "mocos"])

    sala_de_espera = [paciente1,paciente2,paciente3,paciente4]

    enfermero1 = c.Enfermero("David","Muñoz","12351526D","planta1")
    enfermero2 = c.Enfermero("Luisa","Perez","12355626D","planta2")

    listado_enfermeros = [enfermero1,enfermero2]

    hospital = Hospital("Hospital 1",listado_consultas,sala_de_espera,listado_enfermeros)
    hospital.inicio_hospital()