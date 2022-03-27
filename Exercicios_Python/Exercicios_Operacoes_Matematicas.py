"""
Exercícios:
1 - Realizar a média das notas de 4 alunos.
2 - Converter uma temperatura de graus °C para ºF e para K.
Dados: ºF = ºC * 1.8 + 32, K = ºC + 273.15

"""

# Ex 01 - Resposta

Aluno_Miguel = 5.5
Aluno_Joao = 7.7
Aluno_Sofia = 9.8
Aluno_Mariana = 10

mediaDasNotas = (Aluno_Miguel + Aluno_Joao + Aluno_Sofia + Aluno_Mariana) / 4

print(f"A média das notas é: {mediaDasNotas}")

# Ex 02 - Resposta

temperaturaEmCelsius = float(input("Digite a temperatura em Graus °C: "))

temperaturaEmKelvin = temperaturaEmCelsius + 273.15
print(f"A temperatura de {temperaturaEmCelsius}°C convertida em graus Kelvin é de: {temperaturaEmKelvin}°K")

temperaturaEmFahrenheit = (temperaturaEmCelsius * 1.8) + 32
print(f"A temperatura de {temperaturaEmCelsius}°C convertida em graus Fahrenheit é de: {temperaturaEmFahrenheit}°F")
