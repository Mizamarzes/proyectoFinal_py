from tools.utils import *

def matriculas_campers():
    lista_campers = cargar_json("aprobados.json")
    lista_areas = cargar_json("areas.json")
    
    id_buscar = int(input("ID del camper: "))
    
    camper_encontrado = None
    for camper in lista_campers:
        if camper['id'] == id_buscar:
            camper_encontrado = camper
            break

    if not camper_encontrado:
        print("Camper no encontrado en la lista de aprobados.")
        return

    experto_encargado = input("Trainer: ")
    ruta_asignada = input("Ruta de entrenamiento: ")
    fecha_inicio = input("Fecha inicio(dd/mm/yyyy): ")
    fecha_finalizar = input("Fecha final(dd/mm/yyyy): ")

    ruta_encontrada = None
    for area in lista_areas:
        if area['trainer'] == experto_encargado and area['ruta'] == ruta_asignada:
            ruta_encontrada = area
            break

    if not ruta_encontrada:
        print(f"No se encontró una ruta de entrenamiento con el entrenador {experto_encargado} y la ruta {ruta_asignada}.")
        return

    ruta_encontrada['campers'].append(camper_encontrado['id'])
    save_json(lista_areas, "areas.json")

    new_matriculado = {
        "id": id_buscar,
        "trainer": experto_encargado,
        "ruta": ruta_asignada,
        "fecha_inicio": fecha_inicio,
        "fecha_finalizar": fecha_finalizar
    }

    save_json([new_matriculado], "areas.json")
    print("Camper matriculado con éxito en la ruta de entrenamiento.")