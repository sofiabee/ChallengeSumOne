#-*- coding: utf-8 -*-
from string import *
from operator import itemgetter
from functools import cmp_to_key

def processar_dados():
    arquivo = open("cliente.txt", 'r')
    dados = arquivo.read()
    dados = dados.split("Ordenação: ")
    return dados

dados = processar_dados()

def processar_ordem(dados):
    ord = dados[1]
    ord = ord.split(', ')
    ordem = []
    for i in ord:
        ordem.append(i.split(' '))
    return (ordem)

ordem = processar_ordem(dados)

def processar_livros(dados):
    livros = dados[0]
    livros = livros.split("\n")
    return livros

livros = processar_livros(dados)

def organizar_livros(livros):
    lista = []
    for i in livros:
        l =[]
        if i != '':
            aux = i.split(",")
            l.append(str([aux[0].split('-')[0]]).strip("[").strip(']').strip("'"))         #limpando a lista
            l.append(str([aux[0].split('-')[1]]).strip("[").strip(']').strip("'"))
            l.append(str([aux[1]]).strip("[").strip(']').strip("'"))
            l.append(str([aux[2]]).strip("[").strip(']').strip("'"))
            lista.append(l)
    return lista

lista = organizar_livros(livros)

index = {'Título':1, 'Autor':2, 'Edição':3} #facilitar localização

def ordenar_zeroum(ordem, lista):
    i = index[ordem[0][0]]     #identifica index do atributo
    if len(ordem) == 0:
        return lista
    elif len(ordem) == 1:
        if ordem[0][1] == "ascendente":
            for i in sorted(lista, key=itemgetter(i)):
                print(i)
        else:
            for i in sorted(lista, key=itemgetter(i), reverse=True):
                print(i)

def ordena_2(livro_1, livro_2):
    i = index[ordem[0][0]]
    if livro_1[i] < livro_2[i]: # compara título
        if ordem[0][1] == 'descendente':
            return 1
        else:
            return -1
    elif livro_1[i] > livro_2[i]: # compara título
        if ordem[0][1] == 'descendente':
            return -1
        else:
            return 1
    else: # títulos empatados
        j = index[ordem[1][0]]
        if livro_1[j] < livro_2[j]: # compara autor
            if ordem[1][1] == 'descendente':
                return 1
            else:
                return -1
        elif livro_1[j] > livro_2[j]: # compara autor
            if ordem[1][1] == 'descendente':
                return -1
            else:
                return 1
        else: # autores empatados
            return 0

def ordena_3(livro_1, livro_2):
    i = index[ordem[0][0]]
    if livro_1[i] < livro_2[i]: # compara título
        if ordem[0][1] == 'descendente':
            return 1
        else:
            return -1
    elif livro_1[i] > livro_2[i]: # compara título
        if ordem[0][1] == 'descendente':
            return -1
        else:
            return 1
    else: # títulos empatados
        j = index[ordem[1][0]]
        if livro_1[j] < livro_2[j]: # compara autor
            if ordem[1][1] == 'descendente':
                return 1
            else:
                return -1
        elif livro_1[j] > livro_2[j]: # compara autor
            if ordem[1][1] == 'descendente':
                return -1
            else:
                return 1
        else: # autores empatados
            k = index[ordem[2][0]]
            if livro_1[k] < livro_2[k]:
                if ordem[2][1] == 'descendente':
                    return 1
                else:
                    return -1
            elif livro_1[k] > livro_2[k]:
                if ordem[2][1] == 'descendente':
                    return -1
                else:
                    return 1
            else:
                return 0

def ordenar(ordem, lista):
    if len(ordem) <= 1:
        ordenar_zeroum(ordem, lista)
    elif len(ordem) == 2:
        L = sorted(lista, key=cmp_to_key(ordena_2))
        for i in L:
            print(i)
    elif len(ordem) == 3:
        L = sorted(lista, key=cmp_to_key(ordena_3))
        for i in L:
            print(i)

ordenar(ordem,lista)