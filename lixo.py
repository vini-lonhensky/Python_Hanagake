
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
    #Entrada

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
