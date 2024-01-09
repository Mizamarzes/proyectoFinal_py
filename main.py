from process.campers_register import * 
from process.rutas import *
from process.trainers import *
from process.areas_entrenamiento import *
from process.modulos import *
from process.matriculas import *
from tools.menus import *
from tools.utils import *

#-----------------------------------------------------------------------------------
# funciones de control secundarias

def manejar_campers():
    while True:
        limpiar_pantalla() # limpia pantalla
        suboption=menu_campers()
        if suboption==1:
            limpiar_pantalla()
            inscribir_camper()
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            limpiar_pantalla()
            modificar("inscritos.json")
            input("Click cualquier tecla [continuar]: ")
        elif suboption==3:
            break

def trainers():
    while True:
        limpiar_pantalla()
        suboption=menu_trainers()
        if suboption==1:
            limpiar_pantalla()
            crear_trainers()
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            limpiar_pantalla()
            mostrar_listado("trainers.json", campos_trainers)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==3:
            break

def matriculas():
    while True:
        limpiar_pantalla()
        suboption=menu_matriculas()
        if suboption==1:
            limpiar_pantalla()
            matriculas_campers()
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            break

def aulas():
    while True:
        limpiar_pantalla()
        suboption=menu_aulas()
        if suboption==1:
            limpiar_pantalla()
            mostrar_listado("areas.json", campos_aulas)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            break

def rutas():
    while True:
        limpiar_pantalla()
        suboption=menu_rutas()
        if suboption==1:
            limpiar_pantalla()
            crear_nueva_ruta()
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            limpiar_pantalla()
            mostrar_listado("rutas.json", campos_rutas)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==3:
            break

def reportes():
    while True:
        limpiar_pantalla()
        suboption=menu_reportes()
        if suboption==1:
            limpiar_pantalla()
            mostrar_listado("inscritos.json", campos_inscritos)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==2:
            limpiar_pantalla()
            mostrar_listado("aprobados.json", campos_aprobados)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==3:
            limpiar_pantalla()
            mostrar_listado("trainers.json", campos_trainers)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==4:
            limpiar_pantalla()
            mostrar_listado("areas.json", campos_aulas)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==5:
            limpiar_pantalla()
            mostrar_listado("riesgo.json", campos_riesgo)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==6:
            limpiar_pantalla()
            mostrar_listado("en_linea.json", campos_linea)
            input("Click cualquier tecla [continuar]: ")
        elif suboption==7:
            break


#--------------------------------------------------------------------------------------------------
limpiar_json("inscritos.json")
limpiar_json("aprobados.json")
limpiar_json("areas.json")
limpiar_json("matriculas.json")      # matriculas nuevas
generar_list()   # genera la lista de estudiantes de forma alelatoria y lista de aprobados tambien
generar_area_entrenamiento() # genera los salones con sus respectivos trainers y demas
modulo_primera_fase()    # modulos
#-------------------------------------------------------------------------------------------------

# zona controladora principal

while True:
    limpiar_pantalla()
    op=menu_principal()
    if op==1:
        manejar_campers()
    elif op==2:
        trainers()
    elif op==3:
        matriculas()
    elif op==4:
        aulas()
    elif op==5:
        rutas()
    elif op==6:
        reportes()
    elif op==7:
        limpiar_pantalla()
        final_epico()
        break