repetir = True

while repetir:
    respuesta = input('bienvenido al sistema para poder saber si el numero que tienes es par o impar, quieres darme un numero?')
    if respuesta in ['Si','si', 'SI', 'sI']:
        num = float(input('Ingresa un número:'))
        if num % 2 == 0:
            print('El número',num,'es par')    
        else: 
            print('El número',num,'es impar')
    elif respuesta in ['No', 'NO', 'nO', 'no']: 
        repetir = False
    else: 
        print('¿Podrías escribir si o no por favor?')

 




