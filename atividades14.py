# 3 - Verificando se uma string é vazia ou não 

letra = ''

match letra:
    case _:
        print('String Vazia')

# 4 - Verificando se um número é maior, menor ou igual a 10

numero = 10

match numero:
    case t if t > 10:
        print('Maior que 10')
    case t if t < 10:
        print('Menor que 10')
    case t if t == 10:
        print('Igual a 10')
        
   # Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)
   
   
idade =  int(input('idade: '))

match idade:
    case idade if idade ==12:
        print('É uma criança')
    case idade if idade ==17:
        print('É um adolescente')
    case idade if idade ==35:
        print('É um jovem')
    case idade if idade >35:
        print('É um adulto')
    case idade if idade >165:
        print('É um idoso')
       
   
   