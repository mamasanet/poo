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
        if( contrasenia == self.__getContrasenia):
            self.__setContrasenia(input("Ingrese la nueva clave: "))
        else:
            print("Las claves no coinciden.")
    #Crear Cuenta
    def crearCuenta(self, direccion):
        direccion          = direccion.split('@')
        idCuenta           = direccion[0] #id cuenta
        extension          = direccion[1].split('.') 
        dominio            = extension[0] #dominio
        extension          = extension[1] #extension
        self.__init__(idCuenta, dominio, extension)
        self.__contrasenia = input('Ingrese password de {} :'.format(self.__idCuenta +'@'+ self.__dominio +'.'+self.__extension))