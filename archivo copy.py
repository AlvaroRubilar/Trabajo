import re
import os
import locale
from datetime import date
from datetime import datetime, timedelta
locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
dt = datetime.now()
inicio = datetime(2022, 8, 8)
final = datetime(2022, 12, 3)
dias_de_clase = ['martes', 'viernes']
sep_16 = datetime(2022, 9, 16)
validacion = True

feriados = [
    datetime(2022, 8, 15),
    datetime(2022, 9, 17),
    datetime(2022, 9, 19),
    datetime(2022, 10, 10),
    datetime(2022, 10, 31),
    datetime(2022, 11, 1)]
if validacion:
    feriados.append(sep_16)
lista = []
t = timedelta(days=1)
while(inicio <= final):
    if inicio.strftime("%A") in dias_de_clase:
        lista.append(inicio)
    # if inicio in feriados:
    #     print(inicio)
    inicio = inicio + t

archivo = open('algebra.txt', 'r', encoding='utf-8')
archivo2 = open('programa.html', 'w', encoding='utf-8')
archivo3 = open('anuncios.html', 'w', encoding='utf-8')
archivo4 = open('bitacora.txt', 'w', encoding='utf-8')
encabezado = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="font-family:Arial, Helvetica, sans-serif; color:blue; font-weight: bold;">
<h1 style="color:black;">Programación Semestral</h1>\n'''
archivo2.write(encabezado)
hoja_de_ruta = archivo.readlines()
# for x in hoja_de_ruta:
#     archivo2.writelines(x.rstrip('\n')+'<br><br>\n')
for k in range(len(hoja_de_ruta)):
    hoja_de_ruta[k] = hoja_de_ruta[k].rstrip("\n")

i = 0
lista2 = []
lista4 = []
exp = 'Prueba|Resolución'
for x in lista:
    if x in feriados:
        archivo2.writelines(f'{x.day}/{x.month}/{x.year} FERIADO <br><br>\n')
        lista2.append(f'<span style="color:blue;">{x.day}/{x.month}/{x.year} FERIADO</span>')
        lista4.append([f'{x.day}/{x.month}/{x.year}','FERIADO '])
    else:
        if re.findall(exp,hoja_de_ruta[i]):
            archivo2.writelines(
            f'<span style="color:red;">{x.day}/{x.month}/{x.year} {hoja_de_ruta[i]}<br><br></span>\n')
            lista2.append( f'<span style="color:red;">{x.day}/{x.month}/{x.year} {hoja_de_ruta[i]}</span>\n')
        else:
            archivo2.writelines(
            f'{x.day}/{x.month}/{x.year} {hoja_de_ruta[i]}<br><br>\n')
            lista2.append(f'<span style="color:blue;">{x.day}/{x.month}/{x.year} {hoja_de_ruta[i]}</span>')   
        lista4.append([f'{x.day}/{x.month}/{x.year}',hoja_de_ruta[i]])
        i = i+1

archivo2.writelines('</body>\n</html>')
archivo2.close()

i = 0
j = 1
encabezado2 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="font-family:Arial, Helvetica, sans-serif;">
<h1 style="color:black;">Anuncios</h1>\n'''
lista3=[encabezado2]
for k in range(0, len(lista2), 2):
    lista3.append(
        f'''<h2>Semana {j} </h2>
        
        <p>Estimadas/os estudiantes:<br><br>
        Junto con saludar, esta semana veremos:<br><br>
        <b>{lista2[k]}<br><br>
        {lista2[k+1]} </b><br><br>
        
        Nos vemos en clases<br><br>
        Álvaro Rubilar<br><br></p>
        ''')
    j = j+1
lista3.append('</body>\n</html>')
archivo3.writelines(lista3)
lista5 = []
unidades =['Unidad 1: Funciones','Unidad 2: Funciones trigonométricas y aplicaciones']
objetivos =['Competencia: resuelve problemas de fenómenos modelados por funciones elementales, de acuerdo a requerimientos.','Competencia: resuelve problemas de fenómenos modelados por funciones trigonométricas, de acuerdo a requerimientos.']
# for x in lista4:
#     inicio=f'''
# Bitacora {x[0]}
# Unidad: la unidad
# Objetivo: el objetivo'''
#     if re.findall('Prueba',x[1]):
#         centro=f'\nEvaluación: {x[1]}'
#     elif re.findall('Cuestionario',x[1]):
#         centro=f'\nActividades y Evaluación: resuelven {x[1]}'

#     else:
#         centro = f'\nActividades: resuelven {x[1]} '
#     lista5.append('\t'+inicio+centro+'\n\n')
#     i=0
for x in lista4:
    inicio=f'Bitacora {x[0]}\n'
    unidad =unidades[i]+'\n'
    objetivo = objetivos[i]+'\n'

    if re.findall('Síntesis|FERIADO',x[1]):
        centro =x[1]+'\n'
        lista5.append(inicio+centro+'\n\n')
    else:
        if re.findall('Prueba|Resolución',x[1]):
            centro=f'Evaluación: {x[1]}'
        elif re.findall('Cuestionario',x[1]):
            centro=f'Actividades y Evaluación: resuelven {x[1]}'

        else:
            centro = f'Actividades: resuelven {x[1]} '
        lista5.append(inicio+unidad+objetivo+centro+'\n\n')
    if re.findall('Prueba 2',x[1]):
        i=i+1
  
archivo4.writelines(lista5)