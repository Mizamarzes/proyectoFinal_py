from business.campers_register import inscribir_camper, mostrar_campers
from business.generar_campers import generar_list
from commons.menus import menu_principal, menu_campers
from commons.utils import limpiar_pantalla


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
        input("Click cualquier tecla [continuar]: ")

generar_list()     # genera la lista de estudiantes de forma alelatoria
 
while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        centro()
    elif op==2:
        print("Gracias por utilizar nuestro servicio")
        break        
    else: 
        print("Invalido")