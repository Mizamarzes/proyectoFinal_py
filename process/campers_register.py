import json,os
from tools.utils import *

# -------------------------------------------------------------------------------
# funcion de registrar camper unitario

def inscribir_camper():
    lista_campers = cargar_json("campers.json")

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

        new_camper_inscritos = {
            "id": id,
            "estado": estado,
            "nota_prueba_admision": promedio_nota_inicial
        }

        campers_inscritos=cargar_json("inscritos.json")
        campers_inscritos.append(new_camper_inscritos)
        save_json(campers_inscritos, "inscritos.json")

    else:
        estado="Rechazado"

    new_camper={
        'id':id,
        'nombre':nombre,
        "apellidos":apellidos,
        "direccion":direccion,
        "acudiente":acudiente,
        "telefono":[telefonoFijo, numCelular],
        "nota_prueba_admision":promedio_nota_inicial,
        "estado":estado
    }

    lista_campers.append(new_camper)
    print("Se ha inscrito el camper con exito")
    save_json(lista_campers, "campers.json")


# ------------------------------------------------------------------------------------
# crear lista de campers de forma alelatoria
        

def generar_list():
    campers_alelatorios = []
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
        campers_alelatorios.append(datos)

    with open("data/campers.json", "w", encoding="utf-8") as archivo:
        json.dump(campers_alelatorios, archivo, indent=2, ensure_ascii=False)

#----------------------------------------------------------------------------------------
# crear lista de inscritos que aprobaron la prueba de admision

def generar_lista_aprobados():
    try:
        inscritos_file_path = os.path.join("data", "inscritos.json")
        if os.path.exists(inscritos_file_path):
            os.remove(inscritos_file_path)

        campers_inscritos = cargar_json("inscritos.json")

        with open("data/campers.json", "r") as file:
            lista_campers = json.load(file)

        for camper in lista_campers:
            notas_prueba_teorica = camper['nota_prueba_admision']
            notas_prueba_practica = camper['nota_prueba_admision']
            promedio_nota_inicial = promedio(notas_prueba_teorica, notas_prueba_practica, 2)

            estado = "Aprobado" if promedio_nota_inicial >= 60 else "Rechazado"

            new_camper_inscritos = {
                "id": camper['id'],
                "estado": estado,
                "nota_prueba_admision": promedio_nota_inicial
            }

            if estado == "Aprobado":
                campers_inscritos.append(new_camper_inscritos)

        if campers_inscritos:  # Check if there are any campers to save
            save_json(campers_inscritos, "inscritos.json")

    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except json.JSONDecodeError:
        print("Error al decodificar el JSON.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# -------------------------------------------------------------------
# modificar campers, lista general

def modificar_camper():

    try:
        campers_inscritos = cargar_json("inscritos.json")
        lista_campers=cargar_json("campers.json")
        id_a_buscar=int(input("id del camper a modificar: "))
        nuevo_estado=input("Nuevo estado: ")
        
        for camper in lista_campers:
            if camper['id'] == id_a_buscar:
                camper['estado'] = nuevo_estado
                print(f"Estado del camper con id {id_a_buscar} modificado a: {nuevo_estado}")

            if nuevo_estado.lower() == "aprobado":
                new_camper_inscritos = {
                    "id": camper['id'],
                    "estado": nuevo_estado,
                    "nota_prueba_admision": camper['nota_prueba_admision']
                }
                campers_inscritos.append(new_camper_inscritos)

        save_json(lista_campers, "campers.json")

        if campers_inscritos:  
            save_json(campers_inscritos, "inscritos.json")
        
    except FileNotFoundError:
        print(f"El archivo no se encuentra.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el JSON.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

    


        


