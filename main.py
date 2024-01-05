
from proceso.campers_register import lista_campers, inscribir_camper, mostrar_campers, cargar_campers_json
from herramientas.menus import menu_principal
from herramientas.utilidades import limpiar_pantalla

def centro():
    limpiar_pantalla()
    if op==1:
        inscribir_camper()
    elif op==2:
        mostrar_campers()
    else:
        print("Opcion no valida")
    
while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        centro()
    elif op==2:
        continue
    elif op==3:
        break
    else: 
        print("Invalido")