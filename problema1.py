def sumar_5_enteros():
    # definicio de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # ingreso los numeros
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese numero " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # sumamos los numeros
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=' ')

    print("\nla suma de todos los elementos es:")
    print(suma)