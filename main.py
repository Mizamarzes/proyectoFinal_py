import json
from proceso.registrar_camper import registrar_student
from proceso.generar_Lista_campers import generar_list

while True:

    print("Menu Campuslands: ")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar lista de estudiantes")
    print("3. Salir")
    option=int(input())

    if option==1:
        new_student=registrar_student()
        new_student_object = json.dumps(new_student, indent=2)
        with open("registro_campers.json", "w") as file:
            file.write(new_student_object)

    elif option==2:
        students = generar_list()
        students_object = json.dumps(students, indent=2)
        with open("registro_campers.json", "w") as file:
            file.write(students_object)
    elif option==3:
        break
    else: 
        print("Invalido")