import random

#numeros =  ['2','3', '4' ,'5','6', '7','8','9','10','J','Q','K','A']
#naipes = ['♠','♣',' ♦','♥']

###Baralho inicial
baralho = ['A♥', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥','3♥', '2♥','A♠', 'K♠', 'Q♠', 'J♠', '10♠','9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠','A♦','K♦','Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♣', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣']

###Mistura o baralho
baralho_misturado = []
def cria_baralho():
    baralho_misturado = random.sample(baralho, len(baralho))
    return(baralho_misturado)
new_baralho = cria_baralho()


#########################################################################################################
###Lista de naipes
lista_naipes = []
for i in new_baralho:
    if len (i)>2:
        lista_naipes.append(i[2])
    else:
        lista_naipes.append(i[1])

###Lista de valores
lista_valores = []
for i in new_baralho:
    if len(i)==2:
        lista_valores.append(i[0])
    if len (i)>2:
        m = i[0]+i[1]
        lista_valores.append(m)

#########################################################################################################

#########################################################################################################

##Função que verifica possiveis movimentos
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
    if lista_valores[num_jog-2] in carta_jog or lista_naipes[num_jog-2] in carta_jog:
        sol1 = True
    if lista_valores[num_jog-4] in carta_jog or lista_naipes[num_jog-4] in carta_jog:
        sol2 = True

    if sol1 == True and sol2==True:
        return [1, 3]
    elif sol1 == True and sol2==False:
        return [1]
    elif sol1 == False and sol2==True:
        return [3]
    else:
        return []

###### Primeira Rodada ######
#Enumera as opções

qr_jogar = input('Deseja jogar? (s)(n)')
if qr_jogar == 's':
    while len(new_baralho)>1:
        for i,value in enumerate(new_baralho, 1):
            print(i,value)
        num_jog = int(input('Escolha uma carta: '))
        carta_jog = new_baralho[num_jog-1]
        opc = lista_movimentos_possiveis(new_baralho)
        print(lista_movimentos_possiveis(new_baralho))

        print(carta_jog)
        print(lista_valores[num_jog-2], lista_valores[num_jog-4])
        print(lista_naipes[num_jog-2], lista_naipes[num_jog-4])
        if opc == []:
            while opc == []:
                for i,value in enumerate(new_baralho, 1):
                    print(i,value)
                print('Esta carta não possui opções, selecione novamente')
                num_jog = int(input('Escolha uma carta: '))
                carta_jog = new_baralho[num_jog-1]
                opc = lista_movimentos_possiveis(new_baralho)
        if opc == [1]:
            print('Você so possui uma opção, a carta anterior. Esta será escolhida automaticamente')
            del(lista_valores[num_jog-2])
            del(lista_naipes[num_jog-2])
            del(new_baralho[num_jog-2])
        elif opc == [3]:
            print('Você so possui uma opção, a terceira carta anterior. Esta será escolhida automaticamente')
            del(lista_valores[num_jog-4])
            del(lista_naipes[num_jog-4])
            del(new_baralho[num_jog-4])
        else:
            print('Você possui duas escolhas, a carta anterior (1) ou a terceira carta anterior (3)')
            esc = input('Qual sua escolha?: ')
            if esc == '1':
                del(lista_valores[num_jog-2])
                del(lista_naipes[num_jog-2])
                del(new_baralho[num_jog-2])
            else:
                del(lista_valores[num_jog-4])
                del(lista_naipes[num_jog-4])
                del(new_baralho[num_jog-4])

else:
    print('Obrigado por jogar!')     


#while qr_jogar == 's':
    #qr_jogar = input('Deseja jogar? (s)(n)')
    #num_jog = int(input('Escolha uma carta e passe seu número equivalente: '))
#carta_jog = new_baralho[num_jog-1]
#print(carta_jog)


#while carta_jog != 'n':
    #lista_movimentos_possiveis(new_baralho)
    #carta_jog = input('Escolha uma carta: ')