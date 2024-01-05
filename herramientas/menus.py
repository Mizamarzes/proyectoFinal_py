from herramientas.utilidades import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Registrar camper")
    print("2. Mostrar campers")
    print("3. Salir")
    op=validar_opcion("Seleccione: ", 1,3)
    return op
