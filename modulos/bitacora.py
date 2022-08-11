import re
def crear_bitacora(nombre_asignatura,sección,lista_bitacora,unidades):
    i=0
    for x in lista_bitacora:
        inicio=f'Bitacora {x[0]}\n'
        unidad =unidades[i]+'\n'
        objetivo =unidades[i+1]+'\n'

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
        i=i+2