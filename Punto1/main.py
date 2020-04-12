import email as E
if __name__ == "__main__":
    print('Ingrese los siguientes datos:')
    nombre=input('nombre: ')
    direccion= input('direccion email: ')
    email = E.Email()
    print(email.crearCuenta(direccion))
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, direccion))
    email.cambiarContrasenia(input("Ingrese su clave para comenzar con el cambio de pass: "))
