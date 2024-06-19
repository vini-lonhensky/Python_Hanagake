'''Autor: Vinicius RP
Data: 28/05/24
Versão: 7.0
Descrição: Estudos do condicional IF ... ELSE
'''
#================================================================
#Variavel
nota = 0
#inicio
#entrada
nota = int(input('insira a nota um:'))

#processamento
if (nota >= 6):
    print('Aluno aprovado')
#saíd
elif(nota < 4):#if(nota < 6)
    print('Aluno reprovado')
else:
    print('Aluno em recuperação')
#fim
#================================================================