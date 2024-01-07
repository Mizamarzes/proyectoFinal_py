from process.campers_register import * 
from tools.menus import *
from tools.utils import *

generar_list()     # genera la lista de estudiantes de forma alelatoria
generar_lista_aprobados() # genera lista de campers que aprobaron la prueba de admision

def centro():
    limpiar_pantalla()	# limpia pantalla
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