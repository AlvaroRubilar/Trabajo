from cgitb import text
import os

x=2
texto = f'''esto es
una prueba {x}'''
print(texto)



os.chdir("salida")
archivo = open(os.getcwd()+"/hola.txt","w")
dicionario ={

"Asignatura": "Álgebra", 
"Sección":"MAT2110-034V",
"Horario":[["martes","19:00-21:10"],["miércoles","21:10-22:30"]],
"Unidades":[
    ["Unidad 1: Funciones lineales y cuadráticas",
    "Competencia: resuelve problemas de fenómenos modelados por funciones lineales y cuadráticas, de acuerdo a requerimientos."],
    ["Unidad 2: Funciones exponenciales y logarítmicas",
    "Competencia: resuelve problemas de fenómenos modelados por funciones exponenciales y logarítmicas de acuerdo a requerimientos."]]
}
print(
f'''Asignatura: {dicionario["Asignatura"]}

Sección: {dicionario["Sección"]}

Horario

{dicionario["Horario"][0][0]}\t\t{dicionario["Horario"][1][0]}
{dicionario["Horario"][0][1]}\t{dicionario["Horario"][1][1]}

{dicionario["Unidades"][0][0]}
{dicionario["Unidades"][0][1]}

{dicionario["Unidades"][1][0]}
{dicionario["Unidades"][1][1]}
 ''')
def imprimir():
    print(f"imprime x = {x}")
imprimir()
