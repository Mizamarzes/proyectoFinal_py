import json
import os

def cargar_campers_json():
    try:
        with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_campers
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        

lista_campers=cargar_campers_json()
print(lista_campers)

def inscribir_camper():
    print("Ingresa: ")
    num_identificacion=int(input("Numero de identificación: "))
    nombre=input("Nombre: ")
    # apellidos=input("Apellidos: ")
    # direccion=input("Direccion: ")
    # acudiente=input("Acudiente: ")
    # telefonoFijo=int(input("Telefono Fijo: "))
    # numCelular=int(input("Nro celular: "))
    # estado=input("Estado: ")
    
    new_camper={
        'Num_identificacion':num_identificacion,
        'Nombre':nombre,
        # "Apellido":apellidos,
        # "Direccion":direccion,
        # "Acudiente":acudiente,
        # "Telefono":[telefonoFijo, numCelular],
        # "Estado":estado
    }
    

    lista_campers.append(new_camper)
    print("Se ha inscrito el camper con exito")
    save_json()

def save_json():
    try:
      with open(os.path.join("data", "campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
    
def mostrar_campers():
    print("Lista de campers: ")
    for camper in lista_campers:
        print(camper)

