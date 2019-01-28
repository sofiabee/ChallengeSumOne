#-*- coding: utf-8 -*-
from string import *
from operator import itemgetter

def processar_dados():
    arquivo = open("cliente.txt", 'r')
    dados = arquivo.read()
    dados = dados.split("Ordenação:")
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
        if i != '':
            aux = i.split(",")
            lista.append({'Livro':aux[0].split('-')[0], 'Título':aux[0].split('-')[1], 'Autor':aux[1], 'Edição':aux[2]}) #organiza os livros em dicionário
    return lista

lista = organizar_livros(livros)

def ordenar_zeroum(ordem, lista):
    if len(ordem) == 0:
        return lista
    elif len(ordem) == 1:
        if ordem[0][1] == "ascendente": #ordem[0][1] é a regra de ordenação: asc ou desc
            for i in sorted(lista, key=itemgetter(ordem[0][0])): #ordem[0][0] é o atributo
                print(i)
        else:
            for i in sorted(lista, key=itemgetter(ordem[0][0]), reverse=True): #como não é asc, é desc, então é só ordenar inversamente
                print(i)

def ordenar_doistres(ordem, lista):
    print(ordem)
    if ordem[0][1] == "ascendente":
        for i in sorted(lista, key=itemgetter(ordem[0][0], ordem[1][0])):
            print(i)
    else:
        for i in sorted(lista, key=itemgetter('Título', 'Autor', 'Edição')):
            print(i)


def ordenar():
    if len(ordem) <= 1:
        ordenar_zeroum(ordem, lista)
    else:
        ordenar_doistres(ordem, lista)
