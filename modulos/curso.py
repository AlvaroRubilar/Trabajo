from cmath import inf
import hoja_de_ruta
def creacion_curso(asignatura,seccion, dia1,hora1,dia2,hora2):
    if asignatura == 'algebra':
        nombre_asignatura="Álgebra"
        unidades=[
        ["Unidad 1: Funciones lineales y cuadráticas",
        "Competencia: resuelve problemas de fenómenos modelados por funciones lineales y cuadráticas, de acuerdo a requerimientos."],
        ["Unidad 2: Funciones exponenciales y logarítmicas",
        "Competencia: resuelve problemas de fenómenos modelados por funciones exponenciales y logarítmicas de acuerdo a requerimientos."]]
    
    if asignatura == 'algebra_y_trigonometria':
        nombre_asignatura="Álgebra y Trigonometría"
        unidades=[
        ["Unidad 1: Funciones",
        "Competencia: resuelve problemas de fenómenos modelados por funciones elementales, de acuerdo a requerimientos."],
        ["Unidad 2: Funciones trigonométricas y aplicaciones",
        "Competencia: resuelve problemas de fenómenos modelados por funciones trigonométricas, de acuerdo a requerimientos."]]
    if asignatura=="calculo":
        nombre_asignatura="Cálculo"
        unidades =[
            ["Unidad 1: Funciones Reales",
            "Competencia: Resolver problemas que involucran el modelamiento con funciones reales elementales, de acuerdo a requerimientos"],
            ["Unidad 2: La derivada y sus aplicaciones",
            "Competencia: Resolver problemas que involucran el análisis de funciones elementales utilizando procedimientos de cálculo diferencial, de acuerdo a requerimientos."]]
    
    if asignatura=="matematica_aplicada":
        nombre_asignatura="Matemática Aplicada"
        unidades =[
            ["Unidad 1: Arreglos y bucles",
            "Competencia: resuelve problemas de fenómenos modelados por la aritmética matricial, sucesiones y sumatorias, de acuerdo a requerimientos."],
            ["Unidad 2: Funciones lineal y cuadrática",
            "Competencia: resuelve problemas de fenómenos modelados por funciones lineales y cuadráticas, de acuerdo a requerimientos."]]
    return {

    "Asignatura": nombre_asignatura, 
    "Sección":seccion,
    "Horario":[dia1,hora1,dia2,hora2],
    "Unidades":unidades
    }

# diccionario =creacion_curso('calculo','MAT2130-034V',"martes","19:00-21:10","miércoles","21:10-22:30")

# informe=f'''
# Prueba creacion curso
# Asignatura: {diccionario["Asignatura"]}

# Sección: {diccionario["Sección"]}

# Horario

# {diccionario["Horario"][0]}\t\t{diccionario["Horario"][2]}
# {diccionario["Horario"][1]}\t{diccionario["Horario"][3]}

# {diccionario["Unidades"][0][0]}
# {diccionario["Unidades"][0][1]}

# {diccionario["Unidades"][1][0]}
# {diccionario["Unidades"][1][1]}
#  '''
# print(informe)