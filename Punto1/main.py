import csv
import email as E

def punto4(lista):
    archivo     = open('/home/andy/Escritorio/git/poo/Punto1/direccionesgmail.csv')
    reader      = csv.reader(archivo, delimiter = ';')

    auxiliar    = E.Email()

    for fila in reader :

        if (auxiliar.crearCuenta(fila[0])):
            lista.append(auxiliar)
        else:
            print("Email invalido")            

    print(lista)

if __name__ == "__main__":
    print('Ingrese los siguientes datos:')
    nombre      = input('nombre: ')
    direccion   = input('direccion email: ')
    email       = E.Email()
    email.crearCuenta(direccion)
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, direccion))
    email.cambiarContrasenia(input("Ingrese su clave para comenzar con el cambio de pass: "))
    otroemail   = E.Email()

    listaEmails = []
    punto4(listaEmails)
