from process.campers_register import * 
from tools.menus import *
from tools.utils import *


def centro():
    generar_list()     # genera la lista de estudiantes de forma alelatoria
    notas_prueba_inicial() # genera lista de campers que aprobaron la prueba de admision
    limpiar_pantalla()    # limpia pantalla
    op=menu_campers()
    if op==1:
        inscribir_camper()
        input("Click cualquier tecla [continuar]: ")
    elif op==2:
        mostrar_campers()
        input("Click cualquier tecla [continuar]: ")
    elif op==3:
        mostrar_inscritos()
        input("Click cualquier tecla [continuar]: ")
    elif op==4:
        print()
    else:
        print("Invalido")

while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        centro()
    elif op==6:
        print("Gracias por utilizar nuestro servicio")
        break        
    else: 
        print("Invalido")