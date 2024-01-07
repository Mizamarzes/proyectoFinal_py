from business.campers_register import * 
from commons.menus import *
from commons.utils import *

generar_list()     # genera la lista de estudiantes de forma alelatoria
notas_prueba_inicial()

def centro():
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
        inscribir_camper()
        input("Click cualquier tecla [continuar]: ")
    if op==2:
        mostrar_campers()
        input("Click cualquier tecla [continuar]: ")
    if op==3:
        mostrar_inscritos()
        input("Click cualquier tecla [continuar]: ")


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