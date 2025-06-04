# Exercicio 1

usuario = int(input('Digite um número: '))
              
if usuario >=0:
    print('Esse número é positivo')
if usuario <=0:
    print('Esse número é negativo')
if usuario ==0:
    print('Esse número é igual a zero')
              
# Exercicio 2

idade = int(input('Idade: '))
              
if idade >= 16:
    print('Voce pode votar')
    
if idade <=16:
    print('Não pode votar')
    
if idade >=65:
    print('Não precisa votar')
              
# Exercicio 3
              
numero = 7

if numero % 2 == 0:
    print("O número não é par.")
else:
    print("O número impar.")
    
# Exercicio 4

lado1 = int(input('Digite o número primeiro lado: '))
lado2 = int(input('Digite o numero do segundo lado: '))
lado3 = int(input('Digite o numero do terceiro lado: '))

if lado1 == lado2 == lado3:
  print('equilatero')
  
if lado1 == lado2 != lado3:
  print('isóceles')
  
if lado1 != lado2 == lado3:
  print('isóceles')
  
if lado1 != lado2 != lado3:
  print('escaleno')
    
# Exercicio 5

num = 15

if num % 5 == 0 or num % 7 == 0:
    print('Esse numero é multiplo de 5 e 7')
else:
    print('Ele nao é multiplo de 5 e 7')
    
# Exercicio 6

num_positivo = 20

if num_positivo >= 10:
   print('Esse número é positivo e maior que 10')
else:
    print('O numero é mnenor que 10')
    
# Exercicio 7

num_divisivel = 10

if num_divisivel % 3 ==0 or num_divisivel % 5==0:
  print('Esse numero é divisivel por 3 e 5')
else:
    print('Esse numero não e divisivel por 3 e 5')