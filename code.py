import random

#numeros =  ['2','3', '4' ,'5','6', '7','8','9','10','J','Q','K','A']
#naipes = ['♠','♣',' ♦','♥']

#criar baralho
baralho = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥','A♠', 'K♠', 'Q♠', 'J♠', '10♠','9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠','A♦','K♦','Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

#Mistura o baralho
baralho_misturado = []
def cria_baralho():
    baralho_misturado = random.sample(baralho, len(baralho))
    return(baralho_misturado)

new_baralho = cria_baralho()
print(new_baralho)


#########################################################################################################
lista_naipes = []
for i in new_baralho:
    if len (i)>2:
        lista_naipes.append(i[2])
    else:
        lista_naipes.append(i[1])

print(lista_naipes)

##########################################################################################################

lista_valores = []
for i in new_baralho:
    if len(i)>1:
        lista_valores.append(i[0])
    if len (i)>2:
        m = i[0]+i[1]
        lista_valores.append(m)

print(lista_valores)

for i,value in enumerate(new_baralho, 1):
    print(i,value)

carta_jog = input('Escolha uma carta: ')
i = 50

def lista_movimentos_possiveis(new_baralho):
    sol1 = False
    sol2 = False
    if len(carta_jog)>2:
        valor = carta_jog[0] + carta_jog[1]
        naipe = carta_jog[2]
    else:
        valor = carta_jog[0]
        naipe = carta_jog[1]
    
    #Verifica valor e naipe
    if lista_valores[i-1] in carta_jog or lista_naipes[i-1] in carta_jog:
        sol1 = True
    elif lista_valores[i-3] in carta_jog or lista_naipes[i-3] in carta_jog:
        sol2 = True

    if sol1 == True and sol2==True:
        return [1, 3]
    elif sol1 == True and sol2==False:
        del(lista_valores[i-1])
        del(lista_naipes[i-1])
        del(new_baralho[i-1])
        return [1]
    elif sol1 == False and sol2==True:
        del(lista_valores[i-3])
        del(lista_naipes[i-3])
        del(new_baralho[i-3])
        return [3]
    else:
        return []
    print(new_baralho)
print(lista_movimentos_possiveis(new_baralho))

for i,value in enumerate(new_baralho, 1):
    print(i,value)
    
while carta_jog != 'n':
    lista_movimentos_possiveis(new_baralho)
    carta_jog = input('Escolha uma carta: ')