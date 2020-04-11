class Email():
    __idCuenta =''
    __dominio =''
    __extension =''
    __contrasenia =''

#Constructor de la clase email
    def __init__ (self, idCuenta,dominio, extension, contrasenia):
        self.__idCuenta    = idCuenta
        self.__dominio     = dominio
        self.__extension   = extension
        self.__contrasenia = contrasenia
#Obtener Dominio del objeto
    def getDominio(self):
        return self.__dominio
#Retornar Email
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + self.__extension
#Crear Cuenta
