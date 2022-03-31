"""
1 - Crie um sistema de cadastro e login de um site, utilizando um username e
senha informados pelo usuário.

"""

# Resposta
login = False

print("Bem-vindo(a) ao cadastro do site!")

user = input("Crie o seu nome de usuário: ")
senha = input("Crie a sua senha: ")

print(" \n ___________________LOGIN____________________")

if input("Usuário: ") == user and input("Senha: ") == senha:
    login = True

if login:
    print(f"\n Bem vindo(a) {user}")
else:
    print("\n Usuário ou senha incorretos. Tente novamente!")
