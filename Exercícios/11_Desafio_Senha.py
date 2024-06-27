'''
Nome : Vinicius R.P.
Data : 07/06/2024

Descrisão : 
'''
#variavel

senha = '' # Var para receber a senha do usuario
sp = 'senai115' # Senha padrão do sistema
tentativas = 3 # Numerro de tentativa dpo acesso do sistema
while True:

   senha = input('digite asua senha: ')# senai115 => numeros com letras  então sem casting

   if senha == sp :
      print('Aceso liberado')
      break #quebra do loop
   else: 
      tentativas = tentativas - 1 # tentativas -= 1
      print('Acesso negado!')
      print('Você so tem mais ', tentativas, 'tentativas') 
   if tentativas <= 0:
      print('Sistema BLOQUEADO ')
      break
