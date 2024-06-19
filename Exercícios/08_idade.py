'''
Algoritmo "Aumento de salário"
Autor: Vinicius R. P. da Silva
Data: 06/06/2024
versão: 8.0
algoritimo : ''Clacificação idade'' 
Descrição   : Escreva um programa que leia a idade de um individuo e
              escreva a fixa
'''
#============================================================================================
#variavel
idade = 0
classificacao = ''
#entrada
idade = int(input('Insira a sua idade: '))
#processamento
if(idade >= 0 and idade <= 12):
    classificacao = 'Criança'
elif(idade >= 13 and idade <= 17):
    classificacao = 'Adolecente'
elif(idade >= 18 and idade <= 59):
    classificacao = 'Adulto'
elif(idade > 59 ):
    classificacao = 'Adulto plus'
else:
    classificacao = 'Idade inserida invalida'
#saida
print(classificacao)
#============================================================================================