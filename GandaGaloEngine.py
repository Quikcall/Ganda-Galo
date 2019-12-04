# -*- coding:utf-8 -*-
'''
Created on 1/12/2018

@author: valves
'''




class GandaGaloEngine:
    
    def __init__(self):
        self.linhas = 0
        self.colunas = 0
        self.tabuleiro = [] #matriz que representa o puzzle
        self.jogadas = []
    
    def ler_tabuleiro_ficheiro(self, filename):
        '''
        Cria nova instancia do jogo numa matriz
        :param filename: nome do ficheiro a ler
        '''
        try:
            ficheiro = open(filename, "r")
            lines = ficheiro.readlines() #ler as linhas do ficheiro para a lista lines
            dim = lines[0].strip('\n').split(' ')  # obter os dois numeros da dimensao do puzzle, retirando o '\n' 
            self.linhas = int(dim[0])  # retirar o numero de linhas
            self.colunas = int(dim[1])  # retirar o numero de colunas
            self.tabuleiro=[]
            for i in range(1,len(lines)):
                self.tabuleiro.append(lines[i].split())
            return self.tabuleiro
        except:
            print("Erro: na leitura do tabuleiro")
        else:
            self.ficheiro.close()
        return self.tabuleiro
    
    def printpuzzle(self):
        for linha in self.tabuleiro:
            for simbolo in linha:
                print(simbolo,end=" ")
            print()

    def count3x3symbols(self,lp,cp):
        x = 0
        o = 0
        o_x3 = []
        print('UI',len(self.tabuleiro))
        if lp + 1 <= len(self.tabuleiro) - 2 and cp +1 <= len(self.tabuleiro) - 2:
            for linha in self.tabuleiro:
                for simbolo in linha:
                    if simbolo == 'O':
                        o += 1
                    elif simbolo == 'X':
                        x += 1
        o_x3.append(o)
        o_x3.append(x)
        return o_x3

    def getlinhas(self):
        return self.linhas
    
    def getcolunas(self):
        return self.colunas
    
    def gettabuleiro(self):
        return self.tabuleiro

    def settabuleiro(self, t):
        self.tabuleiro = t

    def savejogadas(self, jogada):
        self.jogadas.append(jogada)
    def getjogadas(self):
        return self.jogadas
    def resetjogadas(self):
        self.jogadas = []
    def popjogadas(self, arg):
        return self.jogadas.pop(len(self.jogadas)-1)
    def removelast(self):
        self.jogadas = self.jogadas[0:(len(self.jogadas)-1)]
        print(self.jogadas)

    def validartabuleiro(self, arg):
        tab = open(arg, 'r')
        table = []
        table_strings = []
        temp = True
        for line in tab:
            table_strings.append(line.rstrip())
            table.append(line.rstrip().split(' '))
        print(table)
        if table[0][0] != table[0][1]:
            print('Medidas do puzzle não formam um quadrado')
            tempt = False
        for i in range(1, len(table)):
            for j in table[i]:
                if j not in ['.', '#', 'X', 'O']:
                    print('Caracteres não válidos')
                    tempt = False
                    break
        if temp:
            print('Tabuleiro com dimensões e caracteres válidos')






