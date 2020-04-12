import csv
import email as E

def punto4(lista):
    archivo     = open('/home/andy/Escritorio/git/poo/Punto1/direccionesgmail.csv')
    reader      = csv.reader(archivo, delimiter = ';')
    auxiliar    = E.Email()
    i           = 0

    for fila in reader :

        if (auxiliar.crearCuenta(fila[0],fila[1])):
            lista.append(E.Email())
            lista[i].crearCuenta(fila[0],fila[1])
            i+=1
        else:
            print("Email invalido")

    archivo.close()
    dominio     = input("Ingrese el dominio a buscar:")

    i           = 0

    for email in lista :
        
        if(email.getDominio() == dominio):
            i+=1

    print("Se han encontrado {} emails con el dominio {}".format( i, dominio))
    
if __name__ == "__main__":


    listaEmails = []
    punto4(listaEmails)
