
def generar_list():
    students=[]

    nombres=["Guts", "Thorfin", "Mushashi"]
    apellidos=["Contreras", "Melendez", "Castro"]
    direcciones=["Bucarica", "Florida"," Peyecuesta"]
    acudientes=["Claudia", "Alejandra"," Valentina"]
    telefonos=["315324562", "3187003254", "3118880231"]
    estado=["Activo", "Inactivo"]
    
    for i in range(0,33,1):
        student = {
            "Num_identificacion": i + 1,
            "Nombre": nombres[i % 3],
            "Apellido": apellidos[i % 3],
            "Direccion": direcciones[i % 3],
            "Acudiente": acudientes[i % 3],
            "Telefono": telefonos[i % 3],
            "Estado": estado[i % 2]
        }
    
        students.append(student)
    return students