# -*- coding:utf-8 -*-
'''
Delivered on 1/10/2019

@authors: Mário Varela & José Fernandes
'''
from cmd import *
from GandaGaloWindow import GandaGaloWindow
from GandaGaloEngine import GandaGaloEngine
import random


class GandaGaloShell(Cmd):
    intro = 'Interpretador de comandos para o GandaGalo. Escrever help ou ? para listar os comandos disponíveis.\n'
    prompt = 'GandaGalo> '

    def do_mostrar(self, arg):
        " -  comando mostrar que leva como parâmetro o nome de um ficheiro..: mostrar <nome_ficheiro> \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            global puzzle_name
            puzzle_name = str(arg)
            if num_args == 1:
                eng.ler_tabuleiro_ficheiro(lista_arg[0])
                eng.printpuzzle()
                x = eng.ler_tabuleiro_ficheiro(lista_arg[0])

                global janela  # pois pretendo atribuir um valor a um identificador global
                if janela is not None:
                    del janela  # invoca o metodo destruidor de instancia __del__()
                janela = GandaGaloWindow(40, eng.getlinhas(), eng.getcolunas())
                janela.mostraJanela(eng.gettabuleiro())
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao mostrar o puzzle")

    def do_abrir(self, arg):
        " - comando abrir que leva como parâmetro o nome de um ficheiro..: abrir <nome_ficheiro>  \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)

            global puzzle_name
            puzzle_name = str(arg)

            if num_args == 1:
                eng.ler_tabuleiro_ficheiro(lista_arg[0])
                eng.printpuzzle()
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao mostrar o puzzle")

    def do_gravar(self, arg):
        " - comando gravar que leva como parâmetro o nome de um ficheiro..: gravar <nome_ficheiro>  \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 1:
                file = open(arg, 'w')
                file.write(str(len(eng.gettabuleiro())) + ' ' + str(len(eng.gettabuleiro()[0])))
                for i in eng.gettabuleiro():
                    file.write('\n')
                    for j in i:
                        file.write(str(j))
                        file.write(' ')
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao gravar o puzzle")

    def do_jogar(self, arg):
        " - comando jogar que leva como parâmetro o caractere referente à peça a ser jogada (‘X’ ou ‘O’) e dois inteiros que indicam o número da linha e o número da coluna, respetivamente, onde jogar \n"
        try:
            lista_arg = arg.split(' ')
            num_args = len(lista_arg)
            if num_args == 3:
                x = eng.gettabuleiro()
                print(x)
                if lista_arg[2] in ['X', 'O', '.']:
                    if x[int(lista_arg[0]) - 1][int(lista_arg[1]) - 1] == '#':
                        print('Não é possível jogar numa casa bloqueada')
                    else:
                        x[int(lista_arg[0]) - 1][int(lista_arg[1]) - 1] = lista_arg[2]
                        eng.settabuleiro(x)
                        eng.printpuzzle()
                        eng.savejogadas([lista_arg[0], lista_arg[1], lista_arg[2]])
                        # janela = GandaGaloWindow(40, eng.getlinhas(), eng.getcolunas())
                        #janela.mostraJanela(eng.gettabuleiro())
                        print(eng.getjogadas())


                else:
                    print('Caracter não válido')
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao jogar")

    def do_validar_resolver(self, arg):
        " - comando validar que testa a consistência do puzzle e verifica se o tabuleiro está válido: validar \n"
        try:
            tempt = None
            galos = []
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 0:
                eng.validartabuleiro(arg)
            table = eng.gettabuleiro()
            for lp in range(len(table)):
                for cp in range(len(table)):
                    if table[lp][cp] != '#' and table[lp][cp] != '.':
                        if cp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp][cp + 1] == table[lp][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'horizontal'])
                                tempt = False

                            else:
                                tempt = True
                        if lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp] == table[lp + 2][cp]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'vertical'])
                                tempt = False

                            else:
                                tempt = True
                        if cp <= 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp + 1] == table[lp + 2][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_desc'])
                                tempt = False

                            else:
                                tempt = True
                        if cp + 1 >= len(table) - 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp - 1] == table[lp + 2][cp - 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_asc'])
                                tempt = False

                            else:
                                tempt = True
                        if cp > 1 and cp + 2 <= len(table) - 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp - 1] == table[lp + 2][cp - 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_asc'])
                                tempt = False

                            elif table[lp][cp] == table[lp + 1][cp + 1] == table[lp + 2][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_desc'])
                                tempt = False

                            else:
                                tempt = True
                        else:
                            continue

            else:
                return [galos, tempt]
        except:
            print("Erro ao validar o puzzle e/ou tabuleiro")

    def do_validar(self, arg):
        " - comando validar que testa a consistência do puzzle e verifica se o tabuleiro está válido: validar \n"
        try:
            tempt = None
            galos = []
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 1:
                eng.validartabuleiro(arg)
                print('Tabuleiro e caracteres válidos')
            table = eng.gettabuleiro()
            for lp in range(len(table)):
                for cp in range(len(table)):
                    if table[lp][cp] != '#' and table[lp][cp] != '.':
                        if cp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp][cp + 1] == table[lp][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'horizontal'])
                                tempt = False

                            else:
                                tempt = True
                        if lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp] == table[lp + 2][cp]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'vertical'])
                                tempt = False

                            else:
                                tempt = True
                        if cp <= 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp + 1] == table[lp + 2][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_desc'])
                                tempt = False

                            else:
                                tempt = True
                        if cp + 1 >= len(table) - 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp - 1] == table[lp + 2][cp - 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_asc'])
                                tempt = False

                            else:
                                tempt = True
                        if cp > 1 and cp + 2 <= len(table) - 1 and lp + 2 <= len(table) - 1:
                            if table[lp][cp] == table[lp + 1][cp - 1] == table[lp + 2][cp - 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_asc'])
                                tempt = False

                            elif table[lp][cp] == table[lp + 1][cp + 1] == table[lp + 2][cp + 2]:
                                print('Galo encontrado com origem na posição {},{}'.format(lp + 1, cp + 1))
                                galos.append([lp, cp, table[lp][cp], 'diag_desc'])
                                tempt = False

                            else:
                                tempt = True
                        else:
                            continue

                if not galos:
                    print('Não foram encontrados galos')


            else:
                print('último valor não testado.')
        except:
            print("Erro ao validar o puzzle e/ou tabuleiro")

    def do_ajuda(self, arg):
        " - comando ajuda que indica a próxima casa lógica a ser jogada (sem indicar a peça a ser colocada): ajuda  \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 0:
                janela.mostraJanela(eng.gettabuleiro())

                table = eng.gettabuleiro()
                count = 0
                for lp in range(len(table)):

                    for cp in range(len(table)):
                        if table[lp][cp] == 'X' or table[lp][cp] == 'O':
                            if cp + 2 <= len(table) - 1:
                                if table[lp][cp] == table[lp][cp+2]:
                                    if table[lp][cp+1] == '.':
                                        janela.desenhaLampada(cp+2,lp+1)
                                        count += 1

                                elif table[lp][cp] == table[lp][cp+1]:
                                    if table[lp][cp+2] == '.':
                                        janela.desenhaLampada(cp+3,lp+1)
                                        count += 1

                            if lp + 2 <= len(table) - 1:
                                if table[lp][cp] == table[lp+2][cp]:
                                    if table[lp+1][cp] == '.':
                                        janela.desenhaLampada(cp+1,lp+2)
                                        count += 1

                                elif table[lp][cp] == table[lp+1][cp]:
                                    if table[lp + 2][cp] == '.':
                                        janela.desenhaLampada(cp+1,lp+3)
                                        count += 1

                            if cp <= 1 and lp + 2 <= len(table) - 1:
                                if table[lp][cp] == table[lp + 2][cp + 2]:
                                    if table[lp+1][cp + 1] == '.':
                                        janela.desenhaLampada(cp + 2, lp + 2)
                                        count += 1

                                elif table[lp][cp] == table[lp + 1][cp + 1]:
                                    if table[lp+2][cp + 2] == '.':
                                        janela.desenhaLampada(cp + 3, lp + 3)
                                        count += 1

                            if cp + 1 >= len(table) - 1 and lp + 2 <= len(table) - 1:
                                if table[lp][cp] == table[lp + 2][cp - 2]:
                                    if table[lp + 1][cp -1] == '.':
                                        janela.desenhaLampada(cp, lp+2)
                                        count += 1
                                elif table[lp][cp] == table[lp + 1][cp - 1]:
                                    if table[lp + 2][cp -2] == '.':
                                        janela.desenhaLampada(cp - 1, lp + 3)
                                        count += 1

                            if cp > 1 and cp + 2 <= len(table) - 1 and lp + 2 <= len(table) - 1:
                                if table[lp][cp] == table[lp + 2][cp + 2]:
                                    if table[lp+1][cp + 1] == '.':
                                        janela.desenhaLampada(cp + 2, lp + 2)
                                        count += 1

                                elif table[lp][cp] == table[lp + 1][cp + 1]:
                                    if table[lp+2][cp + 2] == '.':
                                        janela.desenhaLampada(cp + 3, lp + 3)
                                        count += 1

                                if table[lp][cp] == table[lp + 2][cp - 2]:
                                    if table[lp + 1][cp -1] == '.':
                                        janela.desenhaLampada(cp, lp+2)
                                        count += 1
                                elif table[lp][cp] == table[lp + 1][cp - 1]:
                                    if table[lp + 2][cp -2] == '.':
                                        janela.desenhaLampada(cp - 1, lp + 3)
                                        count += 1

                        elif table[lp][cp] == '.':
                            if cp + 2 <= len(table) - 1:
                                if table[lp][cp+1] == 'O' and table[lp][cp+2] == 'O' or table[lp][cp+1] == 'X' and table[lp][cp+2] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                            if lp + 2 <= len(table) - 1:
                                if table[lp+1][cp] == 'O' and table[lp+2][cp] == 'O' or table[lp+1][cp] == 'X' and table[lp+2][cp] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                            if cp <= 1 and lp + 2 <= len(table) - 1:
                                if table[lp + 1][cp+1] == 'O' and table[lp + 2][cp+2] == 'O' or table[lp + 1][cp+1] == 'X' and table[lp + 2][cp+2] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                            if cp + 1 >= len(table) - 1 and lp + 2 <= len(table) - 1:
                                if table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                            if cp > 1 and cp + 2 <= len(table) - 1 and lp + 2 <= len(table) - 1:
                                if table[lp + 1][cp+1] == 'O' and table[lp + 2][cp+2] == 'O' or table[lp + 1][cp+1] == 'X' and table[lp + 2][cp+2] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                                elif table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    janela.desenhaLampada(cp + 1, lp + 1)
                                    count += 1
                if count == 0:
                    for lp in range(len(table)):
                        for cp in range(len(table)):
                            if [lp][cp] == '.':
                                janela.desenhaLampada(cp + 1, lp + 1)
            else:
                print('Erro nos argumentos')
        except:
            print("Erro ao sugerir ajuda")


    def do_undo(self, arg):
        " - comando para anular movimentos (retroceder no jogo): undo \n"
        try:
            if len(eng.getjogadas()) != 0:
                print(eng.getjogadas())
                jogada = eng.getjogadas().pop()
                print(jogada)
                self.do_jogar(jogada[0] + ' ' + jogada[1] + ' .')
                eng.removelast()
                print(eng.getjogadas())
            else:
                print('Nao há mais movimentos registados')
        except:
            print('Erro ao fazer undo')

    def do_resolver(self, arg):
        " - comando para resolver o puzzle: resolver \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args <= 1:
                self.do_ancora(puzzle_name)
                table = eng.gettabuleiro()
                for lp in range(len(table)):

                    for cp in range(len(table)):

                        " - 1ª Linha do gandagalo"
                        if lp == 0 and table[lp][cp] == '.':
                            if cp == 0:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp > 1 and cp + 2 <= len(table) - 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp + 1 == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                        # " - 2ª Linha do gandagalo"
                        elif lp == 1 and table[lp][cp] == '.':
                            if cp == 0:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp > 1 and cp + 2 <= len(table) - 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' or table[lp + 1][
                                    cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' or table[lp + 1][
                                    cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp + 1 == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' or table[lp + 1][
                                    cp + 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                        # linhas do meio
                        elif lp > 1 and lp + 2 <= len(table) - 1 and table[lp][cp] == '.':
                            if cp == 0:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp + 1][cp] == 'X' and \
                                        table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and  table[lp +1][cp] == 'X' or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X'\
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X' or table[lp - 1][cp+1] == 'X' and table[lp -2][cp+1] == 'X' :
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp + 1][cp] == 'O' and \
                                        table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and  table[lp +1][cp] == 'O' or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O'\
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O' or table[lp - 1][cp+1] == 'O' and table[lp -2][cp+1] == 'O' :
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp + 1][cp] == 'X' and \
                                        table[lp + 2][cp] == 'X' or table[lp + 1][cp + 1] == 'X' and table[lp + 2][
                                    cp + 2] == 'X' or table[lp - 1][cp] == 'X' and table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X' or table[lp - 1][
                                    cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp][cp - 1] == 'X' and table[lp][
                                    cp + 1] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp + 1][cp] == 'O' and \
                                        table[lp + 2][cp] == 'O' or table[lp + 1][cp + 1] == 'O' and table[lp + 2][
                                    cp + 2] == 'O' or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][
                                    cp] == 'O' and table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O' or table[lp][
                                    cp - 1] == 'O' and table[lp][cp + 1] == 'O' or table[lp - 1][cp - 1] == 'O' and \
                                        table[lp + 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp > 1 and cp + 2 <= len(table) - 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp - 2] == 'X' or table[lp][cp - 1] == 'X' and table[lp][cp + 1] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and table[lp + 1][cp] == 'X' \
                                        or table[lp + 1][cp + 1] == 'X' and table[lp + 2][cp + 2] == 'X' or table[lp - 1][
                                    cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' or table[lp - 1][cp - 1] == 'X' and \
                                        table[lp + 1][cp + 1] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X' or table[lp + 1][cp - 1] == 'X' and \
                                        table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp - 2] == 'O' or table[lp][cp - 1] == 'O' and table[lp][cp + 1] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and table[lp + 1][cp] == 'O' \
                                        or table[lp + 1][cp + 1] == 'O' and table[lp + 2][cp + 2] == 'O' or table[lp - 1][
                                    cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' or table[lp - 1][cp - 1] == 'O' and \
                                        table[lp + 1][cp + 1] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' or table[lp + 1][cp - 1] == 'O' and \
                                        table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp + 1 == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' or table[lp - 1][
                                    cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' or table[lp - 1][
                                    cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp + 1][cp] == 'X' and table[lp + 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp + 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp + 1][cp] == 'O' and table[lp + 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp + 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                        # PENULTIMA LINHA
                        elif lp == len(table) - 2 and table[lp][cp] == '.':
                            if cp == 0:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp > 1 and cp + 2 <= len(table) - 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' or table[lp - 1][
                                    cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X' or table[lp + 1][
                                    cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' or table[lp - 1][
                                    cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O' or table[lp + 1][
                                    cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp + 1 == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp + 1][cp + 1] == 'X' or table[lp - 1][
                                    cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp + 1][cp - 1] == 'X' and table[lp - 1][cp + 1] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp + 1][cp + 1] == 'O' or table[lp - 1][
                                    cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' \
                                        or table[lp + 1][cp - 1] == 'O' and table[lp - 1][cp + 1] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' or table[lp - 1][cp] == 'X' and \
                                        table[lp + 1][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' or table[lp - 1][cp] == 'O' and \
                                        table[lp + 1][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                        # ULTIMA LINHA
                        elif lp == len(table) - 1 and table[lp][cp] == '.':
                            if cp == 0:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp == 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X':
                                        self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O':
                                        self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp > 1 and cp + 2 <= len(table) - 1:
                                if table[lp][cp + 1] == 'X' and table[lp][cp + 2] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X' \
                                        or table[lp - 1][cp + 1] == 'X' and table[lp - 2][cp + 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp + 1] == 'O' and table[lp][cp + 2] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O' \
                                        or table[lp - 1][cp + 1] == 'O' and table[lp - 2][cp + 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp) + ' ' + str(cp))
                            elif cp + 1 == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp + 1] == 'X' or table[lp][cp - 1] == 'X' and \
                                        table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp + 1] == 'O' or table[lp][cp - 1] == 'O' and \
                                        table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                        x = str(random.choice(('O', 'X')))
                                        self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + x)
                            elif cp == len(table) - 1:
                                if table[lp][cp - 1] == 'X' and table[lp][cp - 2] == 'X' \
                                        or table[lp - 1][cp] == 'X' and table[lp - 2][cp] == 'X' \
                                        or table[lp - 1][cp - 1] == 'X' and table[lp - 2][cp - 2] == 'X':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                                elif table[lp][cp - 1] == 'O' and table[lp][cp - 2] == 'O' \
                                        or table[lp - 1][cp] == 'O' and table[lp - 2][cp] == 'O' \
                                        or table[lp - 1][cp - 1] == 'O' and table[lp - 2][cp - 2] == 'O':
                                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                                else:
                                    self.do_random(str(lp)+' '+str(cp))
                        play = self.do_validar_resolver(puzzle_name)
                        x = (play[1])
                        if x == False:
                                gplay = play[0][0]

                                if gplay[3] == 'vertical':
                                    if gplay[2] == 'X':
                                        for i in range(gplay[0], gplay[0] + 3):
                                            colp = str(gplay[1] + 1)
                                            i = str(i + 1)
                                            self.do_jogar(i + ' ' + colp + ' ' + 'O')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(i + ' ' + colp + ' ' + 'X')
                                        if check != 0:
                                            print('no solution for our algorithm')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                    if gplay[2] == 'O':
                                        for i in range(gplay[0], gplay[0] + 3):
                                            colp = str(gplay[1] + 1)
                                            i = str(i + 1)
                                            self.do_jogar(i + ' ' + colp + ' ' + 'X')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(i + ' ' + colp + ' ' + 'O')
                                        if check != 0:
                                            print('no solution for our algorithm for now')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                elif gplay[3] == 'horizontal':
                                    if gplay[2] == 'X':
                                        for i in range(gplay[1], gplay[1] + 3):
                                            linep = str(gplay[0] + 1)
                                            i = str(i + 1)
                                            self.do_jogar(linep + ' ' + i + ' ' + 'O')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + i + ' ' + 'X')
                                            if check != 0:
                                                print('no solution for our algorithm')
                                                self.do_undoancora('ancora')
                                                eng.resetjogadas()
                                                self.do_resolver(puzzle_name)
                                    elif gplay[2] == 'O':
                                        for i in range(gplay[1], gplay[1] + 3):
                                            linep = str(gplay[0] + 1)
                                            i = str(i + 1)
                                            self.do_jogar(linep + ' ' + i + ' ' + 'X')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + i + ' ' + 'O')
                                        if check != 0:
                                            print('no solution for our algorithm for now')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                elif gplay[3] == 'diag_asc':
                                    if gplay[2] == 'X':
                                        for i in range(3):
                                            linep = str(gplay[0] + 1 - i)
                                            colp = str(gplay[1] + 1 - i)

                                            self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                        if check != 0:
                                            print('no solution for our algorithm')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                    if gplay[2] == 'O':
                                        for i in range(3):
                                            linep = str(gplay[0] + 1 - i)
                                            colp = str(gplay[1] + 1 - i)
                                            self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                        if check != 0:
                                            print('no solution for our algorithm for now')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                elif gplay[3] == 'diag_desc':
                                    if gplay[2] == 'X':
                                        for i in range(3):
                                            linep = str(gplay[0] + 1 + i)
                                            colp = str(gplay[1] + 1 + i)

                                            self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                        if check != 0:
                                            print('no solution for our algorithm')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                    if gplay[2] == 'O':
                                        for i in range(3):
                                            linep = str(gplay[0] + 1 + i)
                                            colp = str(gplay[1] + 1 + i)
                                            self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                            newtry = self.do_validar_resolver(puzzle_name)
                                            check = len(newtry[0])
                                            if check == 0:
                                                print('Puzzle válido e resolvido')
                                                break
                                            else:
                                                self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                        if check != 0:
                                            print('no solution for our algorithm for now')
                                            self.do_undoancora('ancora')
                                            eng.resetjogadas()
                                            self.do_resolver(puzzle_name)
                                else:
                                    print('no solution for our algorithm for now')
                                    continue


                tempt = None
                args_val = self.do_validar_resolver(puzzle_name)
                print(args_val)
                x = len(args_val[0])
                print(x)
                if x == 0:
                    print('Puzzle válido e resolvido')
                    self.do_gravar('Solução_{}'.format(puzzle_name))
                    print('Solução guardada')
                elif x >= 4:
                    self.do_undoancora('ancora')
                    eng.resetjogadas()
                    self.do_resolver(puzzle_name)
                if x >= 1 and x<=3:
                    for values in args_val[0]:
                        eng.resetjogadas()
                        if values[3] == 'vertical':
                            if values[2] == 'X':
                                for i in range(values[0], values[0] + 3):
                                    colp = str(values[1]+1)
                                    i = str(i+1)
                                    self.do_jogar(i + ' ' + colp + ' ' + 'O')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(i + ' ' + colp + ' ' + 'X')
                                if check != 0:
                                    print('no solution for our algorithm')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                            if values[2] == 'O':
                                for i in range(values[0], values[0] + 3):
                                    colp = str(values[1]+1)
                                    i = str(i+1)
                                    self.do_jogar(i + ' ' + colp + ' ' + 'X')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(i + ' ' + colp + ' ' + 'O')
                                if check != 0:
                                    print('no solution for our algorithm for now')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                        elif values[3] == 'horizontal':
                            if values[2] == 'X':
                                for i in range(values[1], values[1] + 3):
                                    linep = str(values[0] + 1)
                                    i = str(i + 1)
                                    self.do_jogar(linep + ' ' + i + ' ' + 'O')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + i + ' ' + 'X')
                                    if check != 0:
                                        print('no solution for our algorithm')
                                        self.do_undoancora('ancora')
                                        eng.resetjogadas()
                                        self.do_resolver(puzzle_name)
                            elif values[2] == 'O':
                                for i in range(values[1], values[1] + 3):
                                    linep = str(values[0] + 1)
                                    i = str(i + 1)
                                    self.do_jogar(linep + ' ' + i + ' ' + 'X')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + i + ' ' + 'O')
                                if check != 0:
                                    print('no solution for our algorithm for now')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                        elif values[3] == 'diag_asc':
                            if values[2] == 'X':
                                for i in range(3):
                                    linep = str(values[0] + 1-i)
                                    colp = str(values[1] + 1-i)
                                    self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                if check != 0:
                                    print('no solution for our algorithm')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                            if values[2] == 'O':
                                for i in range(3):
                                    linep = str(values[0] + 1 - i)
                                    colp = str(values[1] + 1 - i)
                                    self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                if check != 0:
                                    print('no solution for our algorithm for now')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                        elif values[3] == 'diag_desc':
                            if values[2] == 'X':
                                for i in range(3):
                                    linep = str(values[0] + 1+i)
                                    colp = str(values[1] + 1+i)

                                    self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                if check != 0:
                                    print('no solution for our algorithm')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                            if values[2] == 'O':
                                for i in range(3):
                                    linep = str(values[0] + 1 + i)
                                    colp = str(values[1] + 1 + i)
                                    self.do_jogar(linep + ' ' + colp + ' ' + 'X')
                                    newtry = self.do_validar_resolver(puzzle_name)
                                    check = len(newtry[0])
                                    if check == 0:
                                        print('Puzzle válido e resolvido')
                                        self.do_gravar('Solução_{}'.format(puzzle_name))
                                        break
                                    else:
                                        self.do_jogar(linep + ' ' + colp + ' ' + 'O')
                                if check != 0:
                                    print('no solution for our algorithm for now')
                                    self.do_undoancora('ancora')
                                    eng.resetjogadas()
                                    self.do_resolver(puzzle_name)
                        else:
                            print('no solution for our algorithm for now')
            else:
                print('Erro nos argumentos')
        except:
            print("Erro ao validar o puzzle e/ou tabuleiro")


    def do_ancora(self, arg):
        " - comando âncora que deve guardar o ponto em que está o jogo para permitir mais tarde voltar a este ponto: ancora \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args <= 1:
                self.ancora = eng.gettabuleiro()
                file = open('ancora', 'w')
                file.write(str(len(eng.gettabuleiro())) + ' ' + str(len(eng.gettabuleiro()[0])))
                for i in eng.gettabuleiro():
                    file.write('\n')
                    for j in i:
                        file.write(str(j))
                        file.write(' ')
                print(self.ancora)
                print('tabuleiro guardado')
            else:
                print('Erro nos argumentos')
        except:
            print("Erro ao guardar o puzzle e/ou tabuleiro")

    def do_undoancora(self, arg):
        " - comando undo para voltar à última ancora registada: undoancora \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 1:

                eng.ler_tabuleiro_ficheiro('ancora')
                eng.printpuzzle()

            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao mostrar o puzzle")

    def do_gerar(self, arg):
        " - comando gerar que gera puzzles com solução única e leva três números inteiros como parâmetros: o nível de dificuldade (1 para ‘fácil’ e 2 para ‘difícil’), o número de linhas e o número de colunas do puzzle \n"

        try:
            lista_arg = arg.split(' ')
            num_args = len(lista_arg)
            if num_args == 3:
                file = open('new_puzzle', 'w')
                file.write(lista_arg[1] + ' ' + lista_arg[2])
                for i in range(int(lista_arg[1])):
                    file.write('\n')
                    if lista_arg[0] == '2':
                        for j in range(int(lista_arg[2])):
                            x = random.randrange(1,200)
                            if x <= 35:
                                w = random.choice(['O','X'])
                                file.write(w)
                                file.write(' ')
                            elif x<= 70:
                                file.write('#')
                                file.write(' ')
                            else:
                                file.write('.')
                                file.write(' ')
                    if lista_arg[0] == '1':
                        for j in range(int(lista_arg[2])):
                            x = random.randrange(1,200)
                            if x <= 70:
                                w = random.choice(['O','X','#'])
                                file.write(w)
                                file.write(' ')
                            else:
                                file.write('.')
                                file.write(' ')
                print('Necessita da validação por parte do utilizador')
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao montar o puzzle")


    def do_ver(self,arg):
        " - Comando para visualizar graficamente o estado atual do GandaGalo caso seja válido: VER  \n"
        try:
            if puzzle_name:
                arg = puzzle_name
                global janela  # pois pretendo atribuir um valor a um identificador global
                if janela is not None:
                    del janela  # invoca o metodo destruidor de instancia __del__()
                janela = GandaGaloWindow(40, eng.getlinhas(), eng.getcolunas())
                janela.mostraJanela(eng.gettabuleiro())
            else:
                print("Número de argumentos inválido!")
        except:
            print("Erro: ao mostrar o puzzle")

    def do_random(self,arg):
        try:
            lista_arg = arg.split(' ')
            num_args = len(lista_arg)
            if num_args == 2:
                lp = int(lista_arg[0])
                cp = int(lista_arg[1])
                x = eng.count3x3symbols(lp, cp)
                if x[0] > x[1]:
                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'X')
                if x[0] < x[1]:
                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + 'O')
                if x[0] == x[1]:
                    x = str(random.choice(('O', 'X')))
                    self.do_jogar(str(lp + 1) + ' ' + str(cp + 1) + ' ' + x)
            else:
                print("Número de argumentos inválido!")

        except:
            print("Erro: ao mostrar o puzzle")


    def do_sair(self, arg):
        "Sair do programa GandaGalo: sair"
        print('Obrigado por ter utilizado o Gandagalo, espero que tenha sido divertido!')
        global janela  # pois pretendo atribuir um valor a um identificador global
        if janela is not None:
            del janela  # invoca o metodo destruidor de instancia __del__()
        return True


if __name__ == '__main__':
    eng = GandaGaloEngine()
    janela = None
    sh = GandaGaloShell()
    sh.cmdloop()

'''


'''

