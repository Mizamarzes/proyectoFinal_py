
def registrar_student():
    
    print("Ingresa: ")
    num_identificacion=int(input("Numero de identificación: "))
    nombre=str(input("Nombre: "))
    apellidos=str(input("Apellidos: "))
    direccion=str(input("Direccion: "))
    acudiente=str(input("Acudiente: "))
    telefono=int(input("Telefono: "))
    estado=str(input("Estado: "))
    
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
