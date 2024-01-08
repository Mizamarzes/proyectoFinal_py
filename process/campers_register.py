from tools.utils import *
cont=0
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
    numCelular=input("Nro celular: ")
    nota_prueba_teorica=input("Nota prueba de admision teorica: ")
    nota_prueba_practica=input("Nota prueba de admision practica: ")
    promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
    
    if promedio_nota_inicial>=60:
        estado="Aprobado"
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
    lista_nuevo.append(new_camper_inscrito)
    save_json(lista_inscritos, "inscritos.json")
    print("Se ha inscrito el camper con exito")

    generar_lista_aprobados(lista_nuevo)


# ------------------------------------------------------------------------------------
# crear lista de inscritos de forma alelatoria
        
def generar_list():
    campers_alelatorios_inscritos = []
    for i in range(33):

        nota_prueba_teorica=generar_notas_inicial()
        nota_prueba_practica=generar_notas_inicial()
        promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
        id=generar_id()
        
        if promedio_nota_inicial>=60:
            estado="Aprobado"
        else:
            estado="Rechazado"
        
        datos = {
            "id": id,
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": [generar_telefono(),generar_telefono()],
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
    
    for camper in lista_campers:
        promedio_nota_inicial=camper['nota_prueba_admision']
        estado=camper['estado']
        id_=camper['id']

        if promedio_nota_inicial>=60:
            new_camper_aprobado = {
                "id": id_,
                "estado": estado,
                "nota_prueba_admision": promedio_nota_inicial
            }
            campers_aprobados.append(new_camper_aprobado)
    
    save_json(campers_aprobados, "aprobados.json")

# -------------------------------------------------------------------------------
# modificar campers, lista general

def modificar_camper():
    lista_inscritos=cargar_json("inscritos.json")
    id_a_buscar=int(input("Numero de identificacion del camper a modificar: "))
    nuevo_estado=input("Nuevo estado: ")
        
    for camper in lista_inscritos:
        if camper['id'] == id_a_buscar:
            camper['estado'] = nuevo_estado
            print(f"Estado del camper con id {id_a_buscar} modificado a: {nuevo_estado}")

        if nuevo_estado=="Aprobado":
            generar_lista_aprobados(60,id_a_buscar)
        

