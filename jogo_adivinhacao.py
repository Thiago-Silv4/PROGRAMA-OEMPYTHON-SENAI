import random
numero_da_sorte = random.randint(1,1000)
meu_numero = int(input('Digite seu número da sorte: '))

if  numero_da_sorte == meu_numero:
    print('VOCÊ E SORTUDO (A), ACERTOU EM CHEIO * . *', 'O Nº É',numero_da_sorte )
else:
    print('VOCÊ ERROU FEIO, NÃO SOUBE ESCOLHER :p o N° É', numero_da_sorte)
    