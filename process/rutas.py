from process.campers_register import *

#-------------------------------------------------------------------------
# agregrar rutas

def crear_nueva_ruta():
    lista_rutas = cargar_json("rutas.json")        # carga el json de las rutas

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
