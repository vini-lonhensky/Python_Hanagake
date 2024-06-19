'''
Algoritmo "Aumento de salário"
Autor: Vinicius R. P. da Silva
Data: 06/06/202
versão: 7.0
Descrição   : Faça um programa que receba o salário de um funcionário, calcule e mostre o
              novo salário, sabendo-se que:
                Salário < R$ 1000,00 aumento de 25%.
                Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
                Salário >= R$ 2000,00 aumento de 10%.

'''
#============================================================================================
#variavel
salario = 0 # canel style
salario_aumento = 0
porcentagem = ''
#entrada
salario = float(input('Por favor, insira o seu salario:'))
#processamento
if(salario < 1000):
    porcentagem = '25%'
    salario_aumento = salario * 1.25
elif(salario >= 1000 and salario_aumento < 2000):
    porcentagem = '15%'
    salario_aumento = salario * 1.25
elif(salario >= 2000):
    porcentagem = '15%'
    salario_aumento = salario * 1.25
salario_aumento = round(salario_aumento, 2)#funcao nativa do python para arredondar os valores
#saida
print('O se salario de', salario, 'sofreu um reajuste de', porcentagem, 'sendo agora de', salario_aumento)