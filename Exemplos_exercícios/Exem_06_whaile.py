'''
Autor: Vinicius R. P. da Silva
Data: 06/06/202
Versão: 7.0
Algoritimo: Estudo da estrutura de reperição "While "
Descrição   :Estudo da estrutura de reperição "While "


'''

'''
#============================================================================================
#variavel
indice = 1
while indice < 6:
    print('Eu amo a Sophie',indice)
    indice = indice + 1  # indece += 1
#============================================================================================
indice_1 = 1
while indice_1 < 23:
    print(indice_1)
    indice_1 = indice_1 + 1
#============================================================================================
indice_2 = 10
while indice_2 < 0:
    print('Vinicius R. P.',indice_2)
    indice_2 = indice_2 + 1
#============================================================================================
indice_3 = 1
while True:
    print(indice_3)
    indice_3 = indice_3 + 1
    if indice_3 == 5:
        break
#============================================================================================
# '''

indice_4 = 1
while True:
    opcao = input('Digiti S parapara finalizar o programa: ')
    if opcao == 'S' or len(opcao) > 5:
        break
