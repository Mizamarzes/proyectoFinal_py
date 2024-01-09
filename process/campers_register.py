from tools.utils import *

# -------------------------------------------------------------------------------
# funcion de registrar camper o incribir por unidad

def inscribir_camper():
        lista_inscritos = cargar_json("inscritos.json")
        lista_nuevo=[]
    
        id=int(input("Numero de identificacion: "))
        nombre=input("Nombre: ")
        apellidos=input("Apellidos: ")
        direccion=input("Direccion: ")
        acudiente=input("Acudiente: ")
        telefonoFijo=input("Telefono Fijo: ")
        nota_prueba_teorica=input("Nota prueba de admision teorica: ")
        nota_prueba_practica=input("Nota prueba de admision practica: ")
        promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
        estado="Inscrito"
        

        new_camper_inscrito={
            'id':id,
            'nombre':nombre,
            "apellidos":apellidos,
            "direccion":direccion,
            "acudiente":acudiente,
            "telefono":telefonoFijo,
            "nota_prueba_admision":promedio_nota_inicial,
            "estado":estado
        }

        lista_inscritos.append(new_camper_inscrito)
        lista_nuevo.append(new_camper_inscrito)
        save_json(lista_inscritos, "inscritos.json")
        print("Se ha inscrito el camper con exito")

        generar_lista_aprobados(lista_nuevo)

def reinicio():
    salida=input("Desea agregrar otro(y/n): ")
    return salida         

# ------------------------------------------------------------------------------------
# crear lista de inscritos de forma alelatoria
        
def generar_list():
    campers_alelatorios_inscritos = []
    for i in range(100):

        nota_prueba_teorica=generar_notas_inicial()
        nota_prueba_practica=generar_notas_inicial()
        promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
        id=generar_id()
        estado="Inscrito"
        
        
        datos = {
            "id": id,
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": generar_telefono(),
            "nota_prueba_admision":promedio_nota_inicial,
            "estado":estado
        }

        campers_alelatorios_inscritos.append(datos)

    generar_lista_aprobados(campers_alelatorios_inscritos)
    save_json(campers_alelatorios_inscritos,"inscritos.json")        
    

#--------------------------------------------------------------------------------
# optimizacion para crear lista de aprobados

def generar_lista_aprobados(lista_campers):
    campers_aprobados = cargar_json("aprobados.json")
    i=0
    for camper in lista_campers:
        promedio_nota_inicial=camper['nota_prueba_admision']
        estado="Aprobado"
        id_=camper['id']
        
        if promedio_nota_inicial>=60:
            i=i+1
            new_camper_aprobado = {
                "numero":i,
                "id": id_,
                "estado": estado,
                "nota_prueba_admision": promedio_nota_inicial
            }
            campers_aprobados.append(new_camper_aprobado)
    
    save_json(campers_aprobados, "aprobados.json")

# -------------------------------------------------------------------------------
        
def modificar(filename):
    lista_data = cargar_json(filename)
    id_buscar = int(input("Ingrese numero de identificacion: "))
    encontrado = False

    for datos in lista_data:
        if datos['id'] == id_buscar:
            encontrado = True
            break
    
    if encontrado:
        llave = key_menu(lista_data[0]) 
        nuevo_valor = input("Ingrese el nuevo valor: ")

        for datos in lista_data:
            if datos["id"] == id_buscar:
                datos[llave] = nuevo_valor
                break

        save_json(lista_data, filename)
    else:
        print("No se encontro el camper")

#   Seleccionar llave a modificar ---------------------
        
def key_menu(dato):
    print("Seleccione una llave:")
    i=0
    for llave in dato.keys():
        i+=1
        print(f"{i}. {llave}")
        
    opcion = int(input("Opción: "))
    if opcion==1:
        respuesta="id"
    elif opcion==2:
        respuesta="nombre"
    elif opcion==3:
        respuesta="apellidos"
    elif opcion==4:
        respuesta="direccion"
    elif opcion==5:
        respuesta="acudiente"
    elif opcion==6:
        respuesta="telefono"
    elif opcion==7:
        respuesta="estado"
    return respuesta

#----------------------------------------------------------
# buscar camper

def buscar_camper_por_id(filename):
    lista_campers=cargar_json(filename)
    id_buscar=int(input("Ingrese ID: "))
    
    encontrado=None
    for camper in lista_campers:
        if camper['id'] == id_buscar:
            encontrado=camper
            break
    
    if not encontrado:
        print("No encontrado")
        return
    return encontrado