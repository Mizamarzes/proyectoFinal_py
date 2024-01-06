import json
from commons.utils import *
campers = []
def generar_list():
    
    for _ in range(33): 
        datos = {
            "id": generar_id(),
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": generar_telefono(),
            "estado": "Inscrito",
        }
        campers.append(datos)

    campers_object = json.dumps(campers, indent=2, ensure_ascii=False)
    with open("data/campers.json", "w", encoding="utf-8") as archivo:
        archivo.write(campers_object)
