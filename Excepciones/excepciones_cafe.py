class TemperaturaException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje

class CalienteTemperaturaException(TemperaturaException):

    def __init__(self, mensaje):
        TemperaturaException.__init__(self, mensaje=mensaje)


class FrioTemperaturaException(TemperaturaException):

    def __init__(self, mensaje):
        TemperaturaException.__init__(self, mensaje=mensaje)