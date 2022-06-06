def vel(tiempo:int, distancia:int):
    
    velacidad = distancia/tiempo
    '''
    .format, reemplaza el corchte {} por el nombre de la variable dque esta desués del format
    '''
    return 'La velocidad es: {} metros/segundos'.format(velacidad)

tiempo =int(input('Ingrese el tiempo (segundo): '))
distancia =int(input('Ingrese la distancia (metros): '))
'''
llama la función print y denrto esta la función vel, con sus dos parametros
'''
print(vel(tiempo, distancia))