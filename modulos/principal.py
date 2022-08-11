import curso
import hoja_de_ruta as hr
import programacion as p
import bitacora as bt
asignatura = 'algebra'
seccion = 'MAT2110-034V'
dia1 = "martes"
hora1 = "19:00-21:10"
dia2 = "miércoles"
hora2 = "21:10-22:30"
diccionario = curso.creacion_curso(
    asignatura, seccion, dia1, hora1, dia2,hora2)
lista_fechas = hr.crear_hoja(asignatura,dia1,dia2)[0]
lista_bitacora = hr.crear_hoja(asignatura,dia1,dia2)[1]
p.crear_pagina(asignatura,diccionario["Asignatura"],seccion,dia1,hora1,dia2,hora2, lista_fechas)
bt.crear_bitacora()

