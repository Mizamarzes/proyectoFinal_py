from tools.utils import *

#------------------------------------------------------------------------
# crear areas de entrenamiento_____

def generar_area_entrenamiento():
    lista_areas = cargar_json("areas.json")        # cargar el json de los trainers
    lista_trainers = cargar_json("trainers.json")
    salones=["Artemis", "Apolo", "Sputnik"]
    j=0;k=0
    
    for i in lista_trainers:
        k=k+1 
        id=k
        area=salones[j%3]
        trainer=i['nombre']
        ruta=i['ruta']
        horario=i['horario']        
        j=j+1
        
        campers=crear_grupos()

        new_area_entrenamiento = {
            "numero":id,
            "area":area,
            "trainer":trainer,
            "ruta":ruta,
            "horario":horario,
            "campers":campers,
            "cantidad campers":len(campers)
        }
        
        
        lista_areas.append(new_area_entrenamiento)
    save_json(lista_areas, "areas.json")



#-----------------------------------------------------------------
# crear cada grupo
        
def crear_grupos():
    lista_aprobrados=cargar_json("aprobados.json")
    grupo_camper=[]
    cont=0

    for i in lista_aprobrados:
        cont=cont+1
        if cont<=33:
            camper=i['id']
            grupo_camper.append(camper)
    
    return grupo_camper
        