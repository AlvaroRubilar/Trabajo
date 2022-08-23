from math import e
import re
def crear_bitacora(asignatura,nombre_asignatura,seccion,lista_bitacora,unidades):
    i=0
    lista5 = ['# '+nombre_asignatura+' '+seccion+'\n']
    for x in lista_bitacora:
        inicio=f'## Bitácora {x[0]}\n\n'
        unidad =unidades[i][0]+'\n\n'
        objetivo =unidades[i][1]+'\n\n'

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
        if asignatura in ['algebra_y_trigonometria','algebra']:
            if re.findall('Prueba 2',x[1]):
                i=i+1
        if asignatura in ['calculo_diferencial','matematica_aplicada']:
            if re.findall('Prueba 1',x[1]):
                i=i+1
    bita = open('bitacora'+asignatura+'_'+seccion+'.md','w',encoding="utf-8")
    bita.writelines(lista5)
    bita.close()