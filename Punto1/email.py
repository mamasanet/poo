class Email():
    __idCuenta    =''
    __dominio     =''
    __extension   =''
    __contrasenia =''

    #Constructor de la clase email
    def __init__ (self, idCuenta = '', dominio ='', extension = '', contrasenia = ''):
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
    def crearCuenta(self, direccion):
        direccion          = direccion.split('@')
        self.__idCuenta    = direccion[0]
        direccion          = direccion[1].split('.')
        self.__dominio     = direccion[0]
        self.__extension   = direccion[1]
        self.__contrasenia = input('Ingrese password de {} :'.format(self.__idCuenta +'@'+ self.__dominio +'.'+self.__extension))
 