import problema1
from alumnos import alumnos

'''
tres comillas sirven para comentar
varias lineas
dentro de las comillas
'''

edad = 12
altura = 1.79
nombre = "Juan"
estado = True

'''
en Python podemos usar una
variable que almacena
una coleccion de datos
y luego accederla usando un subindice
'''

# lista de enteros
lista1 = [10, 5, 3, 9]
# lista de decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 3.45]
# lista de string
lista3 = ["lunes","martes","miercoles"]

'''
lista de elementos
de diferente tipo
'''
lista4 = ["Juan",45,1.92,False]

if __name__ == '__main__':
    '''
    cantidad de elementos de cada lista:
    '''

    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0] = 1
    print()
    print(lista1)

    print(lista1[3])

    print()

    problema1.sumar_5_enteros()

    print()

    alumnos()