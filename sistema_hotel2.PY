banco_dados = {}

nome = input('Nome: ')
idade = input('Idade: ')
senha = input('Senha: ')

nome2 = input('Nome: ')
idade2 = input('Idade: ')
senha2 = input('Senha: ')
               
nome3 = input('Nome: ')
idade3 = input('Idade: ')
senha3 = input('Senha: ')
               
banco_dados['nomes'] = [nome, nome2, nome3]
banco_dados['idades'] = [idade, idade2, idade3]
banco_dados['senhas'] = [senha, senha2, senha3]

print(banco_dados)

# ACESSO

login_nome = input('Digite seu nome >> ')
senha_acesso = input('Digite sua senha >> ')

if login_nome in banco_dados['nomes'] and senha_acesso in banco_dados['senhas']:
  print('Seja bem vindo ao sistema!')
  
  print('Escolha o quarto:',banco_dados['nomes'][0])
  quartos = ['','simples', 'duplo', 'luxo']
  valores = [100,150,250]
  print('quartos: ',quartos)
  escolha = int(input('id 1 simples | id 2 duplo | id 3 luxo'))
  qd = int(input('Quantidade de dias '))
  calculo = qd * valores[escolha]
  print('R$' , calculo)
  print('Vocês escolheu o quarto',quartos[escolha],'Quant. Dias',qd)
  print('Total a pagar R$', calculo)
  
  print('Escolha o quarto:',banco_dados['nomes'][1])
  quartos = ['','simples', 'duplo', 'luxo']
  valores = [100,150,250]
  print('quartos: ',quartos)
  escolha = int(input('id 1 simples | id 2 duplo | id 3 luxo'))
  qd = int(input('Quantidade de dias '))
  calculo = qd * valores[escolha]
  print('R$' , calculo)
  print('Vocês escolheu o quarto',quartos[escolha],'Quant. Dias',qd)
  print('Total a pagar R$', calculo)
           
  print('Escolha o quarto:',banco_dados['nomes'][2])
  quartos = ['','simples', 'duplo', 'luxo']
  valores = [100,150,250]
  print('quartos: ',quartos)
  escolha = int(input('id 1 simples | id 2 duplo | id 3 luxo'))
  qd = int(input('Quantidade de dias '))
  calculo = qd * valores[escolha]
  print('R$' , calculo)
  print('Vocês escolheu o quarto',quartos[escolha],'Quant. Dias',qd)
  print('Total a pagar R$', calculo)
           
else:
  print('Acesso negado,tente novamente!')

