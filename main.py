import json

def registrar_student():
    print()


def generar_list():
    stundents=[
        
    ]
    
    nombres=["Guts", "Thorfin", "Mushashi"]
    apellidos=["Contreras", "Melendez", "Castro"]
    direcciones=["Bucarica", "Florida"," Peyecuesta"]
    acudientes=["Claudia", "Alejandra"," Valentina"]
    telefonos=["315324562", "3187003254", "3118880231"]
    estado=["Activo", "Inactivo"]
    
    
    for i in range(0,33,1):
        object01={}
        object01["Num_identificacion"]=i+1,
        object01["Nombre"]=nombres[i%3]
        object01["Apellido"]=apellidos[i%3]
        object01["Direccion"]=direcciones[i%3]
        object01["Acudiente"]=acudientes[i%3]
        object01["Telefono"]=telefonos[i%3]
        object01["Estado"]=estado[i%2]
    
        stundents.append(object01)
        
    return stundents

print("Menu Campuslands: ")
print("1. Registrar nuevo estudiante")
print("2. Mostrar lista de estudiantes")

option=int(input())

if option==1:
    registrar_student()
elif option==2:
    generar_list()
    
    stundents = generar_list()
    stundents_object=json.dumps(stundents, indent=1)
    file=open("archivo.json","w")
    file.write(stundents_object)
    file.close()
else: 
    print("Invalido")