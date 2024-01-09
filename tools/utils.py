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
                print(f"Opción no esta entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número valido. ")

def generar_id():
    return random.randint(100000000, 999999999)

def generar_nombre():
    nombres = ["Juan", "Ana", "Carlos", "Laura", "David", "Isabel", "Pedro", "Sofia", "Miguel", "Elena", "Lucia", "Javier", "María", "Alejandro", "Rosa"]
    return random.choice(nombres)

def generar_apellidos():
    apellidos = ["Perez", "Gomez", "Rodriguez", "Fernandez", "Martinez", "Lopez", "Diaz", "Hernandez", "Gutierrez", "Jimenez", "Sánchez", "Ramirez", "Cruz", "Ortega", "Morales"]
    return random.choice(apellidos)

def generar_direccion():
    direcciones = ["Calle A", "Avenida B", "Carrera C", "Calle D", "Avenida E", "Carrera F"]
    return f"{random.randint(1, 100)} {random.choice(direcciones)}"

def generar_acudiente():
    acudientes = ["Padre", "Madre", "Abuelo", "Abuela", "Tio", "Tia"]
    return f"{random.choice(acudientes)} de {generar_nombre()} {generar_apellidos()}"

def generar_telefono():
    return f"{random.randint(1000000, 9999999)}"

def generar_notas_inicial():
    return random.randint(40, 100)

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

campos_inscritos = ['id', 'nombre', 'apellidos', 'direccion', 'acudiente', 'telefono', 'estado']
campos_aprobados = ['numero', 'id', 'estado', 'nota_prueba_admision']
campos_trainers = ['id', 'nombre', 'horario', 'ruta']
campos_rutas = ['nombre', 'fundamentos_de_programacion','programacion_web','programacion_formal','bases_de_datos','backend']
campos_aulas= ['numero', 'area', 'trainer', 'ruta', 'horario', 'campers', 'cantidad campers']
campos_riesgo= ['numero', 'id', 'trainer', 'ruta', 'Nota', 'estado']
campos_linea= ['numero', 'id', 'trainer', 'ruta', 'Nota', 'estado']

def mostrar_listado(nombre_archivo, campos):
    lista_object = cargar_json(nombre_archivo)
    print("Listado: ")
    print("---" * 15)
    
    for dato in lista_object:
        for campo in campos:
            print(f"{campo.capitalize()}: {dato[campo]}")
        print("---" * 15)

#--------------------------------------------------------------------
# limpiar json
        
def limpiar_json(nombre_archivo):
    ruta_archivo = os.path.join("data", nombre_archivo)
    with open(ruta_archivo, "w") as archivo:
        archivo.write("[]")

#------------------------------------------------------------------------

def final_epico():
    # print("    ⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀")
    # print("⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀")
    # print("⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆")
    # print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆")
    # print("⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆")
    # print("⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿")
    # print("⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉")
    # print("⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇")
    # print("⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇")
    # print("⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇")
    # print(" ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇")
    # print("⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇")
    # print("⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ")
    print(" ═══•◉•═════")
    print(" ▂▄▄▓▄▄▂")
    print(" ◢◤ █▀▀████▄▄▄▄◢◤")
    print(" █▄ █ █▄ ███▀▀▀▀▀▀▀╬")
    print(" ◥█████◤")
    print(" ═╩══╩═")
    print(" ╬═╬")
    print(" ╬═╬")
    print(" ╬═╬")
    print(" ╬═╬  GRACIAS POR UTILIZAR NUESTRO SERVICIO!!!!!")
    print(" ╬═╬ ●/")
    print(" ╬═╬/▌")
    print(" ╬═╬/ \ ")                    