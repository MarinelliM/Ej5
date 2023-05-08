from PlanAhorro import PlanAhorro
import csv
from Menu import menu
#def test():
    
if __name__ == '__main__':
    lista = []
    archivo=open('Ej5.csv')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)
    for fila in reader:
        plan = PlanAhorro(int(fila[0]),fila[1],fila[2],int(fila[3]))
        plan.setcantidadcuotasplan(int(fila[4]))
        plan.setcantidadcuotaslicitar(int(fila[5]))
        lista.append(plan)
    # for i in range(len(lista)):
    #     lista[i].mostrar()
    menu(lista)
