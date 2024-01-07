import json
import os

#----------------------------------------------------------
# funcion de carga

def cargar_trainers_json():
    try:
        with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
            lista_trainers = json.load(archivo_json)
            # print("La lista de inscritos ha sido cargada")
            return lista_trainers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
    