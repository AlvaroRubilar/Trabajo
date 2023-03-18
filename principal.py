import curso
import hoja_de_ruta as hr
import programacion as p
import bitacora as bt

lista_cursos =[curso.mat2120_003V]
for ramo in lista_cursos:
    x=list(ramo.values())

    asignatura = x[0]
    seccion = x[1]
    dia1 = x[2]
    hora1 = x[3]
    dia2 = x[4]
    hora2 = x[5]
    opcion = x[6]
    validacion = x[7]

    diccionario = curso.creacion_curso(
        asignatura, seccion, dia1, hora1, dia2,hora2)
    lista_fechas = hr.crear_hoja(asignatura,dia1,dia2,opcion,validacion)[0]
    lista_bitacora = hr.crear_hoja(asignatura,dia1,dia2,opcion,validacion)[1]
    p.crear_pagina(asignatura,diccionario["Asignatura"],seccion,dia1,hora1,dia2,hora2, lista_fechas)
    #print(diccionario["Unidades"])
    bt.crear_bitacora(asignatura,diccionario["Asignatura"],seccion,lista_bitacora,diccionario["Unidades"])

    # print(curso.mat2120_010V.values())