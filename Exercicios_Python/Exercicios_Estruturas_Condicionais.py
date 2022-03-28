"""
1- Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira,
potência).

Peça a operação desejada e depois os dois números ao usuário.
"""
# Minha Resposta
print("escolha uma operação: \n"
      "1- soma \n"
      "2- multiplicação \n"
      "3- divisão \n"
      "4- potência \n")

operacao = int(input("Digite o número da operação voce deseja realizar? "))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operacao == 1:
    print(f'A soma é: {num1 + num2}')
elif operacao == 2:
    print(f"A multiplicação é: {num1 * num2}")
elif operacao == 3:
    print(f"A divisão é: {num1 / num2}")
elif operacao == 4:
    print(f"A potência é: {num1 ** num2}")
else:
    print("Operação inválida. Tente novamente!")


# Resposta Profesor
print('1 - Soma\n2 - Multiplicacao\n3 - Divisao Inteira\n4 - Potencia')

op = int(input('Escolha uma operação: '))

num1 = float(input('Primeiro numero: ')) #Convertendo o numero para float
num2 = float(input('Segundo numero: '))

if op == 1: #Testando o valor de 'op' para determinar o operador
 print(f'Soma: {num1 + num2}')
elif op == 2:
 print(f'Multiplicacao: {num1 * num2}')
elif op == 3:
 print(f'Divisao Inteira: {num1 // num2}')
elif op == 4:
 print(f'Potencia: {num1 ** num2}')
else:
 print('Digite uma opcao valida!')
