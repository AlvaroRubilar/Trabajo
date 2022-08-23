from cmath import inf
import hoja_de_ruta
mat2130_006V = {
"asignatura" : 'algebra_y_trigonometria',
"seccion" : 'MAT2130-006V',
"dia1" : "martes",
"hora1" : "21:10-22:30",
"dia2" : "viernes",
"hora2" : "19:00-21:10",
"opcion":1

}

mat3110_003D = {
"asignatura" : 'calculo_diferencial',
"seccion" : 'MAT3110-003D',
"dia1" : "lunes",
"hora1" : "12:10-14:20",
"dia2" : "martes",
"hora2" : "12:10-13:40",
"opcion":2
}
mat3111_001V = {
"asignatura" : 'calculo_diferencial',
"seccion" : 'MAT3111-001V',
"dia1" : "jueves",
"hora1" : "20:30-22:30",
"dia2" : "viernes",
"hora2" : "21:10-22:30",
"opcion":1

}



mat2110_017D = {
"asignatura" : 'algebra',
"seccion" : 'MAT2110-017D',
"dia1" : "lunes",
"hora1" : "10:40-12:10",
"dia2" : "jueves",
"hora2" : "10:00-12:10",
"opcion":2
}

mat2110_034V = {
"asignatura" : 'algebra',
"seccion" : 'MAT2110-034V',
"dia1" : "martes",
"hora1" : "19:00-21:10",
"dia2" : "miércoles",
"hora2" : "21:10-22:30",
"opcion":1
}

mat2120_009D = {
"asignatura" : 'matematica_aplicada',
"seccion" : 'MAT2120-009D',
"dia1" : "jueves",
"hora1" : "16:00-17:20",
"dia2" : "viernes",
"hora2" : "16:00-17:20",
"opcion":1

}

mat2120_010V = {
"asignatura" : 'matematica_aplicada',
"seccion" : 'MAT2120-010V',
"dia1" : "miércoles",
"hora1" : "19:00-20:20",
"dia2" : "sábado",
"hora2" : "11:30-12:50",
"opcion":1
}
mat2120_001V = {
"asignatura" : 'matematica_aplicada',
"seccion" : 'MAT2120-001V',
"dia1" : "jueves",
"hora1" : "19:00-20:20",
"dia2" : "sábado",
"hora2" : "8:30-9:50",
"opcion":1

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