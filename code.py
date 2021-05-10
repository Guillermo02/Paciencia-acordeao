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

def possui_movimentos_possiveis(new_baralho):
    i = 1
    for i in range(0,len(new_baralho)):
        carta = new_baralho[i]
        if len(carta)>2:
            valor = carta[0] + carta[1]
            naipe = carta[2]
        else:
            valor = carta[0]
            naipe = carta[1]
        if valor in new_baralho[i-1] or naipe in new_baralho[i-1]:
            return True
        if i>=4:
            if valor in new_baralho[i-3] or naipe in new_baralho[i-3]:
                return True
    else:
        return False


qr_jogar = input('Deseja jogar? (s)(n)')
while qr_jogar == 's':
    while len(new_baralho)>1 and possui_movimentos_possiveis(new_baralho) == True:
        #Enumera as opções
        for i,value in enumerate(new_baralho, 1):
            print(i,value)
        num_jog = int(input('Escolha uma carta: '))
        #Enquanto a carta escolhida for inválida...
        while num_jog>len(new_baralho) or num_jog<1:
            print('Carta inválida, selecione novamente')
            num_jog = int(input('Escolha uma carta: '))
        carta_jog = new_baralho[num_jog-1]
        opc = lista_movimentos_possiveis(new_baralho)

        if opc==[]:
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
            lista_valores[num_jog-4]= lista_valores[num_jog-1]
            lista_naipes[num_jog-4] = lista_naipes[num_jog-1]
            new_baralho[num_jog-4]  = new_baralho[num_jog-1]
            del(lista_valores[num_jog-1])
            del(lista_naipes[num_jog-1])
            del(new_baralho[num_jog-1])
        else:
            print('Você possui duas escolhas, a carta anterior (1) ou a terceira carta anterior (3)')
            esc = input('Qual sua escolha?: ')
            if esc == '1':
                del(lista_valores[num_jog-2])
                del(lista_naipes[num_jog-2])
                del(new_baralho[num_jog-2])
            else:
                lista_valores[num_jog-4] = lista_valores[num_jog-1]
                lista_naipes[num_jog-4]  = lista_naipes[num_jog-1]
                new_baralho[num_jog-4]   = new_baralho[num_jog-1]
                del(lista_valores[num_jog-1])
                del(lista_naipes[num_jog-1])
                del(new_baralho[num_jog-1])
    if possui_movimentos_possiveis(new_baralho) == False:
        print('Que pena você perdeu :(')
    else:
        print('Parabéns! Você venceu! :)')
    qr_jogar = input('Deseja jogar novamente? (s)(n)')

else:
    print('Obrigado por jogar!')     