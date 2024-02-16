"""

if 
if ... else
if ... elif .. else
if --> condicional : "entonces"
if variable == 2 :
    #Bloque de código que realizará si la condición se cumple (recuerda que es un true)
tambien se puede poner:
if not variable == 2: --> se procede con el bloque de código 
"""
variable = 6
if variable == 2 :
    print('tu variable es 2')

elif variable == 3 :
    print('Tu variable es 3')
else:
    print('Tu variable no es ni 2 ni 3')

print('programa finalizado')








""""
== doble simbolo de igual se tiene tal cual una comparativa de 2 datos iguales
<
> 
>=
<=
! 
!False --> True 
######## reservadas
not
not False --> True

is

condicionante = False
if condicionante is false: #Se procede
--> esto se convierte en true (por que en efecto tiene un valor False)
COSA IMPORTANTE IS se propone para validar el valor o el estatus de la ubicación en memoria ram 
esta es la principal diferencia entre == & is El == funciona para comparar los valores "reales" de las variables entre si 


Truthy & Falsy 

estos son los ejemplos que vimos en clase pasada 
"si un número entero es 0 entonces sería falso pero si es != 0 entonces es verdadero"
lo mismo pasa con las cadenas de texto.
"si una cadena de texto está vacía, entonces es falso '', en cambio si tiene algo --> se convierte en verdadero
para evaluarlo basta con hacer esto 
En flotantes pasa lo mismo que con los enteros (si es 0.0 queda false)

num1 = 0
num2 = 10

if num1:
    print('num1 es falsy') 
(como es falso no se cumple la condición, recuerda que solo se va a ejecutar el if cuando la condición sea verdadera)
if num2: 
    print('num2 es truthy)
(acá como num2 es != 0 entonces es true --> procede el if)

or y and 

if num1 or num2:
    print('num1 o num2 es truthy) 
    (esto si lo imprime por que es verdadero num2)

if num1 and num2:
    print('num1 y num2 es truthy)
    (Esto no lo imprime por que num1 es false)

"""
#while
#contador = 1
#while contador <= 10:
#    print('Contador es menor a 10', contador)
#    contador += 1 # es lo mismo que decir contador + 1

lista_de_koders = ["Jorge", "Luis", "Miren", "Julio", "Tao", "Irving"] 

#koder es una variable (siendo cada uno de los elementos en la colección que se van a iterar)
#"in" evalua que "algo" se encuientre en una colección de datos
#por cada koder en la lista de koders vamos a hacer lo siguiente: 

for koder in lista_de_koders:
    print('koder',koder) 

#tambien funciona con diccionarios 
    diccionario = {
        'nombre':'Alfredo',
        'edad':36,
        'ocupacion':'Mentor'
    }
#1 forma de hacerlo
    
for key in diccionario:
    print(key, ':', diccionario[key]) #estamos iterando las llaves y consultando el valor de la llave por cada iteración

#desempaquetado (se generan tuplas con 2 valores (x,y) asigandos por decir como key y value las cuales se generaron en una lista)
#Ocease que nos va a dar una lista de tuplas (x,y) por cada elemento iterado, en cambio si solo se tiene por decir 
#una variable (x) sin contar la "y" procederá a ejercer TODOS los elementos del objeto a una tupla creando tuplas individuales
#(x),(x),(x) asignando valor por valor, en este ejemplo sería ('nombre')('Alfredo').
#A diferencia que con (x,y) formando lo siguiente: ('nombre','Alfredo') Todo esto gracias al método .items()
    
for key, value in diccionario.items():
    print(key, ':', value)

#El in también se puede usar en un if para saber si un elemento determinado se encuentra en una colección de datos

#Cuando no se tiene una lista definida ocupamos la función range
#Va a crear un iterable por ejemplo 

#si yo hago solamente print(range(10)) por defecto lo hace del 0 al 10 

for i in range(10): #lo puedo poner con range(5,10) lo hace dek 5 al 10 
    print(i)

