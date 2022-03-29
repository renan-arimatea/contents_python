"""
Estruturas Lógicas

and (e): True apenas se todas as condições forem True

or (ou): True quando pelo menos uma condição for True

is (é): Comparação entre valores, similar ao ==

not (não): Inversão do valor booleano (True -> False, False -> True)
"""

# and

# Exemplo 01
sensor = 68  # range de segurança do sensor: 60 a 75

if sensor >= 60 and sensor <= 75:
    print("Tudo OK!")
else:
    print("ATENÇÃO FALHA DETECTADA")

# Exemplo 02
agua = True
comida = True

if agua and comida:
    print("Cachorro feliz!")
else:
    print("Cachorro triste")


# or

# Exemplo 01
pizza = True
lasanha = False

if pizza or lasanha:
    print("Preciso comer mais salada")
else:
    print("Estou com fome")

# Exemplo 02
num = 7

if num % 2 == 0 or num < 10:
    print("É par ou menor que 10")
else:
    print("É ímpar e maior ou igual a 10")


# is

# Exemplo 01
login = False

print(login is True)  # login é True? Não (False)
print(login is False)  # login é False? Sim (True)

if login is True:
    print("logado")
else:
    print("deslogado")


# not

# Exemplo 01
login = True

if not login:
    print("deslogado")
else:
    print("logado")
