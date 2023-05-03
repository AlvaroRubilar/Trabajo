import re
import os
import locale
from datetime import date
from datetime import datetime, timedelta
locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
def crear_hoja(asignatura,dia1,dia2,opcion,validacion):
   
    inicio = datetime(2023, 3, 6)
    final = datetime(2023, 7, 8)
    dias_de_clase = [dia1, dia2]
    jueves_santo = datetime(2023, 4, 6)
    

    feriados = [
        datetime(2023, 4, 7),
        datetime(2023, 4, 8),
       datetime(2023, 4, 28),
       datetime(2023, 4, 29)
        datetime(2023, 5, 1),
        datetime(2023, 6, 21),
        datetime(2023, 6, 26),
       ]
    if validacion:
        feriados.append(jueves_santo)
    
    t = timedelta(days=1)

    if opcion == 1:
        archivo = open(asignatura+'.txt', 'r', encoding='utf-8')
    else:
        archivo = open(asignatura+'2.txt', 'r', encoding='utf-8')
    lista_archivo=archivo.readlines()
    for k in range(len(lista_archivo)):
        lista_archivo[k] = lista_archivo[k].rstrip("\n")
    fechas =[]
    #print(lista_archivo)
    t = timedelta(days=1)
        
    while(inicio<=final):
        if inicio.strftime("%A") in dias_de_clase:
            fechas.append(inicio)

        inicio = inicio + t


    i=0
    lista1 = []
    lista2 = []
    for x in fechas:
        if x in feriados:
            lista1.append(f'{x.day}/{x.month}/{x.year} FERIADO')
            lista2.append([f'{x.day}/{x.month}/{x.year}','FERIADO'])
        else:
            lista1.append(f'{x.day}/{x.month}/{x.year} {lista_archivo[i]}')
            lista2.append([f'{x.day}/{x.month}/{x.year}' ,f'{lista_archivo[i]}'])
            i=i+1
      
    return [lista1,lista2]
