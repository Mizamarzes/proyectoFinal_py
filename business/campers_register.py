import json
import os

def cargar_campers_json():
    try:
        with open(os.path.join("data","campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_campers
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return []
        
lista_campers=cargar_campers_json()

def inscribir_camper():
    id=int(input("Numero de identificacion: "))
    nombre=input("Nombre: ")
    apellidos=input("Apellidos: ")
    direccion=input("Direccion: ")
    acudiente=input("Acudiente: ")
    telefonoFijo=input("Telefono Fijo: ")
    numCelular=input("Nro celular: ")
    estado="Inscrito"
    
    new_camper={
        'id':id,
        'nombre':nombre,
        "apellidos":apellidos,
        "direccion":direccion,
        "acudiente":acudiente,
        "telefono":[telefonoFijo, numCelular],
        "estado":estado
    }
    
    lista_campers.append(new_camper)
    print("Se ha inscrito el camper con exito")
    save_json()

def save_json():
    try:
      with open(os.path.join("data", "campers.json"), 'w', encoding="utf-8") as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2,  ensure_ascii=False)
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

