"""
Output - print(): Apresenta dados para o usuário

Input - input(): Recebe dados do usuário

"""

# MODO 01
print("Digite uma cor: ")
cor = input()

print(f"Você escolheu a cor {cor}")

# MODO 02
cor = input("Digite uma cor: ")

num = input("Digite um número: ")

print(f"Você escolheu a cor {cor} e o número {num}")

# Print sem pular linha

print("tomate")
print("tomate")
print("tomate")

print("tomate", end=" ")
print("tomate", end=" ")
print("tomate", end=" ")

# Realizar operações nas saídas (print)

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# soma = print(f"A soma dos números é: {num1 + num2}") # Erro: A soma vai estar errada

print(f"A soma é: {int(num1) + int(num2)}")

# obs.: Casting - conversão de um tipo de dado para outro.
