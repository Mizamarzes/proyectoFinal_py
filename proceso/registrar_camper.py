
def regiar_student():
    
    print("Ingresa: ")
    num_identificacion=int(input("Numero de identificación: "))
    nombre=input("Nombre: ")
    apellidos=input("Apellidos: ")
    direccion=input("Direccion: ")
    acudiente=input("Acudiente: ")
    telefono=int(input("Telefono: "))
    estado=input("Estado: ")
    
    new_student={
        "Num_identificacion":num_identificacion,
        "Nombre":nombre,
        "Apellido":apellidos,
        "Direccion":direccion,
        "Acudiente":acudiente,
        "Telefono":telefono,
        "Estado":estado
    }
    
    return new_student
