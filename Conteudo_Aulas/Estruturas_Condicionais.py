"""
Estruturas Condicionais

- if (se)
- elif (senão se)
- else (senão)
"""

# Testar altura para brinquedos do parque (if / else)
altura = float(input("Digite sua altura: "))

if altura < 1.6:
    print("Você não pode entrar!")
else:
    print("Você pode brincar!")

# Consultar média final para aprovação (if / elif / else)
nota = float(input("Digite a sua nota: "))

if nota > 6:
    print("Pode curtir as suas merecidas férias!")
elif nota == 6:
    print("Foi por pouco, mas você passou!")
else:
    print("Te vejo ano que vem outra vez...")

# Consultar média final para aprovação (if / else)
nota = float(input("Digite a sua nota: "))

if nota >= 6:
    print("Pode curtir as suas merecidas férias!")
else:
    print("Te vejo ano que vem outra vez...")

# Determinar se um número é par ou ímpar
num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")

# ou
if num % 2 != 0:
    print(f"{num} é ímpar")
else:
    print(f"{num} é par")


# Utlizando outros tipos de dados

# Strings
pais = input("Digite um país que deseja visitar: ")

if pais == "Noruega":
    print("Ah não, muito frio!")
elif pais == "China":
    print("Ah não, muito longe!")
elif pais == "Austrália":
    print("Ah não, muito bicho gigante")
else:
    print("Oba, vou arrumar as malas!")

#Boolean
login = False
senha = "abc123"

key = input("Digite a sua senha: ")

if key == senha:
    login = True
else:
    print("Senha incorreta")

if login == True:
    print("Bem vindo, você entrou!")
else:
    print("Tente novamente")

#Cuidado com as variáveis locais e globais
"""
login = False #variável global

senha = "abc123"
key = "abc123" #abc1234

if key == senha:
    login = True #variável local
else:
    print("Senha incorreta")

if login == True:
    print("Bem vindo, você entrou!")
else:
    print("Tente novamente")
"""
