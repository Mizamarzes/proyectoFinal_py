from tools.utils import *

#-------------------------------------------------------------
# menu principal

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Rutas")
    print("4. Salir")       
    op=validar_opcion("Opcion: ",1,4)
    return op

#----------------------------------------------------------------
# menus secundarios

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. Listar campers pre-prueba-admision")
    print("3. Listar aprobados")
    print("4. Modificar campers")
    print("5. Salir")
    op=validar_opcion("Opcion: ",1,5)
    return op

def menu_rutas():
    print("----------- Menú Rutas-----------")
    print("1. Agregar ruta")
    print("2. Mostrar rutas")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_trainers():
    print("----------- Menú Modificar-----------")
    print("1. Agregar Trainer")
    print("2. Mostrar Trainers")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

#-----------------------------------------------------------------
# menus terciarios

def menu_modificar():
    print("----------- Menú Modificar-----------")
    print("1. Modificar estado camper")
    print("2. Salir")
    op=validar_opcion("Opcion: ",1,2)
    return op
