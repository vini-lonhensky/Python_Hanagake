#================================================================
#Autor: Vinicius RP
#Data: 28/05/24
#Versão: 6.0
#Descrição: Faça um algoritimo que receba o raio em metros
#           de um circulo e apresete a sua Área: 
#           ---------------------------------------------------
#           Exemplo de execução  
#           insira o raio em metro: 5
#           Área do circulo: 78.5m^2
#           ---------------------------------------------------
#           
#           a = área
#           pi = 3.14
#           r = raio
#           a = pi*(r^2)
#           ---------------------------------------------------
#===============================================================
#Variavel 
# casting = float
r = 0 # raio
a = 0 # area
pi = 3.14 # contate pi
c = 0 #circulo
#Entrada
r = float(input('insira o Raio do circulo em metro: '))
#Processo
a = pi*(r**2)
#Fim
print('A Área do círculo é:', a,'m^2')
#===============================================================