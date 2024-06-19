'''
Nome : Vinicius R.P.
Data : 13/06/2024
Algoritimo : Tabuada
Descrisão : Façaum programa que calcule a tabuada de um numero digitado
            pelo usuario;
'''
#============================================================================================
# Variavel
t1 = 1
media = 0
while t1 <= 10:
    t0 = 0 

    numero =int(input('Digite seu número de 0 á 10:'))

    if(numero > 10):
        print('numero invalido')
        break

    for t0 in range(11):
        # Resultado = numero * t0
        #print(numero, 'X', t0, '=' ,numero * t0)
        print(f'{numero} X {t0} = {numero * t0}')
       

#============================================================================================



