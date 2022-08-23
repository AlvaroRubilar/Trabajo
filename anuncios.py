import re
def crear_anuncios(asignatura,nombre,seccion,dia1,hora1,dia2,hora2, lista_fechas):
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
    pagina =[encabezado, f'<h1>Anuncios</h1>\n<h4>{nombre} {seccion}</h2>\n']
    tabla = f'''
     <p>
      <b>{dia1.capitalize()}:</b> {hora1} <br>
      <b>{dia2.capitalize()}:</b> {hora2} <br>
     </p>
      <p class="text-primary fw-bold">\n'''
    pagina.append(tabla)
    for x in lista_fechas:
        if re.findall('Prueba|Resolución|Curstionario',x):
            pagina.append(f'<span class="text-danger fw-bold">{x}<br></span>\n')
        else:
            pagina.append(f'{x} <br>\n')
    pagina.append('</p>\n</body>\n</html>')
    archivo = open('programa_'+asignatura+seccion+'.html',"w",encoding="utf-8")
    archivo.writelines(pagina)
    archivo.close()
