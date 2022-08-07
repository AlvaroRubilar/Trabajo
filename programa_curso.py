import locale
from datetime import date
from datetime import datetime,timedelta
locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
dt = datetime.now()
inicio=datetime(2022,8,8)
final = datetime(2022, 12,3)
dias_de_clase = ['lunes','viernes']
sep_16 = datetime(2022,9,16)
validacion = True

feriados = [
            datetime(2022,8,15),
            datetime(2022,9,17),
            datetime(2022,9,19),
            datetime(2022,10,10),
            datetime(2022,10,31),
            datetime(2022,11,1)]
if validacion:
    feriados.append(sep_16)

algebra_y_trigonometria = [

"Guía de ejercicios N°0:  Concepto de Función",
"Guía de ejercicios N°1: Funciones, Modelo Lineal.",
"Guía de ejercicios N°1: Funciones, Modelo Lineal.",
"Guía de ejercicios N°1: Funciones, Modelo Lineal.",

"Guía de ejercicios N°2: Funciones Cuadráticas.",
"Guía de ejercicios N°2: Funciones Cuadráticas.",
"Guía de ejercicios N°2: Funciones Cuadráticas.",
"Guía de ejercicios N°3:Funciones Lineales y Cuadráticas. Cuestionario 1 en AVA (5%)",

"Guía de ejercicios N°3: Funciones Lineales y Cuadráticas",
"Guía resumen N°1 de la primera unidad: Funciones lineales, cuadráticas y aplicaciones.",
"Prueba 1 (30% de relevancia)",
"Guía de ejercicios N°4: Función exponencial. ",

"Guía de ejercicios N°4: Función exponencial. ",
"Guía de ejercicios N°4: Función exponencial. ",
"Guía de ejercicios N°5: Función Logarítmica y Función Exponencial.",
"Guía de ejercicios N°5: Función Logarítmica y Función Exponencial.",

"Guía de ejercicios N°5: Función Logarítmica y Función Exponencial.",
"Guía resumen N°2 de la primera unidad: Funciones Exponencial y Logarítmica.",
"Prueba 2 (25% de relevancia)",
"Guía de ejercicios N°6: Funciones Trigonométricas",


"Guía de ejercicios N°6: Funciones Trigonométricas",
"Guía de ejercicios N°6: Funciones Trigonométricas",
"Guía de ejercicios N°7: Aplicaciones de las funciones trigonométricas.",
"Guía de ejercicios N°7: Aplicaciones de las funciones trigonométricas.",


"Guía de ejercicios N°7: Aplicaciones de las funciones trigonométricas.",
"Guía de ejercicios N°7: Aplicaciones de las funciones trigonométricas. Cuestionario 3 en AVA (5%)",
"Guía resumen de la segunda unidad: Funciones trigonométricas y aplicaciones",
"Prueba 3 (30% de relevancia)",

"Síntesis de la asignatura",
"Síntesis de la asignatura",
"Síntesis de la asignatura",
"Síntesis de la asignatura",

"Síntesis de la asignatura",
"Síntesis de la asignatura"


]
algebra = [
     "Guía de ejercicios N°0: Ecuaciones de primer grado.",
     "Guía de ejercicios N°0: Ecuaciones de primer grado.",
     "Guía de ejercicios N°0: Ecuaciones de primer grado.",
     "Guía de ejercicios N°0: Ecuaciones de primer grado.",
     
     "Guía de ejercicios N°1: Funciones lineales.",
     "Guía de ejercicios N°1: Funciones lineales.",
     "Resolución de problemas 1 (5% de relevancia)",
     "Guía de ejercicios N°1: Funciones lineales.",

    "Guía de ejercicios N°1: Funciones lineales.",
    "Guía resumen N°1 de la primera unidad: Funciones lineales",
    "Prueba 1 (26% de relevancia)",
    "Guía de ejercicios N°2: Funciones cuadráticas.",

    "Guía de ejercicios N°2: Funciones cuadráticas.",
    "Guía de ejercicios N°2: Funciones cuadráticas.",
    "Guía de ejercicios N°2: Funciones cuadráticas.",
    "Resolución de problemas 2 (5% de relevancia)",

    "Guía de ejercicios N°3: Funciones lineales y cuadráticas",
    "Guía de ejercicios N°3: Funciones lineales y cuadráticas",
    "Guía resumen N°2 de la primera unidad: Funciones lineales y cuadráticas",
    "Prueba 2 (28% de relevancia)",

    "Guía de ejercicios N°4: Función exponencial",
    "Guía de ejercicios N°4: Función exponencial",
    "Guía de ejercicios N°4: Función exponencial",
    "Resolución de problemas 3 (5% de relevancia)",

    "Guía de ejercicios N°5: Función exponencial y logarítmica.",
    "Guía de ejercicios N°5: Función exponencial y logarítmica.",
    "Guía de ejercicios N°5: Función exponencial y logarítmica.",
    "Resolución de problemas 4 Nota de ET Práctico (15% de relevancia)",

    "Repaso general unidad II Guía resumen de la segunda unidad: Funciones exponenciales y logarítmicas.",
    "Prueba 3 (31% de relevancia)",
    "Síntesis de la asignatura",
    "Síntesis de la asignatura",

    "Síntesis de la asignatura",
    "Síntesis de la asignatura"



     ]
calculo_diferencial = []
matematica_aplicada = [
"Guía de ejercicios N°01: Sucesiones.",
"Guía de ejercicios N°01: Sucesiones.",
"Guía de ejercicios N°01: Sucesiones.",
"Guía de ejercicios N°01: Sucesiones.",

"Guía de ejercicios N°02: Sumatorias.",
"Guía de ejercicios N°02: Sumatorias.",
"Guía de ejercicios N°02: Sumatorias.",
"Guía de ejercicios N°03: Matrices. Cuestionario 1 en AVA (10% de relevancia)",

"Guía de ejercicios N°03: Matrices",
"Guía de ejercicios N°03: Matrices",
"Guía de ejercicios N°04: Aplicaciones de las matrices",
"Guía de ejercicios N°04: Aplicaciones de las matrices",

"Guía de ejercicios N°04: Aplicaciones de las matrices",
"Guía de ejercicios N°04: Aplicaciones de las matrices. Cuestionario 2 en AVA(10% de relevancia)",
"Guía resumen de la Unidad I: Arreglos y bucles",
"Prueba 1 (35% de relevancia)",

"Guía de ejercicios N°05: Concepto de Función.",
"Guía de ejercicios N°05: Concepto de Función.",
"Guía de ejercicios N°06: Función Lineal.",
"Guía de ejercicios N°06: Función Lineal.",

"Guía de ejercicios N°06: Función Lineal.",
"Guía de ejercicios N°07:Función cuadrática.",
"Guía de ejercicios N°07:Función cuadrática.",
"Guía de ejercicios N°07:Función cuadrática.",

"Guía de ejercicios N°07: Función cuadrática.",
"Guía de ejercicios N°07: Función cuadrática.Cuestionario 3 en AVA (10% de relevancia) ",
"Guía resumen de la Unidad II: Funciones lineal y cuadrática.",
"Prueba 2 (35% de relevancia)",

"Síntesis de la asignatura",
"Síntesis de la asignatura",
"Síntesis de la asignatura",
"Síntesis de la asignatura",

"Síntesis de la asignatura",
"Síntesis de la asignatura"

]

hoja_de_ruta = algebra_y_trigonometria
lista =[]
t = timedelta(days=1)
while(inicio<=final):
    if inicio.strftime("%A") in dias_de_clase:
        lista.append(inicio)
    if inicio in feriados:
        print(inicio)
    inicio = inicio + t
i=0
for x in lista:
    if x in feriados:
        print(f'{x.day}/{x.month}/{x.year} FERIADO')
    else:
        print(f'{x.day}/{x.month}/{x.year} {hoja_de_ruta[i]}')
        i=i+1


