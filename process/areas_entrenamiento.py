from tools.utils import *

#------------------------------------------------------------------------
# crea grupos

def crear_grupos(inicio, fin):
    lista_aprobados = cargar_json("aprobados.json")
    grupo_camper = []

    for i in range(inicio, fin):
        if i < len(lista_aprobados):
            camper = lista_aprobados[i]['id']
            grupo_camper.append(camper)

    return grupo_camper

#-------------------------------------------------------------------------
# genera el area de entrenamiento con sus respectiva informacion

def generar_area_entrenamiento():
    lista_areas = cargar_json("areas.json")
    lista_trainers = cargar_json("trainers.json")
    salones = ["Artemis", "Apolo", "Sputnik"]
    
    cantidad_camper_por_entrenador = 30
    cantidad_total_camper = cantidad_camper_por_entrenador * len(lista_trainers)

    for j, trainer in enumerate(lista_trainers):
        id = j + 1
        area = salones[j % 3]
        trainer_nombre = trainer['nombre']
        ruta = trainer['ruta']
        horario = trainer['horario']
        
        inicio = j * cantidad_camper_por_entrenador
        fin = inicio + cantidad_camper_por_entrenador
        campers = crear_grupos(inicio, fin)
        
        new_area_entrenamiento = {
            "numero": id,
            "area": area,
            "trainer": trainer_nombre,
            "ruta": ruta,
            "horario": horario,
            "campers": campers,
            "cantidad campers": len(campers)
        }
        
        lista_areas.append(new_area_entrenamiento)
    save_json(lista_areas, "areas.json")

#--------------------------------------------------------------------------------
