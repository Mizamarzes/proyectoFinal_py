from process.campers_register import * 
from process.rutas import *
from tools.menus import *
from tools.utils import *

generar_list()     # genera la lista de estudiantes de forma alelatoria
generar_lista_aprobados() # genera lista de campers que aprobaron la prueba de admision

def manejar_campers():
	# limpia pantalla
    suboption=menu_campers()
    if suboption==1:
        inscribir_camper()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==2:
        mostrar_campers()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==3:
        mostrar_inscritos()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==4:
        modificar_camper()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==5:
        print()

def rutas():

    suboption=menu_rutas()
    if suboption==1:
        crear_nueva_ruta()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==2:
        mostrar_rutas()
        input("Click cualquier tecla [continuar]: ")
    elif suboption==3:
        print()

while True:
    op=menu_principal()
    if op==1:
        manejar_campers()
    elif op==2:
        rutas()
    elif op==3:
        print("Gracias por utilizar nuestro servicio")
        break