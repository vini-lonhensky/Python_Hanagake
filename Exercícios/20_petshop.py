'''
Nome : Vinicius R.P.
Data : 25/06/2024
Algoritimo : Senha
Descrisão : crie uma matriz e apresente ela no final da execuçao, aonde 
            existe duas colunas [Tipo, Nome] e 4 linhas preenchidos com 
            o tipo do animal e sue respequitivo nome

            # Tipo
'''
#=============================================================================


tabela_petshop =[
                    ['#', 'Tipo', 'Nome'],
                    ['0', 'Gato', 'Frajola'],
                    ['1', 'Cão', 'Coragem'],
                    ['2', 'Passarinho', 'pica-pau'],
                    ['3', 'Urso', 'Ursinho Pooh']

]

for linha in range(5):
    linha_completa = ''
    for coluna in range(3):
        linha_completa += tabela_petshop [linha] [coluna] +'|'
    
    print(f'{linha_completa}')