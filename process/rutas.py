import json
import os
from campers_register import cargar_json, save_json

#-------------------------------------------------------------
# funciones de carga de json

def cargar_rutas_json():
    try:
        with open(os.path.join("data", "rutas.json"), 'r') as archivo_json:        
            lista_rutas = json.load(archivo_json)
            # print("La lista de inscritos ha sido cargada")
            return lista_rutas
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

#------------------------------------------------------------------
# funciones de guardar json
    
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

#-------------------------------------------------------------------------
# mostrar rutas

def mostrar_rutas():
    lista_rutas = cargar_rutas_json()
    print("Lista de rutas: ")
    for ruta in lista_rutas:
        print(ruta)

#-------------------------------------------------------------------------
# agregrar rutas

def crear_nueva_ruta():
    lista_rutas = cargar_rutas_json()

    nombre_ruta=input("Nombre de la ruta:  ")
    fundamentos_programacion=input("Temas de fundamentos de programacion:  ")
    programacion_web=input("Tecnologias de programacion web: ")
    programacion_formal=input("Lenguaje formal: ")
    bases_de_datos=input("Tecnologias para bases de datos: ")
    backend=input("Tecnologias para backend: ")

    new_ruta = {
        "nombre": nombre_ruta,
        "fundamentos_de_progamacion": fundamentos_programacion,
        "programacion_web": programacion_web,
        "programacion_formal": programacion_formal,
        "bases_de_datos": bases_de_datos,
        "backend": backend,
    }

    lista_rutas.append(new_ruta)
    save_json(lista_rutas, "rutas.json")
