'''
Autor: Vinicius R. P. da Silva
Data: 06/06/202
Versão: 7.0
Algoritimo: "Tipo triâgulo"
Descrição   : Faça uma programa que receba 3 valorese verifique se eles podem representar os
              lados em um triangulo;

                1-Triângulo Escaleno: triângulo que possui todos os lados com medidas diferentes;
                2-Triângulo Isóceles: triânguloque que possui todos os lados com medidas iguais;
                3-Triângulo Equilatero: triângulo que possui todos os lados com medidas iguais;
    Lembrando que a soma das medidas de dois lados de um triângulo é sempre maior que a medida do 
    terceiro lado.
'''
#============================================================================================
#variavel
a = 0
b = 0
c = 0
tipo = ''
#entrada 
#Ctrl + Alt + Shift + (direcionais up down)
a = int(input('insira o valor a:'))
b = int(input('insira o valor b:'))
c = int(input('insira o valor c:'))
#processamento

if((a + b) > c and 
   (a + c) > b and 
   (b + c) > a and 
   a > 0 and b > 0 and c > 0):
    print('Triângolo Existe')
    if(a == b and b == c):
        tipo ='trianuglo Equilatero'
    elif (a == b or a == c or b == c):
        #Como existiu a verificação co ''if'' anterior que um dos lados não são iguais,
        #Não existe a necessidade  da verificação do terceiro lado como diferente.
        tipo = 'Triângulo Isóceles'
    elif(a != b and a != c and b != c):
        tipo ='Triângulo Escaleno'
else:
    print('Triângulo não existe')
#saida
print(tipo)