from commons.utils import validar_opcion

def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Registrar camper")
    print("2. Salir")
    op=validar_opcion("Seleccione: ",1,5)
    return op

def menu_campers():
    print("----------- Menú Campers-----------")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Salir")
    op=validar_opcion("Opcion: ",1,5)
    return op