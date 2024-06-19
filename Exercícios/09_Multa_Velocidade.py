'''
Autor: Vinicius R. P. da Silva
Data: 06/06/202
Versão: 7.0
Algoritimo : multa
Descrição   : Escreva um programa que laia a velocidade maxima permitida em 
              uma avenida e velocidade com que o motorista estava dirigindo nela e 
              clacule a multa que uma pessoa vai receber;
              
                Velocidade ultrapasada     Valor da Multa
                Até 10 Km/H                     R$ 50,00
                11 a 30 Km/H                    R$ 100,00
                Mais 31 Km/H                    R$ 200,00
'''
#============================================================================================
#variavel
limiteVelocidade = 0
velocidadedoMotorista = 0
diferencaVelocidade = 0
multa = ''
#entrada
limiteVelocidade = int(input('Insira o limite de velocidade da via: '))
velocidadedoMotorista = int(input('incira a velocidade do motorista: ') )
#processsamento
diferencaVelocidade = velocidadedoMotorista - limiteVelocidade
if(diferencaVelocidade > 0 and diferencaVelocidade<=10):
    multa = 'R$50,00'
elif(diferencaVelocidade >= 11 and diferencaVelocidade <=30):
    multa = 'R$100,00'
elif(diferencaVelocidade >= 31):
    multa = 'R$200,00'
else:
    multa = 'R$0,001'
#saida
print('A multa é de', multa, 'condutor irresponsável')