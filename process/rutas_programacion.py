import json

try:
    with open("data/campers.json", "r") as file:
        lista_campers = json.load(file)

    for camper in lista_campers:
        print("")
        print(f"Numero de identificacion: {camper['id']}")

except FileNotFoundError:
    print("El archivo no se encuentra.")
except json.JSONDecodeError:
    print("Error al decodificar el JSON.")
except Exception as e:
    print(f"Se produjo un error: {e}")


# rutas={
#     "ruta1": "NodeJs",
#     "ruta2": "Java",
#     "ruta3": "NetCore"
# }

# for clave,valor in colection.items():
#     print(f"{clave} -> {valor}")