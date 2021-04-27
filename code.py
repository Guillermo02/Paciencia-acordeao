import random

#criar baralho

numeros =  ['2','3', '4' ,'5','6', '7','8','9','10','J','Q','K','A']
naipes = ['♠','♣',' ♦','♥']

baralho = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥','A♠', 'K♠', 'Q♠', 'J♠', '10♠','9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠','A♦','K♦','Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

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


jog = new_baralho[8]
i = 8
def lista_movimentos_possiveis(new_baralho):
    sol1 = False
    sol2 = False
    if len(jog)>2:
        valor = jog[0] + jog[1]
        naipe = jog[2]
    else:
        valor = jog[0]
        naipe = jog[1]
    
    #Verifica valor e naipe
    if lista_valores[i] == lista_valores[i-1] or lista_naipes[i] == lista_naipes[i-1]:
        sol1 = True
    elif lista_valores[i] == lista_valores[i-3] or lista_naipes[i] == lista_naipes[i-3]:
        sol2 = True

    if sol1 == True and sol2==True:
        return [1, 3]
    elif sol1 == True and sol2==False:
        return [1]
    elif sol1 == False and sol2==True:
        return [3]
    else:
        return []