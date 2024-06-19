#===================================================================================================
#Autor: Vinicius RP
#Data: 24/05/24
#Versão: 4.0
#Descrição: Faça um algoritimo que um valor na moeda Real (R$),
#           a cotação da conversão REAL para DOLAR, e apresente 
#           aquantidade desse valor em Dolar($):
#           ---------------------------------------------------
#           Exemplo de execução  
#           insira o valor em real: 500
#           insira cotação do dia: 5 
#           R$5000,00 equivalem 1000,00
#===================================================================================================
#variaveis
real = 0 #receb o valor em reais
cotacao = 0 #valor da cotação 1 Xreais
dolar = 0 #valor convertido em dólar
#Inicio
#Entrada
print('===================================================')
#necessario  fazer o casting (conversão de tipos de dados)
#float <= '5000'
real = float(input('Insira o valor em reais (R$): '))
cotacao = float(input('Insira valor da cotação: '))
#Processo
dolar = real / cotacao
#Saída
print('O resultado em dolár é:', dolar)

print('===================================================')
#Fim