"""
Exercícios:

1 - Crie um programa que encontre e imprima as raízes de uma equação do
segundo grau, utilizando o método de Bhaskara.
"""

# Resposta
# Equação do segundo grau: A * x ** 2 + B * x + C

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b ** 2) - (4 * a * c)  # Encontrando o valor de delta

x1 = (-b + delta ** 0.5) / (2 * a)  # Encontrando as raízes de x1 e x2
x2 = (-b - delta ** 0.5) / (2 * a)

# Na matemática, a raiz quadrada de um número é igual a este elevado á meio (0.5)

print(f"As raízes são: {x1} e {x2}")
