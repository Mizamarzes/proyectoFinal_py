import random, os, json

#---------------------------------------------------------------------------
# necesidades varias

def numero_alelatorio():
    num_random=random.randint(0,2)
    return num_random

def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def generar_id():
    return random.randint(100000000, 999999999)

def generar_nombre():
    nombres = ["Juan", "Ana", "Carlos", "Laura", "David", "Isabel", "Pedro", "Sofía", "Miguel", "Elena", "Lucía", "Javier", "María", "Alejandro", "Rosa"]
    return random.choice(nombres)

def generar_apellidos():
    apellidos = ["Pérez", "Gómez", "Rodríguez", "Fernández", "Martínez", "López", "Díaz", "Hernández", "Gutiérrez", "Jiménez", "Sánchez", "Ramírez", "Cruz", "Ortega", "Morales"]
    return random.choice(apellidos)

def generar_direccion():
    direcciones = ["Calle A", "Avenida B", "Carrera C", "Calle D", "Avenida E", "Carrera F"]
    return f"{random.randint(1, 100)} {random.choice(direcciones)}"

def generar_acudiente():
    acudientes = ["Padre", "Madre", "Abuelo", "Abuela", "Tío", "Tía"]
    return f"{random.choice(acudientes)} de {generar_nombre()} {generar_apellidos()}"

def generar_telefono():
    return f"{random.randint(1000000, 9999999)}"

def generar_notas_inicial():
    return random.randint(20, 100)

def promedio(a,b,cant):
    a = int(a)
    b = int(b)
    prom=(a+b)/cant
    return prom

#------------------------------------------------------------------------
# funciones json

# cargar los json

def cargar_json(filename_path):
    try:
        with open(os.path.join("data", filename_path), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            # print("La lista de inscritos ha sido cargada")
            return lista_campers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
    
# ------------------------------------------------------------------------

# save json
    
def save_json(lista_campers, filename):
    try:
        with open(os.path.join("data", filename), 'w', encoding="utf-8") as archivo_json:
            json.dump(lista_campers, archivo_json, indent=2, ensure_ascii=False)
            # print(f"La lista de {filename} ha sido guardada")
    except FileNotFoundError:
        print(f"El archivo {filename} no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON {filename}. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido al guardar {filename}: {e}")


#-----------------------------------------------------------------------

# mostrar listas de campers y demas

def mostrar_objecto_lista(filename_e):
    lista_object = cargar_json(filename_e)
    print("Listado: ")
    for object in lista_object:
        print(object)

#--------------------------------------------------------------------
# limpiar json
        
def limpiar_json(nombre_archivo):
    ruta_archivo = os.path.join("data", nombre_archivo)

    with open(ruta_archivo, "w") as archivo:
        archivo.write("[]")

#------------------------------------------------------------------------
        