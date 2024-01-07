import json
import os
from tools.utils import *

# ------------------------------------------------------------------------------
# funciones de carga de json

def cargar_campers_json():
    try:
        with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            return lista_campers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
    
def cargar_inscritos_json():
    try:
        with open(os.path.join("data", "inscritos.json"), 'r') as archivo_json:        
            campers_inscritos = json.load(archivo_json)
            print("La lista de inscritos ha sido cargada")
            return campers_inscritos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []


#-------------------------------------------------------------------------------
# funcion de guardar json
    
def save_json(lista_campers, filename):
    try:
        with open(os.path.join("data", filename), 'w', encoding="utf-8") as archivo_json:
            json.dump(lista_campers, archivo_json, indent=2, ensure_ascii=False)
            print(f"La lista de {filename} ha sido guardada")
    except FileNotFoundError:
        print(f"El archivo {filename} no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {filename}. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido al guardar {filename}: {e}")

# -------------------------------------------------------------------------------
# funcion de registrar camper unitario

def inscribir_camper():
    lista_campers = cargar_campers_json()

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
        estado="Inscrito"

        new_camper_inscritos = {
            "id": id,
            "estado": estado,
            "nota_prueba_admision": promedio_nota_inicial
        }

        campers_inscritos=cargar_inscritos_json()
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
        
campers_alelatorios = []
def generar_list():
    
    for i in range(33):

        nota_prueba_teorica=generar_notas_inicial()
        nota_prueba_practica=generar_notas_inicial()
        promedio_nota_inicial = promedio(nota_prueba_teorica, nota_prueba_practica, 2)
        estado = "Inscrito" if promedio_nota_inicial >= 60 else "Rechazado"

        datos = {
            "id": generar_id(),
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": [generar_telefono(),generar_telefono()],
            "nota_prueba_admision":promedio_nota_inicial,
            "estado:":estado
        }
        campers_alelatorios.append(datos)

    with open("data/campers.json", "w", encoding="utf-8") as archivo:
        json.dump(campers_alelatorios, archivo, indent=2, ensure_ascii=False)

#----------------------------------------------------------------------------------------
# crear lista de inscritos que aprobaron la prueba de admision

inscritos_file_path = os.path.join("data", "inscritos.json")
if os.path.exists(inscritos_file_path):
    os.remove(inscritos_file_path)

campers_inscritos = cargar_inscritos_json()

def notas_prueba_inicial():
    try:
        with open("data/campers.json", "r") as file:
            lista_campers = json.load(file)

        for camper in lista_campers:
            notas_prueba_teorica = generar_notas_inicial()
            notas_prueba_practica = generar_notas_inicial()
            promedio_nota_inicial = promedio(notas_prueba_teorica, notas_prueba_practica, 2)

            estado = "Inscrito" if promedio_nota_inicial >= 60 else "Rechazado"

            new_camper_inscritos = {
                "id": camper['id'],
                "estado": estado,
                "nota_prueba_admision": promedio_nota_inicial
            }

            if estado == "Inscrito":
                campers_inscritos.append(new_camper_inscritos)

        if campers_inscritos:  # Check if there are any campers to save
            save_json(campers_inscritos, "inscritos.json")

    except FileNotFoundError:
        print("El archivo no se encuentra.")
    except json.JSONDecodeError:
        print("Error al decodificar el JSON.")
    except Exception as e:
        print(f"Se produjo un error: {e}")


# --------------------------------------------------------------------
# funciones para mostrar

def mostrar_campers():
    lista_campers = cargar_campers_json()
    print("Lista de campers: ")
    for camper in lista_campers:
        print(camper)

def mostrar_inscritos():
    campers_inscritos = cargar_inscritos_json()
    print("Lista de inscritos: ")
    for inscrito in campers_inscritos:
        print(inscrito)

# -------------------------------------------------------------------
# modificar campers, lista general





        


