'''
Nome : Vinicius R.P.
Data : 070/6/2024
Algoritimo : Média turma
Descrisão : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 4 e 7 	    Exame
                    De 8 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''
#============================================================================================
#Variavel
aluno = 0
alunos = 6
alunosaprovdos = 0
alunosreprovados = 0
alunosexame = 0
mediaf = 0
while aluno < alunos:
    aluno = aluno + 1
    # ALUDO XX
    nota = 0
    notadoius = 0
    media = 0
    nota = float(input(f'insira a nota um do aluno{aluno}:'))
    notadoius = float(input(f'insira a nota dois do aluno{aluno}:'))
    media =(nota + notadoius)  / 2
    mediaf = mediaf + media

    if(media >= 8):
        print('Aluno aprovado')
        alunosaprovdos += 1
    elif(media <=3):
        print('Aluno reprovado')
        alunosreprovados += 1
    elif(media >=3 and media <=7):
        print('Exame')
        alunosexame += 1

mediaf = round(mediaf / alunos)

print(f'Quantidade de alunos Aprovados:{alunosaprovdos}')
print(f'Quantidade de alunos Exames:{alunosexame}')
print(f'Quantidade de alunos Reprovados:{alunosreprovados}')
print(f'Média Final :', {mediaf})
    



