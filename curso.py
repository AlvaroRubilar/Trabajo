from cmath import inf
import hoja_de_ruta



mat2120_003V = {
"asignatura" : 'matematica_aplicada',
"seccion" : 'MAT2120-003V',
"dia1" : "jueves",
"hora1" : "19:00-20:20",
"dia2" : "sábado",
"hora2" : "8:30-09:50",
"opcion":1,
"validacion":True

}
mat1110_016D = {
"asignatura" : 'nivelacion_matematica',
"seccion" : 'MAT1110-016D',
"dia1" : "lunes",
"hora1" : "8:30-10:40",
"dia2" : "martes",
"hora2" : "10:40-12:50",
"opcion":1,
"validacion":True

}
mat1110_043D = {
"asignatura" : 'nivelacion_matematica',
"seccion" : 'MAT1110-043D',
"dia1" : "miércoles",
"hora1" : "8:30-10:40",
"dia2" : "viernes",
"hora2" : "8:30-10:40",
"opcion":1,
"validacion":True

}
mat1110_052D = {
"asignatura" : 'nivelacion_matematica',
"seccion" : 'MAT1110-052D',
"dia1" : "miércoles",
"hora1" : "14:30-16:40",
"dia2" : "viernes",
"hora2" : "10:40-12:50",
"opcion":1,
"validacion":True

}
mat3110_004V = {
"asignatura" : 'calculo_diferencial',
"seccion" : 'MAT3110-004V',
"dia1" : "lunes",
"hora1" : "19:00-21:10",
"dia2" : "miércoles",
"hora2" : "19:00-20:30",
"opcion":1,
"validacion":True

}
mat6110_008V = {
"asignatura" : 'herramientas_matematicas',
"seccion" : 'MAT6110-008V',
"dia1" : "miércoles",
"hora1" : "21:10-22:30",
"dia2" : "sábado",
"hora2" : "10:00-11:20",
"opcion":1,
"validacion":True

}

mat3120_002V = {
"asignatura" : 'calculo_integral',
"seccion" :'MAT3120-002V',
"dia1" :'jueves',
"hora1" :'20:30-22:30',
"dia2" :'sábado',
"hora2" :'13:00-14:20',
"opcion":'1',
"validacion":True

}


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
    if asignatura=="calculo_diferencial":
        nombre_asignatura="Cálculo Diferencial"
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
    if asignatura == "nivelacion_matematica":
        nombre_asignatura = "Nivelación Matemática"
        unidades = [
            ["Unidad 1: Los números en la vida","Competencia: resuelve problemas de fenómenos modelados por operaciones matemáticas básicas, de acuerdo a requerimientos."],
            ["Unidad 2: Aplicaciones numéricas en la resolución de problemas","Competencia: resuelve problemas de fenómenos modelados por cantidades proporcionales, potencias y raíces, de acuerdo a requerimientos."],
            ["Unidad 3: El lenguaje de las matemáticas","Competencia: resuelve problemas de fenómenos modelados por lenguaje algebraico, de acuerdo a requerimientos."]]
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
