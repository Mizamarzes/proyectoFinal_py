from tools.utils import *

#-------------------------------------------------------------
# menu principal

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Rutas")
    print("6. Reportes")
    print("7. Salir")       
    op=validar_opcion("Opcion: ",1,7)
    return op

#----------------------------------------------------------------
# menus secundarios

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. Buscar campers")
    print("3. Modificar camper")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_trainers():
    print("----------- Menú Trainers-----------")
    print("1. Agregar Trainer")
    print("2. Mostrar Trainers")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_matriculas():
    print("----------- Menú Matriculas-----------")
    print("1. Matricular camper")
    print("2. Salir")
    op=validar_opcion("Opcion: ",1,2)
    return op

def menu_aulas():
    print("----------- Menú Aulas-----------")
    print("1. Mostrar Aulas")
    print("2. Salir")
    op=validar_opcion("Opcion: ",1,2)
    return op

def menu_rutas():
    print("----------- Menú Rutas-----")
    print("1. Agregar ruta")
    print("2. Mostrar rutas")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_reportes():
    print("---------------------------Menú Reportes------------------------")
    print("1. Listar campers inscritos")
    print("2. Listar campers aprobados(examen admision)")
    print("3. Listar trainers")
    print("4. Listar campers y entenador asociados a una ruta de entrenamiento")
    print("5. Listar campers en riesgo")
    print("6. Listar campers en linea o aprobados")
    print("7. Salir")
    op=validar_opcion("Opcion: ",1,7)
    return op

#-----------------------------------------------------------------



