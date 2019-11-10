from inicio import inicio
from desenho import forca
import palavras
import random
aleatorio = random.choice #atribuindo módulo a uma variável
categorias=[aleatorio(palavras.filmes()),aleatorio(palavras.animais())]#Sortea uma categoria aleatória.
newgame = 1
while newgame == 1: # Menu Principal
    jognov = 1
    inicio()
    print('\n1 - Novo jogo\n2 - Sair')
    newgame =  int(input('Selecione uma opção: '))
    if newgame == 1:
        vit = der = 0  # Reseta pontos
        nome = input('Nome do jogador: ') # Nome do novo jogador
        while jognov == 1:
            erros = 0 # reseta o número de erros
            #CAPTURA PALAVRA INICIAL
            print('Qual modo deseja jogar?\n  ')
            print('1 - Escolher palavra\n2 - Escolher uma categoria\n3 - Sortear uma categoria\n')
            modo = int(input('Selecione uma opção : '))
                # Escolhe palavra para acertarem.
            if modo == 1:
                word=input('\nInforme a palavra: ');
                temp=[]
                for letra in word:
                 if letra == ' ':
                    temp.append (' ')
                 else:
                    temp.append('_')
                #Permite o usuário escolher uma categoria.
            elif modo == 2:
                print('1 - Animais\n2 - Filmes')
                print('\n')
                categ = int(input('Selecione uma opção:  '))
                    # Seleciona uma palavra da categoria animais.
                if categ == 1:
                    word=aleatorio(palavras.animais())
                    temp=[]
                    for letra in word:
                        if letra == ' ':
                            temp.append (' ')
                        else:
                            temp.append('_')
                    # Seleciona uma palavra da categoria filmes.
                elif categ == 2:
                    word = aleatorio(palavras.filmes())
                    temp = []
                    for letra in word :
                        if letra == ' ' :
                            temp.append (' ')
                        else :
                            temp.append ('_')
                # Sortea uma categoria para jogar.
            elif modo == 3:
                categ = aleatorio(categorias)
                word=categ
                temp=[]
                for letra in word :
                    if letra == ' ' :
                        temp.append (' ')
                    else :
                        temp.append ('_')

            while True:

                print('\n'*20) # limpa a tela
                forca(erros,nome,vit,der) # imprime desenho da forca

                #imprime a adivinhacao
                print('\n\nAdivinhe: ', end='')

                for let in temp:
                    print(let, end=' ')
                print('\n'*2)

                #Verifica se perdeu
                if erros==6:
                    der+=1
                    break


                #Verificar se o jogador ganhou
                ganhouJogo=True
                for let in temp:
                    if let=='_':
                        ganhouJogo=False
                if ganhouJogo:
                    vit+=1
                    print('\nPARABÉNS VENCEDOR!!!')
                    break

                #captura a letra do usuario
                print ('2 - Desistir')
                letraDig=input('Informe uma letra:')
                if letraDig == '2':
                    der+=1
                    break

                #verifica se acertou alguma letra
                errouLetra=True
                for i, let in enumerate(word):
                    if word[i]==letraDig:
                        temp[i]=word[i]
                        errouLetra=False
                if errouLetra:
                    erros=erros+1

            print ('\nDeseja jogar novamente?')
            print ('1 - Continuar jogando  2 - Menu')
            jognov = int (input ('\nSelecione uma opção: '))

    else:
        break
