'''Exercício Python 20:
 O mesmo professor do desafio 19
 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos
 e mostre a ordem sorteada.'''
from random import shuffle
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
