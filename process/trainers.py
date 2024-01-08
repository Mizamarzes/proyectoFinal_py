from tools.utils import *

#------------------------------------------------------------------------
# crear trainers

def crear_trainers():
    lista_trainers = cargar_json("trainers.json")        # cargar el json de los trainers

    id_trainer=int(input("Numero de identificacion: "))
    nombre_trainer=input("Nombre del trainer:  ")
    horario=input("Horario: ")
    ruta=input("Ruta a enseñar: ")
    
    new_trainer = {
        "id": id_trainer,
        "nombre": nombre_trainer,
        "horario": horario,
        "ruta": ruta,
        
    }
    lista_trainers.append(new_trainer)
    save_json(lista_trainers, "trainers.json")