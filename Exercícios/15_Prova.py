'''
Descrição : 1Faça um programa que receba dois valores, sendo que o            
            primeiro deve ser menor que o segundo.
            o programa deve ser apresentar todos os números ímpares
            contidos nesta sequeêcia.
            (modulo %. Exemplo: 7%2 = 1)
'''
#============================================================================================
# Variavel
vs = 0
ts = 0

vs = int(input('insira o valor um:'))
ts = int(input('insira o valor dois:'))

for v in range(vs , ts):
    resto = v % 2
    if v % 2 ==1:
        print(resto)
        print(f'{v} % 2 = {resto}')


