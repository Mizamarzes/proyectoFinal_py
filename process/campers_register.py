from tools.utils import *

# -------------------------------------------------------------------------------
# funcion de registrar camper unitario

def inscribir_camper():
    lista_inscritos = cargar_json("inscritos.json")
    campers_aprobados=cargar_json("aprobados.json")

    id=int(input("Numero de identificacion: "))
    nombre=input("Nombre: ")
    apellidos=input("Apellidos: ")
    direccion=input("Direccion: ")
    acudiente=input("Acudiente: ")
    telefonoFijo=input("Telefono Fijo: ")
    numCelular=input("Nro celular: ")
    nota_prueba_teorica=input("Nota prueba de admision teorica: ")
    nota_prueba_practica=input("Nota prueba de admision practica: ")
    promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)

    if promedio_nota_inicial>=60:
        estado="Aprobado"

        new_camper_aprobado = {
            "id": id,
            "estado": estado,
            "nota_prueba_admision": promedio_nota_inicial
        }

        
        campers_aprobados.append(new_camper_aprobado)
        save_json(campers_aprobados, "aprobados.json")

    else:
        estado="Rechazado"

    new_camper_inscrito={
        'id':id,
        'nombre':nombre,
        "apellidos":apellidos,
        "direccion":direccion,
        "acudiente":acudiente,
        "telefono":[telefonoFijo, numCelular],
        "nota_prueba_admision":promedio_nota_inicial,
        "estado":estado
    }

    lista_inscritos.append(new_camper_inscrito)
    print("Se ha inscrito el camper con exito")
    save_json(lista_inscritos, "inscritos.json")


# ------------------------------------------------------------------------------------
# crear lista de campers de forma alelatoria
        
def generar_list():
    campers_alelatorios_inscritos = []
    for i in range(33):

        nota_prueba_teorica=generar_notas_inicial()
        nota_prueba_practica=generar_notas_inicial()
        promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
        estado = "Aprobado" if promedio_nota_inicial >= 60 else "Rechazado"

        datos = {
            "id": generar_id(),
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": [generar_telefono(),generar_telefono()],
            "nota_prueba_admision":promedio_nota_inicial,
            "estado":estado
        }
        campers_alelatorios_inscritos.append(datos)

    save_json(campers_alelatorios_inscritos,"inscritos.json")

#----------------------------------------------------------------------------------------
# crear lista de inscritos que aprobaron la prueba de admision

def generar_lista_aprobados():
    
    campers_aprobados=[]
    lista_inscritos=cargar_json("inscritos.json")
        
    for inscrito in lista_inscritos:
        notas_prueba_teorica = inscrito['nota_prueba_admision']
        notas_prueba_practica = inscrito['nota_prueba_admision']
        promedio_nota_inicial = promedio(notas_prueba_teorica, notas_prueba_practica, 2)

        estado = "Aprobado" if promedio_nota_inicial >= 60 else "Rechazado"

        new_camper_aprobado = {
            "id": inscrito['id'],
            "estado": estado,
            "nota_prueba_admision": promedio_nota_inicial
        }

        if estado == "Aprobado":
            campers_aprobados.append(new_camper_aprobado)
    
    save_json(campers_aprobados, "aprobados.json")

# -------------------------------------------------------------------------------
# modificar campers, lista general

def modificar_camper():

    lista_inscritos=cargar_json("inscritos.json")
    campers_aprobados = cargar_json("aprobados.json")
        
    id_a_buscar=int(input("id del camper a modificar: "))
    nuevo_estado=input("Nuevo estado: ")
        
    for camper in lista_inscritos:
        if camper['id'] == id_a_buscar:
            camper['estado'] = nuevo_estado
            print(f"Estado del camper con id {id_a_buscar} modificado a: {nuevo_estado}")

        if nuevo_estado.lower() == "aprobado":
            new_camper_aprobado = {
                "id": camper['id'],
                "estado": nuevo_estado,
                "nota_prueba_admision": camper['nota_prueba_admision']
            }
            campers_aprobados.append(new_camper_aprobado)

    save_json(campers_aprobados, "aprobado.json")

#-----------------------------------------------------------------------------
# optimizacion para añadir lista de aprobados


        


