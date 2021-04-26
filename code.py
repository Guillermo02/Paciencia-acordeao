import random

#criar baralho

numeros =  ['2','3', '4' ,'5','6', '7','8','9','10','J','Q','K','A']
naipes = ['♠','♣',' ♦','♥']

baralho = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥','A♠', 'K♠', 'Q♠', 'J♠', '10♠','9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠','A♦','K♦','Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']


def cria_baralho():
    baralho_misturado = random.sample(baralho, len(baralho))
    return(baralho_misturado)