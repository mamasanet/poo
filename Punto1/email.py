class Email():
    __idCuenta    =''
    __dominio     =''
    __extension   =''
    __contrasenia =''

    #Constructor de la clase emaicambiarContraseniacambiarContrasenial
    def __init__ (self, idCuenta = '', dominio ='', extension = '', contrasenia = ''):
        pass
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
        self.__idCuenta    = direccion[0]
        direccion          = direccion[1].split('.')
        self.__dominio     = direccion[0]
        self.__extension   = direccion[1]
        self.__contrasenia = input('Ingrese password de {} :'.format(self.__idCuenta +'@'+ self.__dominio +'.'+self.__extension))
 