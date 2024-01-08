from process.campers_register import * 
from process.rutas import *
from process.trainers import *
from process.areas_entrenamiento import *
from tools.menus import *
from tools.utils import *

#-----------------------------------------------------------------------------------
# funciones de control secundarias

def manejar_campers():
    limpiar_pantalla() # limpia pantalla
    suboption=menu_campers()
    if suboption==1:
        inscribir_camper()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==2:
        mostrar_objecto_lista("inscritos.json")
        input("Click cualquier tecla [continuar]: ")
    elif suboption==3:
        mostrar_objecto_lista("aprobados.json")
        input("Click cualquier tecla [continuar]: ")
    elif suboption==4:
        modificar_camper()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==5:
        print()

def rutas():
    limpiar_pantalla()
    suboption=menu_rutas()
    if suboption==1:
        crear_nueva_ruta()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==2:
        mostrar_objecto_lista("rutas.json")
        input("Click cualquier tecla [continuar]: ")
    elif suboption==3:
        print()

def trainers():
    limpiar_pantalla()
    suboption=menu_trainers()
    if suboption==1:
        crear_trainers()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==2:
        mostrar_objecto_lista("trainers.json")
        input("Click cualquier tecla [continuar]: ")
    elif suboption==3:
        print()

#--------------------------------------------------------------------------------------------------
limpiar_json("inscritos.json")
limpiar_json("aprobados.json")
limpiar_json("areas.json")
generar_list()   # genera la lista de estudiantes de forma alelatoria y lista de aprobados tambien
generar_area_entrenamiento() # genera los salones con sus respectivos trainers y demas
#-------------------------------------------------------------------------------------------------

# zona controladora principal

while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        manejar_campers()
    elif op==2:
        trainers()
    elif op==3:
        rutas()
    elif op==4:
        print("Gracias por utilizar nuestro servicio")
        break