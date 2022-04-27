import re  
ruta = "datos.txt"
archivo = open(ruta, mode ='r', encoding="utf-8") 
archivo2 = open('resultado.txt', mode = 'w', encoding = 'utf-8')
for x in archivo.readlines():
    if(x!="\n"):
        archivo2.write(x)

becquer = """26/3/2022 Repaso derivadas. Guía N°1
29/3/2022 Antiderivación e integrales Guía N°2
2/4/2022 Antiderivación e integrales Guía N°2
5/4/2022 Métodos de integración Guía N°3
9/4/2022 Métodos de integración Guía N°3
12/4/2022 Aplicaciones integrales indef. Guía N°4
16/4/2022 FERIADO
19/4/2022 Aplicaciones integrales indef. Guía N°4
23/4/2022 Evaluación: TALLER 1 (5% de relevancia)
26/4/2022 Guía Resumen Prueba 1.
30/4/2022 Evaluación: PRUEBA N°1 (25 % de relevancia)
3/5/2022 Teorema fundamental del cálculo Guía N°5
7/5/2022 Significado geométrico de la integral definida Guía N°6
10/5/2022 Significado geométrico de la integral definida Guía N°6
14/5/2022 Aplicaciones de las integrales definidas Guía N°7
17/5/2022 Evaluación: TALLER 2 (5% de relevancia)
21/5/2022 FERIADO
24/5/2022 Guía Resumen Prueba 2.
28/5/2022 Evaluación: PRUEBA N°2 (25 % de relevancia)
31/5/2022 Ecuaciones diferenciales ordinarias Guía N°8
4/6/2022 Ecuaciones diferenciales ordinarias Guía N°8
7/6/2022 Ecuaciones diferenciales de variables separables Guía N°9
11/6/2022 Ecuaciones diferenciales de variables separables Guía N°9
14/6/2022 Ecuaciones diferenciales lineales de primer orden Guía N°10
18/6/2022 Ecuaciones diferenciales lineales de segundo orden homogéneas con coeficientes constantes. Guía N°11
21/6/2022 FERIADO
25/6/2022 Evaluación: TALLER 3 (5% de relevancia)
28/6/2022 Guía Resumen Prueba 3
2/7/2022 Evaluación: PRUEBA N°3 (35 % de relevancia)"""
separacion_lineas=re.split(r'\n', becquer)

for x in separacion_lineas:
   print(re.match('\d{1,2}\/\d{1,2}\/2022',x).group(0))
