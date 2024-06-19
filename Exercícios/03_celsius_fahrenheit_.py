#===================================================================================================
#Autor: Vinicius RP
#Data: 24/05/24     28/05/24
#Versão: 5.0
#Descrição: Faça um algoritimo que receba a te,peratura em,
#           ºC e convertapara ºF ºK
#           ---------------------------------------------------
#           Exemplo de execução  
#           insira a temperatura em Celsio: 0
#           Fahrenheit: 32ºF
#           Kelvin: 273,15 K
#===================================================================================================
#Variavel 
Celsio = 0 #temperatura em Celsio inserida pelo usuario
Fahrenheit = 0 #temperatura em Fahrenheit vinda da conversão
Kelvin = 0 #temperatura em Kelvin  vinda da conversão
#Inicio
#Entrada
Celsio = float(input('insira valor em C:'))
#Processo
Fahrenheit = (Celsio * (9 / 5) )+ 32
Kelvin = (Fahrenheit - 32)  * (5 / 9) +273.15
#Saída
print('O resultado em Celsio é:', Celsio,'°C')
print('O resultado em fahrenheit é:', Fahrenheit,'°F')
print('O resultado em Kelvin é:', Kelvin,'°K')
#Fim