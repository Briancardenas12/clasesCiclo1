def per(base:float, lado:float, altura: float):
    perimetro =lado*3
    area =altura*(base/2)
    '''
    El .format puede recibir mas de una sola variable, según la cantidad de corchtes que tenga
    se separan por las comas
    '''
    return 'El perimetro del triangiulo es: {} y el area del triangiulo es: {}'.format(perimetro, area)

base= float(input('Ingrese la base del triangiulo:'))
lado= float(input('Ingrese el lado del triangiulo:'))
altura= float(input('Ingrese la altura del triangiulo:'))

print(per(base, lado, altura))