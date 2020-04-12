#def inciso1():
    #print('ingrese los siguientes datos:')
    #nombre=input('nombre:')
    #direccion= input('direccion email:')
    #print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, direccion))
#    pass
from email import Email
if __name__ == "__main__":
    print('ingrese los siguientes datos:')
    nombre=input('nombre: ')
    direccion= input('direccion email: ')
    email = Email()
    print(email.crearCuenta(direccion))
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, direccion))