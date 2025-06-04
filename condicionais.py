idade = int(input('Idade: '))
# condicional simpes ***
if idade >= 16:
    print('Voce pode votar')
    
if idade <=16:
    print('Não pode votar')
    
if idade >=65:
    print('Não precisa votar')
    
#-----------------//-------------

idade = int(input('Digite sua idade: '))
titulo_eleitor = input('Possui Titulo de eleitor? s ou n')

if idade >= 16 and titulo_eleitor == 's':
    print('Pode votar')
else:
    print('Voce não pode votar')
    
# ---------------------//----------

ingresso_show_latitude10 = input('Ingresso com desconto? sim/não')


if ingresso_show_latitude10 =='sim' or ingresso_show_latitude10 =='não':
    print('Acesso autorizado!')
else:
    print('Acesso não autorizado')
    
#-------------------//--------------
    
idade = int(input('Idade: '))

if idade <=12:
    print('Criança')
elif idade >12 and idade <=14:
    print('pré - Adolescente')
elif idade >=15 and idade <=17:
    print('Adolescente')
elif idade > 18 and idade <=25:
    print('Jovem')
elif idade >25 and idade <=64:
    print('Adulto')
else:
    print('Idoso(a)')
