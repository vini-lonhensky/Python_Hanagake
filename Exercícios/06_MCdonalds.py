'''Autor: Vinicius RP
Data: 04/06/24
Versão: 8.0
Descrição   : Escreva um algoritimo para exibir o nome do lanche de acordo
             do número iserido pelo usuario, seguido a tela a baixo:
             
                    Nr.     Lanche
                    1       Big Mec
                    2       Quarterão
                    3       McChicken
                    4       Cheddar McMelt
                    5       McFish
                    
'''
#variavel
lanche = 0
#entrada
print('**************************************************************************************')
print('Nr. Lanche \n 1.Big Mec \n 2. Quarterão3 \n 3.McChicken \n 4.Cheddar McMelt \n 5.McFish')
lanche = int(input('Isira a opção desejada ?'))
#processo

if lanche == 1:
    print('Big Mec')
elif lanche == 2:
    print('Quarterão')
elif lanche == 3:
    print('McChicken')
elif lanche == 4:
    print('McMelt')
elif lanche == 5:
    print('McFish')
else:
    print('Opção invalida')
print('**************************************************************************************')