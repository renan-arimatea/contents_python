"""
Exercícios:

1) Descubra quais erros estão presentes nos códigos abaixo:

a)
    nome = 'Mark'
    print(int(nome))

# Resposta: não podemos transformar uma string em um inteiro.

b)
    filme = 'Avatar'
    print('A maior bilheteria de 2009 foi {filme}')

# Resposta: faltou o f dentro do parênteses - print(f'A maior bilheteria de 2009
foi {filme}')

c)
    frase = 'Eu sou seu pai'
    print(frase[-1::])

# Resposta: Sintaxe incorreta, o certo é utilizar [::-1] para inverter a frase

d)
    numero1 = 10
    dado = int(input(Digite o numero que deseja: ))
    print(numero1 * dado)

# Resposta: faltou as aspas ""  - dado = int(input("Digite o numero que deseja: "))

"""

"""
2) Criação de personagem de mundo de ficção, apresentando opções de acordo
com os tipos das variáveis:

- Cor de Cabelo (string)
- Cor de pele (string)
- Classe: Guerreiro, Mago, Arqueiro (string)
- Idade (int)
- Altura (float)
- Habilidade Específica (string)

Imprima para o usuário o personagem completo.
"""

# Resposta

print("Vamos começar criando o seu personagem: ")

nome = input("Qual é o nome do seu personagem? ")
cabelo = input("Qual é a cor do cabelo do seu personagem? ")
pele = input("Qual é a cor da pele do seu personagem? ")
classe = input("Agora escolha a classe do seu personagem dentre: \n 1- Guerreiro\n 2 - Mago\n 3 - Arqueiro\n Opcao: ")
idade = int(input("Qual é a idade do seu personagem em anos? "))
altura = float(input("Qual é a altura do seu personagem em metros? "))
habilidade = input("Agora qual é a habilidade específica do seu personagem? ")

print("------------------------ Aguarde enquanto os deuses criam seu personagem -------------------- ")
print(f"--------------------------------Personagem criado com sucesso! ----------------------------- \n"
      f"-------------------------Abaixo você pode ver as caracteristica de {nome} ------------------- \n")

personagem = print(
                   f"Nome: {nome} \n"
                   f"Cor do cabelo: {cabelo} \n"
                   f"Cor da pele: {pele} \n"
                   f"Classe: {classe} \n"
                   f"Idade: {idade} \n"
                   f"Altura: {altura} \n"
                   f"Habilidade: {habilidade}"
                    )
