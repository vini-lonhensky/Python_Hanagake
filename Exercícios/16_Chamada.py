'''
Nome : Vinicius R.P.
Data : 14/06/2024
Algoritimo : 
Descrisão : Faça um programa que insira o numero da chamada do 
            aluno e apresente o nome dele?
'''
#============================================================================================
aluno =[
    'luana',
    'gustavo',
    'danielle',
    'felipe',
    'João',
    'thiago',
    'vitor',
    'josé',
    'arthur',
    'pedro',
    'mauricio',
    'davi',
    'kawan',
    'andrey',
    'lucas',
    'diego',
    'joão timão',
    'ana',
    'vinícius vasco',
    'adriel',
    'patrick',
    'bruno',
    'prfessor girafalles mini'
]
while True:
    alunos = 0
    alunos = int(input('Incira o número da chamada :'))
    print(aluno[alunos])
    continuar = input('Digite S para sair e C para continuar:')
    if continuar == 'S':
        break



