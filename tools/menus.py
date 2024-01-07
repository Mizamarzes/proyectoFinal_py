from tools.utils import *

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. Listar campers")
    print("3. Listar aprobados")
    print("4. Modificar campers")
    print("5. Salir")
    op=validar_opcion("Opcion: ",1,5)
    return op