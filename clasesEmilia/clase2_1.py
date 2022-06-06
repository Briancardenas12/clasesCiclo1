from traceback import print_tb


print('Algoritmo para comparar dos numeros')
print('Digite el primer numero')
num1=float(input())
print('Digite el segundo numero')
num2=float(input())

if num1>num2:
    print('El numero ingresado es mayor: ', num1, '>', num2)
elif num1<num2:
    print('El numero ingresado es mayor: ', num2, '>', num1)
else:
    print('Ambos numros son iguales')
