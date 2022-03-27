"""
Exercícios:
1) Relacione as colunas de acordo com o tipo da variável.

(1)Inteiros     (5) “Casa”
                (3) 2 + 0j
(2) Float       (4) True
                (5) ‘123’
(3) Complexo    (2) 1.2345
                (4) False
(4) Booleano    (5) ‘’’2j’’’
                (3) 10 + 1j
(5) String      (1) 2
                (5) ‘Programando Ideias’
"""

"""
2) Faça um programa que receba o nome de um aluno e quanto ele tirou na
prova de programação, depois imprima em apenas uma linha o nome no modo
title() e quanto a pessoa tirou na prova. Ex: Ana Carolina tirou 8
"""

nome = input("Qual é o nome do aluno(a)? ")
nota = input("Qual é a nota para este aluno(a)? ")

print(f"A nota do aluno(a) {nome.title()} foi de {nota}")
