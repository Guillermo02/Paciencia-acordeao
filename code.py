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


