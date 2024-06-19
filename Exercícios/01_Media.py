#===================================================================================================
#Autor: Vinicius RP
#Data: 24/05/24
#Versão: 3.0
#descrição: Faça um algoritimo que receba 5 notas e imprima 
#           a media final do aluno
#           -----------------------------------------------
#           Exemplo de execução
#           Nota 1: 10
#           Nota 2: 10
#           Nota 3: 10
#           Nota 4: 10
#           Nota 5: 10
#           Média final: 10
#====================================================================================================
#Aluno 1---------------------------------------------------------------------------------------------
#inicio
#entrada
#casting => para converter o valor de string para inteiro 
#   5   = int ( ' 5 ' )
notaUm = int(input('insira a nota um:'))
notaDois = int(input('insira a nota dois:'))
notaTres = int(input('insira a nota tres:'))
notaQuatro =int(input('insira a nota quatro:'))
notaCinco = int(input('insira a nota cinco:'))
#processamento
media = (notaUm + notaDois + notaTres + notaQuatro + notaCinco) /5
#saída
print('a média do aluno é:', media)
#fim