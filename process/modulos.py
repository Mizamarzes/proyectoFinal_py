from tools.utils import *

#------------------------------------------------------------------
def modulo_primera_fase():
    lista_areas = cargar_json("areas.json")
    campers_en_linea = []
    campers_en_riesgo = []
    i = 0

    for area in lista_areas:
        ruta_asignada = area['ruta']
        entrenador = area['trainer']

        for camper_id in area['campers']:
            i += 1
            nota_practica = generar_notas_inicial() * 0.6
            nota_teorica = generar_notas_inicial() * 0.3
            nota_trabajos = generar_notas_inicial() * 0.1
            suma_total = nota_practica + nota_teorica + nota_trabajos

            if suma_total > 60:
                estado = "En_linea"
            else:
                estado = "Riesgo"

            new_camper = {
                "numero": i,
                "id": camper_id,
                "trainer": entrenador,
                "ruta": ruta_asignada,
                "Nota": suma_total,
                "estado": estado,
            }

            if suma_total > 60:
                campers_en_linea.append(new_camper)
            else:
                campers_en_riesgo.append(new_camper)

    save_json(campers_en_linea, "en_linea.json")
    save_json(campers_en_riesgo, "riesgo.json")

