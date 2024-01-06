from proceso.campers_register import inscribir_camper, mostrar_campers
from herramientas.menus import menu_principal, menu_campers
from herramientas.utilidades import limpiar_pantalla

def centro():
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
        inscribir_camper()
        input("Click cualquier tecla [continuar]: ")
    if op==2:
        mostrar_campers()
        input("Click cualquier tecla [continuar]: ")
    
    
while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        centro()
    elif op==2:
        print()
    elif op==3:
        print("Gracias por utilizar nuestro servicio")
        break
    else: 
        print("Invalido")