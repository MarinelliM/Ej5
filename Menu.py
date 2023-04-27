def menu(lista):
    print('1 - Actulaizar el valor de vehiculo de cada plan')
    print('2 - Mostrar informacion del vehiculo cuyo valor de la cuota sea inferior al ingresado')
    print('3 - Mostrar el monto que se debe haber pagado para licitar el vehículo')
    print('4 - Modificar la cantidad cuotas que debe tener pagas para licitar')
    print('0 - Salir')
    op = int(input('Ingrese la opcion a buscar:'))
    while op != 0:
        if op == 1:
            opcion1(lista)
        elif op == 2:
            opcion2(lista)
        elif op == 3:
            opcion3(lista)
        elif op == 4:
            opcion4(lista)
        else:
            print('Opcion incorrecta')
            op = int(input('Ingrese la opcion a buscar:'))
        print('1 - Actulaizar el valor de vehiculo de cada plan')
        print('2 - Mostrar informacion del vehiculo cuyo valor de la cuota sea inferior al ingresado')
        print('3 - Mostrar el monto que se debe haber pagado para licitar el vehículo')
        print('4 - Modificar la cantidad cuotas que debe tener pagas para licitar')
        print('0 - Salir')
        op = int(input('Ingrese la opcion a buscar:'))
    print('Fin del programa')

def opcion1(lista):
    for i in range(len(lista)):
        lista[i].mostrar()
        valor_actual = int(input('Ingrese el valor actual del vehiculo:'))
        lista[i].setvalorvehiculo(valor_actual)

def opcion2(lista):
    cuota = int(input('Ingrese un valor de cuota para buscar aquellas que son inferiores:'))
    i=0
    while i < len(lista):
        if lista[i].getvalorcuota() < cuota:
            lista[i].mostrar()
        else: i+=1

def opcion3(lista):
    for i in range(len(lista)):
        print('Para licitar el vehiculo {}, se debe haber pagado un monto de {} pesos'.format(lista[i].mostrar2(),lista[i].monto_para_licitar()))

def opcion4(lista):
    codigo = int(input('Ingrese el codigo del plan a buscar:'))
    cuota = int(input('Ingrese la nueva cantidad de cuotas que se debe tener pagas para licitar el vehiculo:'))
    i = 0
    while i < len(lista):
        if lista[i].getcodigoplan() == codigo:
            lista[i].setcantidadcuotaslicitar(cuota)
            print('La cantidad de cuotas a licitar se actualizo')
            print('Los datos del vehiculo actualizado son: valor de la cuota: {}, {}, {}'.format(lista[i].getvalorcuota(),lista[i].verPlanes(),lista[i].mostrar2())) 
            i = len(lista)
        else: i+=1
        codigo = int(input('No se encontro el vehiculo, porfavor ingrese de nuevo el codigo del plan:'))
        i=0
