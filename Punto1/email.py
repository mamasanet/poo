from validar import is_valid_email

class Email():
    __idCuenta    =''
    __dominio     =''
    __extension   =''
    __contrasenia =''

    #Constructor de la clase emaicambiarContraseniacambiarContrasenial
    def __init__ (self, idCuenta = '', dominio ='', extension = '', contrasenia = ' '):
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
    #Obtener Contrasenia
    def __getContrasenia(self):
        return self.__contrasenia
    #Modificar Contrasenia
    def __setContrasenia(self, contrasenia):
        self.__contrasenia = contrasenia
    #Cambiar contrasenia
    def cambiarContrasenia(self,contrasenia):
        if( contrasenia == self.__getContrasenia()):
            self.__setContrasenia(input("Ingrese la nueva clave: "))
        else:
            print("Las claves no coinciden.")
    #Crear Cuenta
    def crearCuenta(self, direccion):
        if(is_valid_email(direccion)):
            idCuenta, extension          = direccion.split('@')
            extension , dominio          = extension.split('.',1) 
            self.__init__(idCuenta, dominio, extension)
            self.__contrasenia = input('Ingrese password de {} :'.format(self.retornaEmail()))
            return True
        else:
            print("Email invalido")
            return False

