import locale
from datetime import date
from datetime import datetime,timedelta
locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
dt = datetime.now()
inicio=datetime(2021,3,15)
final = datetime(2021, 7,10)
dias_de_clase = ['lunes','viernes']
jueves_santo = datetime(2021,4,1)
validacion = True

feriados = [
            datetime(2021,4,2),
            datetime(2021,4,3),
            datetime(2021,5,1),
            datetime(2021,5,21),
            datetime(2021,6,28)]
if validacion:
    feriados.append(jueves_santo)
calculo2 =[
'Repaso de derivadas • Guía N°1',
'Repaso de derivadas • Guía N°1',
'Antiderivación e integrales . • Guía N°2',
'Antiderivación e integrales . • Guía N°2',
'Métodos de integración. • Guía N°3',
'Métodos de integración. • Guía N°3',
'Métodos de integración. • Guía N°3',
'Aplicaciones de las integrales indefinidas.  • Guía N°4',
'Aplicaciones de las integrales indefinidas.  • Guía N°4',
'Evaluación: Cuestionario 1 en AVA',
'Repaso Prueba 1 • Guía Resumen: Integrales indefinidas.',
'Evaluación: PRUEBA N°1',
'Teorema fundamental del calculo. • Guía N°5',
'Teorema fundamental del calculo. • Guía N°5',
'Significado geométrico de la integral definida. • Guía N°6',
'Significado geométrico de la integral definida. • Guía N°6',
'Aplicaciones de las integrales definidas. • Guía N°7',
'Evaluación: Cuestionario 2 en AVA',
'Repaso Prueba 2 • Guía Resumen: Integrales definidas.',
'Evaluación: PRUEBA N°2',
'Ecuaciones diferenciales ordinarias. • Guía N°8',
'Ecuaciones diferenciales ordinarias. • Guía N°8',
'Ecuaciones diferenciales de variables separables.• Guía N°9',
'Ecuaciones diferenciales de variables separables.• Guía N°9',
'Ecuaciones diferenciales lineales de primer orden. • Guía N°10',
'Ecuaciones diferenciales lineales de segundo orden homogéneas con coeficientes constantes. • Guía N°11',
'Ecuaciones diferenciales lineales de segundo orden homogéneas con coeficientes constantes. • Guía N°11',
'Evaluación: Cuestionario 3 en AVA',
'Repaso Prueba 3 • Guía Resumen: Ecuaciones diferenciales ordinarias.',
'Evaluación: PRUEBA N°3 (35 % de relevancia)',
'• Guía Repaso Examen.',
'• Guía Repaso Examen.',
'• Guía Repaso Examen.',
'• Guía Repaso Examen.']

mate_aplicada =[
'Guía N°01 - Sucesiones',
'Guía N°01 - Sucesiones',
'Guía N°01 - Sucesiones',
'Guía N°01 - Sucesiones',
'Guía N°02 - Sumatorias',
'Guía N°02 - Sumatorias',
'Guía N°02 - Sumatorias',
'Cuestionario N°1',
'• Guía N°03 - Matrices',
'• Guía N°03 - Matrices',
'• Guía N°03 - Matrices',
'• Guía N°04 - Aplicaciones de las matrices',
'• Guía N°04 - Aplicaciones de las matrices',
'• Guía N°04 - Aplicaciones de las matrices',
'• Guía N°04 - Aplicaciones de las matrices',
'Cuestionario N°2',
'Repaso General Unidad I Guía Resumen de la primera unidad: Arreglos y Bucles.',
'Evaluación: PRUEBA 1',
'Guía N°05 - Concepto de Función',
'Guía N°05 - Concepto de Función',
'• Guía N°06 - Función Lineal',
'• Guía N°06 - Función Lineal',
'• Guía N°06 - Función Lineal',
'• Guía N°07 - Función Cuadrática',
'• Guía N°07 - Función Cuadrática',
'• Guía N°07 - Función Cuadrática',
'• Guía N°07 - Función Cuadrática',
'Cuestionario N°3',
'Repaso General Unidad II Guía Resumen de la primera unidad: Funciones lineal y cuadrática.',
'Evaluación: PRUEBA 2',
'Síntesis de la Asignatura',
'Síntesis de la Asignatura',
'Síntesis de la Asignatura',
'Síntesis de la Asignatura'
]

formas_y_espacio = [

'Guía N°1 - Puntos, rectas, vértices y planos.',
'Guía N°2 - Planos y Escalas.',
'Guía N°3 - Perímetro y área de figuras planas.',
'Guía N°3 - Perímetro y área de figuras planas.',
'Síntesis de la Unidad 1: Geometría Plana. Guía de Repaso de la Unidad I Cuestionario 1 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°1 (30% de relevancia).',
'Guía N°4 - Superficie y volumen de cuerpos geométricos.',
'Guía N°4 - Superficie y volumen de cuerpos geométricos.',
'Síntesis de la Unidad 2: Geometría en el espacio. Guía de Repaso de la Unidad II Cuestionario 2 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°2 (25% de relevancia)',
'Guía N°5 - Rumbo y Asimut.',
'Guía N°6 - Teorema de Pitágoras.',
'Guía N°7 - Razones Trigonométricas',
'Guía N°7 - Razones Trigonométricas.',
'Síntesis de la Unidad 3: Ángulos y trigonometría. Guía de Repaso de la Unidad III Cuestionario 3 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°3 (30% de relevancia).',
'Guía de Repaso de la Asignatura Síntesis de las Unidades 1, 2 y 3'



]
formas_y_espacio2 = [

'Guía N°1 - Puntos, rectas, vértices y planos.',
'Guía N°2 - Planos y Escalas.',
'Guía N°3 - Perímetro y área de figuras planas.',
'Guía N°3 - Perímetro y área de figuras planas.',
'Síntesis de la Unidad 1: Geometría Plana. Guía de Repaso de la Unidad I Cuestionario 1 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°1 (30% de relevancia).',
'Guía N°4 - Superficie y volumen de cuerpos geométricos.',
'Guía N°4 - Superficie y volumen de cuerpos geométricos.',
'Síntesis de la Unidad 2: Geometría en el espacio. Guía de Repaso de la Unidad II Cuestionario 2 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°2 (25% de relevancia)',
'Guía N°5 - Rumbo y Asimut.',
'Guía N°6 - Teorema de Pitágoras.',
'Guía N°7 - Razones Trigonométricas',

'Síntesis de la Unidad 3: Ángulos y trigonometría. Guía de Repaso de la Unidad III Cuestionario 3 en AVA (asincrónico, 5% de relevancia)',
'Evaluación: PRUEBA N°3 (30% de relevancia).',
'Guía de Repaso de la Asignatura Síntesis de las Unidades 1, 2 y 3'



]

herramientas = [
'Guía 1	Conjuntos',
'Guía 1	Conjuntos',
'Guía 1	Conjuntos',
'Guía 2	Lógica proposicional.',
'Guía 2	Lógica proposicional.',
'Guía 2	Lógica proposicional.',
'Guía 2	Lógica proposicional.',
'Evaluación: CUESTIONARIO EN AVA N°1',
'Guía 2	Lógica proposicional.',
'Guía de Repaso de la Unidad I	Síntesis de la Unidad 1: Introducción a la Teoría de conjuntos, lógica y sus aplicaciones.',
'Evaluación: PRUEBA 1',
'Guía 3 	Números Complejos',
'Guía 3 	Números Complejos',
'Guía 3 	Números Complejos',
'Guía 4 	Aplicaciones de los numeros complejos en la electricidad',
'Guía 4 	Aplicaciones de los numeros complejos en la electricidad',
'Evaluación: CUESTIONARIO EN AVA N°2',
'Guía 4 	Aplicaciones de los numeros complejos en la electricidad',
'Guía de Repaso de la Unidad II	Síntesis de la Unidad 2:El conjunto de los números complejos y sus aplicaciones',
'Evaluación: PRUEBA 2',
'Guía 5	Matrices, conceptos básicos',
'Guía 5	Matrices, conceptos básicos',
'Guía 5	Matrices, conceptos básicos',
'Guía 6	Aplicaciones de matrices',
'Guía 6	Aplicaciones de matrices',
'Evaluación: CUESTIONARIO EN AVA N°3',
'Guía 6	Aplicaciones de matrices',
'Guía 6	Aplicaciones de matrices',
'Guía de Repaso de la Unidad III	Sintesis de la Unidad 3: Matrices y aplicaciones',
'Evaluación: PRUEBA N°3',
'Guía de Repaso de la Asignatura',
'Guía de Repaso de la Asignatura',
'Guía de Repaso de la Asignatura',
'Guía de Repaso de la Asignatura'
]
algebra_y_trigonometria = []
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
    "RPs Justificados Síntesis de la asignatura"



     ]
calculo_diferencial = []
matematica_aplicada = []
hoja_de_ruta = algebra
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


