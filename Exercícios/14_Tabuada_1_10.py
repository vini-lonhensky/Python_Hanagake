'''
Nome : Vinicius R.P.
Data : 13/06/2024
Algoritimo : Tabuada
Descrisão : Façaum programa que aprecente a tabuada do 1 ao 10;
'''
#============================================================================================
# Variavel
# tendo o 
a = 1
numero = 0
print('\n')
print('\n')
print('Aqui está sua Tabuda do 1 ao 10')

for numero in range(1,11): # Partino do 0 até 10
    print('\n')
    print('======================================')
    print('\n')
    for a in range(11):
        print(f'{numero} X {a} = {numero * a}')
