##Clase Hospital.
class Hospital(doctor, enfermero, consultas, habitacion={}, sala_espera):
    def __init__(self, doctor, enfermero, consultas, habitacion, sala_espera):
        self.doctor = doctor
        self.enfermero = enfermero
        self.consultas = consultas
        self.habitacion = habitacion
        self.sala_espera = sala_espera


##Clase persona: con nombre apellido.
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "Se llama {} {}".format(self.nombre, self.apellido)


##Clase doctor que hereda de persona el nombre y apellido
import random


class Doctor(Persona):
    def __init__(self, especialidad, nombre, apellido):
        Persona.__init__(self, nombre, apellido)
        self.especialidad = especialidad

    def __str__(self):
        return "El doctor se llama {} {} y su especialidad es {}".format(self.especialidad, self.nombre, self.apellido)

    def diagnosticar(self, paciente):
        print("El doctor " + self.nombre + " esta atendiendo al paciente " + paciente.nombre)
        num = random.randrange(1, 10)
        print(num)
        # El paciente esta grave y entra en habitación
        enfermedades = ["Covid", "Cancer", "Rotura"]
        if (num > 7):
            paciente.enfermedad = random.choice(enfermedades)
            print(
                "El paciente " + paciente.nombre + " tiene " + paciente.enfermedad + ". Se le ingresa en una habitación")

        else:
            print("El paciente " + paciente.nombre + " no esta grave")
            print("No se le traslada a ninguna habitación")


##Clase enfermero que hereda de persona el nombre y apellido
class Enfermero(Persona):
    def __init__(self, planta, nombre, apellido):
        Persona.__init__(self, nombre, apellido)
        self.planta = planta

    def __str__(self):
        return "El enfermero se llama {} {} y esta en la planta {}".format(self.planta, self.nombre, self.apellido)


##Clase paciente que hereda de persona el nombre y apellido
class Paciente(Persona):
    def __init__(self, sintoma, nombre, apellido):
        Persona.__init__(self, nombre, apellido)
        self.sintoma = sintoma

    def __str__(self):
        return "El paciente se llama {} {} y el sintoma que tiene es {}".format(self.sintoma, self.nombre,
                                                                                self.apellido)


##Clase enfermo que hereda de paciente los sintomas
class Enfermo(Paciente):
    def __init__(self, enfermedad, sintoma, nombre, apellido):
        Paciente.__init__(self, enfermedad, sintoma, nombre, apellido)
        self.enfermedad = enfermedad

    def __str__(self):
        return "El enfermo se llama {} {}, el sintoma es {} y la enfermedad es {}".format(self.enfermedad, self.sintoma,
                                                                                          self.nombre, self.apellido)
