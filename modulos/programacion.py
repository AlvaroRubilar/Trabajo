import re
def crear_pagina(asignatura,nombre,seccion,dia1,hora1,dia2,hora2, lista_fechas):
    encabezado=f'''
    <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  
  <body class="container">
  
    
    '''
    pagina =[encabezado, f'<h1>Programación Semestral</h1>\n<h4>{nombre} {seccion}</h2>\n']
    tabla = f'''
     <p>
      <b>{dia1.capitalize()}:</b> {hora1} <br>
      <b>{dia2.capitalize()}:</b> {hora2} <br>
     </p>
      <p class="text-primary fw-bold">\n'''
    pagina.append(tabla)
    lista_anuncios = []
    j=1
    for x in lista_fechas:
        if re.findall('Prueba|Resolución|Cuestionario',x):
            pagina.append(f'<span class="text-danger fw-bold">{x}<br></span>\n')
            lista_anuncios.append(f'<span class="text-danger fw-bold">{x}<br></span>\n')
        else:
            pagina.append(f'{x} <br>\n')
            lista_anuncios.append(f'<span class="text-primary">{x} <br></span>\n')
    pagina.append('</p>\n</body>\n</html>')
    pagina_anuncios =[encabezado, f'<h1>Anuncios</h1>\n<h4>{nombre} {seccion}</h2>\n',tabla]
    for k in range(0,len(lista_anuncios),2):
      pagina_anuncios.append(
        f'''<h2>Semana {j} </h2>
        
        <p >Estimadas/os estudiantes:<br>
        Junto con saludar, esta semana veremos:<br><br>
        <b>{lista_anuncios[k]}
        {lista_anuncios[k+1]} </b><br><br>
        
        Nos vemos en clases<br>
        Álvaro Rubilar<br><br></p>
        ''')
      j = j+1
    pagina_anuncios.append('\n</body>\n</html>')
    archivo = open('programa_'+asignatura+seccion+'.html',"w",encoding="utf-8")
    archivo.writelines(pagina)
    archivo.close()
    archivo2 = open('anuncios_'+asignatura+seccion+'.html',"w",encoding="utf-8")
    archivo2.writelines(pagina_anuncios)
    archivo2.close()

