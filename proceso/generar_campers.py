import random
from herramientas.utilidades import generar_num_identificacion,generar_nombre,generar_apellidos,generar_direccion 
from herramientas.utilidades import generar_acudiente,generar_telefono,generar_estado

def generar_list():
    datos_aleatorios = []
    for _ in range(5): 
        datos = {
            "numero_identificacion": generar_num_identificacion(),
            "nombre": generar_nombre(),
            "apellidos": generar_apellidos(),
            "direccion": generar_direccion(),
            "acudiente": generar_acudiente(),
            "telefono": generar_telefono(),
            "estado": generar_estado()
        }
        datos_aleatorios.append(datos)

    for datos in datos_aleatorios:
        print(datos)